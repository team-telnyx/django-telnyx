=============================
Django Telnyx
=============================

.. image:: https://badge.fury.io/py/django-telnyx.svg
    :target: https://badge.fury.io/py/django-telnyx

.. image:: https://travis-ci.org/luizanao/django-telnyx.svg?branch=master
    :target: https://travis-ci.org/luizanao/django-telnyx

.. image:: https://codecov.io/gh/luizanao/django-telnyx/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/luizanao/django-telnyx




The simplest way to integrate Django apps to Telnyx API's.

Documentation
-------------

The full documentation will be available at readthedocs shortly.

Quickstart
----------

Install django-telnyx::

    pip install django-telnyx

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_telnyx.apps.DjangoTelnyxConfig',
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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
