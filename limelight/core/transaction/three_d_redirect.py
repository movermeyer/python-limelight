# -*- coding: utf-8 -*-

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

from .transaction_method import TransactionMethod


class ThreeDRedirect(TransactionMethod):
    def parse_response(self, response):
        self.__save_response_data({k: v for k, v in parse_qs(response).items()})

    validate = {'order_id': lambda x: isinstance(x, int)}

    @property
    def __name__(self):
        return 'three_d_redirect'