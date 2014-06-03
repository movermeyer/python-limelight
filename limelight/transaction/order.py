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
    An order object, probably a mixin eventually.
    """
    pass
