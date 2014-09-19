# -*- coding: utf-8 -*-

from voluptuous import Required, Optional

from ._schema import condition_for
from ..request import MembershipMethod


class OrderUpdate(MembershipMethod):
    __name__ = 'order_update'
    schema = {Required('order_ids'): condition_for['order_ids'],
              Required('actions'): condition_for['actions'],
              Required('values'): condition_for['values'], }