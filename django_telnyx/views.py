"""

Webhook Class View.

All incoming webhooks pointed to `WEBHOOK_URL` will be handled by `WebhookView`
which will make sure the request is a valid, comes from Telnyx servers and they are
properly signed.
"""
import logging

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from . import telnyx
from .settings import WEBHOOK_PUBLIC_KEY
from .signals import WEBHOOK_SIGNALS

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name="dispatch")
class WebhookView(View):
    """Verify incoming requests class"""

    def post(self, request):
        """Verify webhooks and make sure they were sent by Telnyx and it's a valid and
        signed request
        """
        telnyx.public_key = WEBHOOK_PUBLIC_KEY
        if request.content_type != "application/json":
            return HttpResponseBadRequest()

        payload = request.body
        signature = request.headers.get("Telnyx-Signature-Ed25519")
        timestamp = request.headers.get("Telnyx-Timestamp")

        if not (signature and timestamp):
            return HttpResponseBadRequest()

        webhook_event = telnyx.Webhook.construct_event(payload, signature, timestamp)
        try:
            WEBHOOK_SIGNALS[webhook_event.data.event_type].send(
                sender=self.__class__, event=webhook_event
            )
        except KeyError as ke:
            logger.warning(
                "Event type '%s' unknown or not registered. Webhook will not be handled",
                ke.args[0],
            )

        return HttpResponse("OK")
