"""
Webook `Signals` to handlers.

Here all the webhooks events needs to be registered in order to available to `webhook`
decorator when user choose to use it - Otherwise an exception UnknownEventTypeException
will be raised.

Check individual sections to learn more about possible events:
https://developers.telnyx.com/docs/v2/call-control/receiving-webhooks
"""
from django.dispatch import Signal

WEBHOOK_SIGNALS = dict(
    [
        (hook, Signal(providing_args=["event"]))
        for hook in ["message.sent", "message.received", "message.finalized"]
    ]
)
