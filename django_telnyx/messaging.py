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

    See: https://developers.telnyx.com/docs/api/v2/messaging/Messages#createMessage
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


def sms_number_pool(
    messaging_profile_id: str, to: str, text: str
) -> telnyx.api_resources.message.Message:
    """Proxy method call to `telnyx.Message.create`

    :param message_profile_id: message profile id (uuid) - Check Telnyx docs to see how
    to create one
    :type message_profile_id: str
    :param to: Destination E.164 phone number format
    :type to: str
    :param text: SMS text content
    :type text: str
    :return: Message obj
    :rtype: telnyx.api_resources.message.Message

    See: https://developers.telnyx.com/docs/api/v2/messaging/Messages#createNumberPoolMessage
    Usage:
        ```
        telnyx.Message.create(
            messaging_profile_id ="uuid", # Your messaging profile id
            to="+1111111111",
            text="Hello World!"
        )
        ```
    """
    return telnyx.Message.create(
        messaging_profile_id=messaging_profile_id,
        to=to,
        text=text,
    )


def get_sms(sms_id: str) -> telnyx.api_resources.message.Message:
    """Proxy method call to `telnyx.Message.retrieve`

    Note: This API endpoint can only retrieve messages that are no older than 10 days
    since their creation.

    :param sms_id: An id of SMS (uuid formated)
    :type sms_id: str
    :return: Message obj
    :rtype: telnyx.api_resources.message.Message

    See: https://developers.telnyx.com/docs/api/v2/messaging/Messages#retrieveMessage
    Usage:
        ```
        telnyx.Message.retrieve("uuid")
        ```
    """
    return telnyx.Message.retrieve(id=sms_id)
