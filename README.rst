|build| |downloads| |license|

Python-LimeLight
================

A pythonic Lime Light API wrapper.

We currently support only a subset of the full Lime Light API functionality, we will be adding
methods and plan to achieve total coverage some time during the next several months.

``python-limelight`` contains two modules that implement the two APIs that Lime Light exposes. Lime
Light calls these APIs their Transaction and Membership APIs, we've implemented them as
``limelight.transaction`` and ``limelight.membership``. Both are essentially an 1:1 mapping of
pythonic-as-possible functions to API methods. Unfortunately, Lime Light's API is pretty much all
over the place. It's comprehensive and useful, but not well organized or consistent.

Our solution is designed for both flexibility and ease of use: the entire API is exposed in python
in the aforementioned modules and is used as machinery for a much more cohesive interface to the
CRM.

Additionally, ``python-limelight`` implements extensive client-side data validation to limit the
amount of time spent waiting for a response (which can take up to *thirty seconds*).

Installation
~~~~~~~~~~~~

``python-limelight`` is available on PyPi:

    pip install python-limelight

Though, for the time being we recommend you track the git repo:

    pip install git+https://github.com/heropunch/python-limelight.git@master

Making API Calls
~~~~~~~~~~~~~~~~

    >>> import os
    >>> from limelight.api import TransactionClient
    >>> client = TransactionClient(host=os.environ['LIMELIGHT_HOST'],
                                   username=os.environ['LIMELIGHT_USER'],
                                   password=os.environ['LIMELIGHT_PASSWORD'])
    >>> client.NewOrder(**order_data)
    <limelight.transaction.new_order.NewOrder object at 0x106f8a1d0>

.. |build| image:: https://travis-ci.org/heropunch/python-limelight.svg
   :target: https://travis-ci.org/heropunch/python-limelight
   :alt: Travis-CI

.. |license| image:: https://pypip.in/license/python-limelight/badge.png
   :target: https://pypi.python.org/pypi/python-limelight/
   :alt: License

.. |downloads| image:: https://pypip.in/download/python-limelight/badge.png
   :target: https://pypi.python.org/pypi/python-limelight/
   :alt: Downloads
