# -*- coding: utf-8 -*-

import re

ALPHANUMERIC = re.compile(r'^(?:[\w ](?!_))+$')
NUMERIC = re.compile(r'^[0-9]+$')


def is_alphanumeric(length):
    def _is_alphanumeric(string):
        if len(string) == length or length == 0:
            return bool(re.match(ALPHANUMERIC, string))
        else:
            return False
    return _is_alphanumeric


def is_numeric(length):
    def _is_numeric(number):
        if len(str(number)) == length or length == 0:
            return bool(re.match(NUMERIC, str(number)))
        else:
            return False
    return _is_numeric