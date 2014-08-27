# -*- coding: utf-8 -*-

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

from . import utils
from .request import Request


class TransactionMethod(Request):
    def parse_response(self, response):
        self.__save_response_data({utils.to_underscore(k): utils.to_python(v)
                                   for k, v in parse_qs(response).items()})

    @property
    def endpoint(self):
        return "https://{host}/admin/transact.php".format(host=self.host)


class MembershipMethod(Request):
    @property
    def endpoint(self):
        return "https://{host}/admin/membership.php".format(host=self.host)
