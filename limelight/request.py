# -*- coding: utf-8 -*-

from requests import post, get, ConnectionError, Timeout

from copy import copy

from voluptuous import Schema

from . import utils, errors


class Request(object):
    """
    The superclass of all Lime Light API methods.


    """
    TIMEOUT = 12
    MAX_TRIES = 3
    VERIFY_CERT = True
    preserve_field_labels = None
    http_method = 'POST'
    schema = utils.not_implemented
    endpoint = utils.not_implemented
    error = utils.not_implemented

    def __init__(self, host=None, username=None, password=None, **kwargs):
        self.host = host
        self.username = username
        self.password = password
        self.response = None
        cleaned_data = Schema(self.schema)(kwargs)
        self.__make_request(cleaned_data)

    def __make_request(self, request_data, tried=0):
        """
        :param request_data: Data being sent over to Lime Light
        :type request_data: dict
        :param tried: The number of times the request has been tried so far. By default,
                      ``__make_request`` will attempt a request three times before giving up
        :type tried: int
        :rtype: None
        """
        if self.preserve_field_labels is not None:
            data = {}
            for key, value in request_data.items():
                if key in self.preserve_field_labels:
                    data[key] = value
                else:
                    data[utils.to_camel_case(key)] = value
        else:
            data = copy(request_data)
        data.update({'method': self.__name__,
                     'username': self.username,
                     'password': self.password})
        try:
            if self.http_method.upper() == 'POST':
                self.response = post(self.endpoint, data=data, timeout=self.TIMEOUT,
                                     verify=self.VERIFY_CERT)
            elif self.http_method.upper() == 'GET':
                self.response = get(self.endpoint, params=data, timeout=self.TIMEOUT,
                                    verify=self.VERIFY_CERT)
            else:
                raise errors.ImproperlyConfigured(self.__name__, '.http_method should be one of ',
                                                  '"GET" or "POST"')
        except (Timeout, ConnectionError):
            if tried <= self.MAX_TRIES:
                return self.__make_request(request_data, tried=tried + 1)
            else:
                raise


class TransactionMethod(Request):
    preserve_field_labels = {'click_id', 'preserve_force_gateway', 'thm_session_id',
                             'total_installments', 'alt_pay_token', 'alt_pay_payer_id',
                             'force_subscription_cycle', 'recurring_days', 'subscription_week',
                             'subscription_day', 'master_order_id', 'temp_customer_id',
                             'auth_amount', 'cascade_enabled', 'save_customer', }

    def __init__(self, **kwargs):
        kwargs['tran_type'] = 'Sale'
        super(TransactionMethod, self).__init__(**kwargs)

    @property
    def endpoint(self):
        return "https://{host}/admin/transact.php".format(host=self.host)


class MembershipMethod(Request):
    @property
    def endpoint(self):
        return "https://{host}/admin/membership.php".format(host=self.host)