# -*- coding: utf-8 -*-
"""
Lime Light Response
~~~~~~~~~~~~~~~~~~~

Appendix A – Response Codes and Meanings

100 – Success

"""

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

try:
    from urllib.parse import parse_qs
except ImportError:
    from urlparse import parse_qs
import socket

import ssl

from limelight.errors import (LimeLightException, TransactionDeclined, )
from limelight.utils import to_underscore, to_python


class Response(object):
    """
    Supposed to make working with Lime Light's responses nicer.
    """
    def __init__(self, request):
        lime_light_response = self.__read_response(request)
        for k, v in parse_qs(lime_light_response).items():
            setattr(self, to_underscore(k), to_python(v))
        if self.is_success() is False:
            if self.response_code == 800:
                raise TransactionDeclined(self.decline_reason)
            else:
                raise LimeLightException(self.response_code)

    def is_success(self):
        return all((hasattr(self, 'response_code'), self.response_code == 100))

    @staticmethod
    def __read_response(request, tried=0):
        try:
            return urlopen(request, timeout=12).read()
        except (socket.timeout, ssl.SSLError):
            if tried <= 3:
                return Response.__read_response(request, tried=tried + 1)
            else:
                raise LimeLightException("Request timed out, try again in a few minutes.")