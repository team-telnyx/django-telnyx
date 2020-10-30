"""General settings for Django-Telnyx

These variables are meant to be overwritten in the top-level app
"""
from django.conf import settings

API_KEY = getattr(settings, "TELNYX_API_KEY", "")
WEBHOOK_PUBLIC_KEY = getattr(settings, "TELNYX_WEBHOOK_PUBLIC_KEY", "")
WEBHOOK_URL = getattr(settings, "TELNYX_WEBHOOK_URL", "webhook/")
