"""
House of Messaging related features.

This module works as as Proxy to Telnyx SDK commands.
See: github.com/team-telnyx/telnyx-python for more info.
"""
from . import telnyx


def sms(  # pylint: disable=invalid-name
    to: str, from_: str, text: str
) -> telnyx.api_resources.message.Message:  # pylint: disable=invalid-name
    """Proxy method call to `telnyx.Message.create`

    :param to: Destination E.164 phone number format
    :type to: str
    :param from_: Sender E.164 phone number format
    :type from_: str
    :param text: SMS text content
    :type text: str
    :return: Message obj
    :rtype: telnyx.api_resources.message.Message

    Usage:
        ```
        from django_telnyx import messaging
        messaging.sms(from_='+1111111111', to='+22222222', text="Hello World!")
        ```
    """
    return telnyx.Message.create(
        from_=from_,
        to=to,
        text=text,
    )
