# -*- coding: utf-8 -*-

from . import membership, transaction
from .. import utils


class Client(object):
    """
    A Lime Light API client object.
    """
    method_package = property(utils.not_implemented)

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def __getattr__(self, item):
        method_class = getattr(self.method_package, item)
        setattr(method_class, 'host', self.host)
        setattr(method_class, 'username', self.username)
        setattr(method_class, 'password', self.password)
        return method_class


class Membership(Client):
    method_package = membership


class Transaction(Client):
    method_package = transaction