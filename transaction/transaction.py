# -*- coding: utf-8 -*-

import urlparse
import urllib
import urllib2

from limelight.response import Response
from limelight.errors import (ImproperlyConfigured,
                              RequestError,
                              NoPreviousOrder, )
from limelight.utils import to_camel_case


class Transaction(object):
    """
    Exposes the Lime Light Transaction API as instance methods.
    """
    required_fields = ('customer', 'ip_address', 'product', 'upsell_count', 'upsell_products',
                       'campaign_id', 'date', 'payment_method', 'shipping_address', 'quantity')
    request_string = "{endpoint}/admin/transact.php?{query_string}".format
    tracking_map = {'offer_id': 'C1',
                    'affiliate_id': 'AFID',
                    'affiliate_sub_id': 'SID',
                    'affiliate_sub_id2': 'AID'}

    @property
    def tracking_keys(self):
        for k in self.tracking_map.iterkeys():
            yield k
    credit_card_map = {'first_name': 'billing_first_name',
                       'last_name': 'billing_last_name',
                       'type': 'credit_card_type',
                       'number': 'credit_card_number',
                       'expires': 'expiration_date',
                       'ccv': 'CCV'}

    @property
    def credit_card_keys(self):
        for k in self.credit_card_map.iterkeys():
            yield k

    def __init__(self, username, password, endpoint=None):
        """
        :param username: Username used for API calls
        :param password: Password used for API calls
        :param endpoint: API endpoint
        :raises ImproperlyConfigured: if any args are falsy
        """
        if not all((username, password, endpoint)):
            raise ImproperlyConfigured
        self.username = username
        self.password = password
        self.endpoint = endpoint

    def __request(self, method, **kwargs):
        """
        This is what requests are made of!

        Converts python-style keys in kwargs into CamelCase keys and urlencodes the resulting dict.

        :param method: API method
        :param kwargs: Data being passed into the method
        :return: Lime Light response
        """
        kwargs['username'] = self.username
        kwargs['password'] = self.password
        kwargs['method'] = to_camel_case(method, initial_cap=True)
        query_string = urllib.urlencode(**{to_camel_case(k): v for k, v in kwargs.iteritems()})
        request = self.request_string(endpoint=self.endpoint,
                                      query_string=query_string)
        try:
            response = urllib2.urlopen(request, timeout=7).read()
            return Response(**urlparse.parse_qs(response))
        except urllib2.URLError as e:
            raise RequestError(e)

    def new_order(self, order):
        """
        Creates a new order in Lime Light.

        Takes a local order object, pulls out, and formats the information. All of that is sent to
        ```__request``` which makes the Lime Light method call.

        :param careers.models.Order order: Order information
        """
        new_order = {k: v for k, v in order.__dict__.iteritems() if k in self.required_fields}
        customer = new_order.pop('customer', None)
        credit_card = new_order.pop('payment_method', None)
        response, auth_data = self._authorize_payment(customer, credit_card,
                                                      product=order.product,
                                                      campaign_id=order.campaign_id)
        if not response.is_success():
            raise
        new_order.update(auth_data)
        address = new_order.pop('address', None)
        for k, v in address.__dict__.iteritems():
            key = 'address1' if k == 'street' else k
            new_order['shipping_' + key] = v
            new_order['billing_' + key] = v
        partial_ = customer.partial
        for k, v in partial_.__dict__.iteritems():
            if k in self.tracking_keys:
                new_order[self.tracking_map[k]] = v
        if 'transaction_id' in partial_ and partial_['transaction_id'] is not None:
            new_order['transaction_id'] = partial_['transaction_id']
        new_order['tran_type'] = 'Sale'
        try:
            response = self.__request('new_order', **new_order)
            return response
        except:
            raise

    def new_order_card_on_file(self, product, previous_order_id=None, upsell=None, partial=None):
        """
        :param product:
        :param previous_order_id:
        :param list upsell:
        """
        if not all((product, previous_order_id, partial)):
            raise ValueError("All arguments are required!")
        new_order = {self.tracking_map[k]: v for k, v in partial.__dict__.iteritems() if k in self.tracking_keys}
        new_order['product_id'] = product
        new_order['previous_order_id'] = previous_order_id
        return self.__request('new_order_card_on_file', **new_order)

    def new_order_with_prospect(self):
        """
        """
        raise NotImplementedError

    def _authorize_payment(self, customer, credit_card, product=None, campaign_id=None):
        """
        Authorize payment

        :param bizopp.models.User customer:
        :param careers.models.CreditCard credit_card:
        :param careers.models.Product product:
        :param int campaign_id:
        """
        if not all((customer, credit_card, product, campaign_id)):
            raise ValueError("All arguments are required!")
        new_authorization = {}
        for k, v in customer.__dict__.iteritems():
            if k in ('phone_number', 'email', 'ip', ):
                new_authorization[k] = v
        for k, v in credit_card.__dict__.iteritems():
            if k in self.credit_card_keys:
                new_authorization[self.credit_card_map[k]] = v
        for k, v in credit_card.address.__dict__.iteritems():
            key = 'address1' if k == 'street' else k
            new_authorization['billing_' + key] = v
        new_authorization['product_id'] = product.id
        new_authorization['campaign_id'] = campaign_id
        response = self.__request('authorize_payment', **new_authorization)
        return response, new_authorization
