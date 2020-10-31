"""
Decorators for hadnling webhooks.

As webhooks requests are originaly handled by `WebhookView` class, these decorators
connects custom methods to Signals.

`WebhookView` send signals to incoming `Event.event_type` and users can capture these
events using decorators - if users try to captuer an non-valid event an
UnknownEventTypeException will be raised.

"""
import logging
from functools import wraps
from typing import List, Tuple, Union

from .signals import WEBHOOK_SIGNALS

__all__ = ["webhook", "all_webhooks"]

logger = logging.getLogger(__name__)


class UnknownEventTypeException(Exception):
    """Custom Exception for unknown event types handling"""

    pass


def webhook(event_types: Union[str, List[str], Tuple[str]], **kwargs):
    """
    A decorator for connecting receivers to webhook signals.
    Method accept one or more event_type.

    Note: Be aware that you can have as much methods receiving the same `Signal` as you
    want at the same time. Also this can co-exist alongside to `all_webhooks`, in this
    case, both decorated methods will handle it.

        @webhook("message.sent")
        def my_hook_handler(event):
            ...

        @webhook("message.sent", "message.finalized")
        def my_hook_handler(event):
            ...

        @webhook(["message.sent", "message.finalized"])
        def my_hook_handler(event):
            ...
    """

    def _decorator(func):
        try:
            if isinstance(event_types, (list, tuple)):
                for s in event_types:
                    WEBHOOK_SIGNALS[s].connect(func, **kwargs)
            else:
                WEBHOOK_SIGNALS[event_types].connect(func, **kwargs)
        except KeyError as ke:
            _msg = f"Event type '{ke.args[0]}' unknown or not registered."
            logger.error(_msg)
            raise UnknownEventTypeException(_msg) from None

        return func

    return _decorator


def all_webhooks(func, *args, **kwargs):
    """
    A decorator for connecting receiver to all webhook signals.
    The method that is decorated with this will handle all incoming webhooks.

    Note: Be aware that you can have as much methods receiving the same `Signal` as you
    want at the same time. Also this can co-exist alongside to `webhook`, in this
    case, both decorated methods will handle it.

        @all_webhooks
        def my_hook_handler(event):
            ...
    """

    @wraps(func)
    def _decorator(*args, **kwargs):
        for hook in WEBHOOK_SIGNALS:
            WEBHOOK_SIGNALS[hook].connect(func, *args, **kwargs)
        return func

    return _decorator(*args, **kwargs)
