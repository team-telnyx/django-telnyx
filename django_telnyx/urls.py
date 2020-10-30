"""
Django_telnyx urls

This register `settings.WEBHOOK_URL` as an URl to receive webhooks requests.

    Usage:
    ```
    urlpatterns = [
        ...
        url(r"^", include("django_telnyx.urls", namespace="django_telnyx")),
    ]
    ```
"""
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import settings, views

app_name = "django_telnyx"  # pylint: disable=invalid-name

urlpatterns = [
    url(rf"^{settings.WEBHOOK_URL}", views.WebhookView.as_view(), name="webhook"),
]
