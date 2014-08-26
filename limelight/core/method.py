# -*- coding: utf-8 -*-

from .. import utils
from .request import Request


class TransactionMethod(Request):
    @property
    def endpoint(self):
        return "https://{host}/admin/transact.php".format(host=self.host)

    host = property(utils.not_implemented)


class MembershipMethod(Request):
    @property
    def endpoint(self):
        return "https://{host}/admin/membership.php".format(host=self.host)

    host = property(utils.not_implemented)