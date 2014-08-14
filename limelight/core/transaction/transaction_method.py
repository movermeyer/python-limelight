# -*- coding: utf-8 -*-

from ... import utils
from ..request import Request
from ..error import ValidationError


class TransactionMethod(Request):
    def __init__(self, **kwargs):
        for field, rule in self.validate.items():
            if hasattr(self, field) and rule(getattr(self, field)):
                pass
            else:
                raise ValidationError()
        self.__make_request(kwargs)

    validate = property(utils.not_implemented)