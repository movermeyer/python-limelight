# -*- coding: utf-8 -*-

import urllib
import urllib2

from limelight.response import Response
from limelight.errors import ImproperlyConfigured
from limelight.utils import to_camel_case


class Transaction(object):
    """
    Exposes the Lime Light Transaction API as instance methods.
    """
    def __init__(self, username=None, password=None, endpoint=None):
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

    required_fields = (
        'customer', 'ip_address', 'product', 'upsell_count', 'upsell_products',
        'campaign_id', 'date', 'payment_method', 'shipping_address', 'quantity'
    )
    request_string = "{endpoint}/admin/transact.php?{query_string}".format

    # Map local tracking names to Lime Light names
    tracking_map = {
        'offer_id': 'C1',
        'affiliate_id': 'AFID',
        'affiliate_sub_id': 'SID',
        'affiliate_sub_id2': 'AID'
    }

    @property
    def tracking_keys(self):
        for k in self.tracking_map.iterkeys():
            yield k

    # Map local credit card field names to Lime Light names
    credit_card_map = {
        'first_name': 'billing_first_name',
        'last_name': 'billing_last_name',
        'type': 'credit_card_type',
        'number': 'credit_card_number',
        'expires': 'expiration_date',
        'ccv': 'CVV'
    }

    @property
    def credit_card_keys(self):
        for k in self.credit_card_map.iterkeys():
            yield k

    # Map local address field names to Lime Light names
    address_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'street': 'address1',
        'city': 'city',
        'state': 'state',
        '_state': 'state',
        'postal_code': 'zip',
        'country': 'country'
    }

    @property
    def address_keys(self):
        for k in self.address_map.iterkeys():
            yield k

    # Map local customer field name to Lime Light names
    customer_map = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'phone_number': 'phone',
        'email_address': 'email',
        'ip_address': 'ip_address'
    }

    @property
    def customer_keys(self):
        for k in self.customer_map.iterkeys():
            yield k

    def __request(self, method, convert_method=True, **kwargs):
        """
        This is what requests are made of!

        Converts python-style keys in kwargs into CamelCase keys and urlencodes the resulting dict.

        :param method: API method
        :param kwargs: Data being passed into the method
        :return: Lime Light response
        """
        kwargs['username'] = self.username
        kwargs['password'] = self.password
        kwargs['method'] = to_camel_case(method, initial_cap=True) if convert_method else method
        query_string = urllib.urlencode({to_camel_case(k): v for k, v in kwargs.iteritems()})
        request = self.request_string(endpoint=self.endpoint,
                                      query_string=query_string)
        return Response(urllib2.urlopen(request, timeout=7))

    def new_order(self, order):
        """
        Creates a new order in Lime Light.

        Takes a local order object, pulls out, and formats the information. All of that is sent to
        ```__request``` which makes the Lime Light method call.

        :param careers.models.Order order: Order information
        """
        new_order = {k: v for k, v in order.__dict__.iteritems() if k in self.required_fields}
        customer = new_order.pop('customer', order.customer)
        credit_card = new_order.pop('payment_method', order.payment_method)
        response, auth_data = self._authorize_payment(customer, credit_card,
                                                      product=order.product,
                                                      campaign_id=order.campaign_id)
        new_order.update(auth_data)
        address = new_order.pop('shipping_address', order.shipping_address)
        for k, v in address.__dict__.iteritems():
            if not k in ('id', ):
                new_order['shipping_' + self.address_map[k]] = v
        partial_ = customer.partial
        for k, v in partial_.__dict__.iteritems():
            if k in self.tracking_keys:
                new_order[self.tracking_map[k]] = v
        if hasattr(response, 'transaction_id'):
            new_order['transaction_id'] = response.transaction_id
        elif 'transaction_id' in partial_.__dict__ and partial_.__dict__['transaction_id'] is not None:
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
        new_authorization = {}
        for k, v in customer.__dict__.iteritems():
            if k in ('phone_number', 'email_address', 'ip_address', ):
                new_authorization[self.customer_map[k]] = v
        for k, v in credit_card.__dict__.iteritems():
            if k in self.credit_card_keys:
                if k == 'expires':
                    value = v.strftime("%m%y")
                else:
                    value = v
                new_authorization[self.credit_card_map[k]] = value
        for k, v in credit_card.billing_address.__dict__.iteritems():
            if not k in ('id', ):
                new_authorization['billing_' + self.address_map[k]] = v
        new_authorization['product_id'] = product.id
        new_authorization['campaign_id'] = campaign_id
        response = self.__request('authorize_payment', convert_method=False, **new_authorization)
        return response, new_authorization
