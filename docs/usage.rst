=====
Usage
=====

To use django-telnyx in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_telnyx',
        ...
    )

Add django-telnyx's URL patterns:

.. code-block:: python

    from django_telnyx import urls as django_telnyx_urls


    urlpatterns = [
        ...
        url(r'^', include(django_telnyx_urls)),
        ...
    ]
