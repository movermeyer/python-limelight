# -*- coding: utf-8 -*-

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs

from .. import utils
from .request import Request


class TransactionMethod(Request):
    def parse_response(self, response):
        for k, v in parse_qs(response).items():
            setattr(self, utils.to_underscore(k), utils.to_python(v))

    @property
    def endpoint(self):
        return "https://{host}/admin/transact.php".format(host=self.host)

    host = property(utils.not_implemented)


class MembershipMethod(Request):
    @property
    def endpoint(self):
        return "https://{host}/admin/membership.php".format(host=self.host)

    host = property(utils.not_implemented)