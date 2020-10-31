"""
Example view intended to demo how to use django_telnyx features and decorators
"""
from django.http import HttpResponse

from django_telnyx import messaging
from django_telnyx.decorators import all_webhooks, webhook

# Fill your phone numbers
FROM_NUMBER = ""
TO_NUMBER = ""


def my_first_sms(request):  # pylint: disable=unused-argument
    """"Example method of how to send SMS"""
    messaging.sms(from_=FROM_NUMBER, to=TO_NUMBER, text="Hello World!")
    return HttpResponse("<h1>Page was Sent</h1><p>Wait for webhooks</p>")


@webhook("message.sent")
def sms_sent_handler(event, **kwargs):  # pylint: disable=unused-argument
    """Example method of how to handler `message.sent` events"""
    print(f"Request Sent! This is how the Event looks like: {event}")


@webhook("message.finalized")
def sms_finalized_handler(event, **kwargs):  # pylint: disable=unused-argument
    """Example method of how to handler `message.finalized` events"""
    print(f"Request Finalized with status: {event.data.payload.to[0].status}")


@all_webhooks
def any_wehbhook_handler(event, **kwargs):  # pylint: disable=unused-argument
    """Example method of how to handler all events indepent of it types"""
    print("Im receiving all webhooks!")
