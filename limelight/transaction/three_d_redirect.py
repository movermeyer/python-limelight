# -*- coding: utf-8 -*-

from voluptuous import Required

from ..request import TransactionMethod


class ThreeDRedirect(TransactionMethod):
    """
    Starts 3DS redirect process.

    :param order_id: order_id that is in 3DS wait order status
    """
    @property
    def __name__(self):
        return 'three_d_redirect'

    schema = {Required('order_id'): int}