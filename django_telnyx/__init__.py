"""Django-telnyx Module"""

import telnyx

from .settings import API_KEY, WEBHOOK_PUBLIC_KEY

telnyx.api_key = API_KEY

__version__ = "0.1.0"
