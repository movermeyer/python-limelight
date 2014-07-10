# -*- coding: utf-8 -*-

from six import with_metaclass


class BaseOrder(type):
    """
    Baseclass for order objects.

    Handles validation, among other things.
    """
    pass


class Order(object):
    """
    An order object
    """
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def submit(self, use_auth=False, card_on_file=False, has_prospect=False):
        pass