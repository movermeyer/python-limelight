# -*- coding: utf-8 -*-

from . import utils
import membership
import transaction


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
        method_class = getattr(transaction, item, None)
        method_class = getattr(membership, item) if method_class is None else method_class
        if method_class is None:
            raise AttributeError
        setattr(method_class, 'host', self.host)
        setattr(method_class, 'username', self.username)
        setattr(method_class, 'password', self.password)
        return method_class

