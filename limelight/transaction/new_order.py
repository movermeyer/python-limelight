# -*- coding: utf-8 -*-

from voluptuous import Schema, Required, Optional, All, Length

from ..method import TransactionMethod


class NewOrder(TransactionMethod):
    schema = Schema({Required('first_name'): All(str, Length(max=64)),
                     Required('last_name'): All(str, Length(max=64)),
                     Required('shipping_address1'): str,
                     Optional('shipping_address2'): str,
                     Required('shipping_city'): str, })