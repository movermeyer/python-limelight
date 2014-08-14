# -*- coding: utf-8 -*-

try:
    from eventlet.green.urllib.request import urlopen
except ImportError:
    from eventlet.green.urllib2 import urlopen

from eventlet.green.socket import timeout as Timeout
from eventlet.green.ssl import SSLError

from copy import copy

from .. import utils


class Request(object):
    def __save_response_data(self, data):
        for k, v in data.items():
            setattr(self, utils.to_underscore(k), utils.to_python(v))

    def parse_response(self, response):
        raise NotImplementedError

    def __make_request(self, request_data, tried=0):
        data = copy(request_data)
        data.update({'method': self.__name__,
                     'username': '',
                     'password': ''})
        try:
            request = urlopen(self.endpoint,
                              {utils.to_camel_case(k): v for k, v in data.items()},
                              timeout=12)
            self.parse_response(request.read())
            return self.response_code
        except (Timeout, SSLError):
            if tried <= 3:
                return self.__make_request(request_data, tried=tried + 1)
            else:
                raise Exception

    endpoint = property(utils.not_implemented)
    response_code = property(utils.not_implemented)
    error = property(utils.not_implemented)