# -*- coding: utf-8 -*-

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

from ..method import TransactionMethod
from .. import validations


class ThreeDRedirect(TransactionMethod):
    def parse_response(self, response):
        self.__save_response_data({k: v for k, v in parse_qs(response).items()})

    validate = {'order_id': validations.is_numeric(0)}

    @property
    def __name__(self):
        return 'three_d_redirect'