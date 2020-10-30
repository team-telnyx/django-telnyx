"""Example App URLS"""
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

from tests.example_app.views import my_first_sms

urlpatterns = [
    url(r"^send_sms/", my_first_sms),
    url(r"^admin/", admin.site.urls),
    url(r"^", include("django_telnyx.urls", namespace="django_telnyx")),
]
