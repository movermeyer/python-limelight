# -*- coding: utf-8 -*-

from ..method import TransactionMethod
from .. import validations


class AuthorizePayment(TransactionMethod):
    def parse_response(self, response):
        pass

    validate = {'billing_first_name': validations.is_alphanumeric(64),
                'billing_last_name': validations.is_alphanumeric(64),
                'billing_address1': validations.is_alphanumeric(64),
                'billing_address2': validations.is_alphanumeric(64),
                'billing_city': validations.is_alphanumeric(32),
                'billing_state': None,
                'billing_zip': validations.is_numeric(10)}