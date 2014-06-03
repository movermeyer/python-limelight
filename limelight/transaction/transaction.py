# -*- coding: utf-8 -*-

import urllib

from limelight.response import Response
from limelight.errors import ImproperlyConfigured
from limelight.utils import to_camel_case
from limelight.transaction import maps


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
        query_string = urllib.urlencode({to_camel_case(k): v for k, v in kwargs.items()})
        request = self.request_string(endpoint=self.endpoint,
                                      query_string=query_string)
        return Response(request)

    def new_order(self, order):
        """
        Creates a new order in Lime Light.

        Takes a local order object, pulls out, and formats the information. All of that is sent to
        ```__request``` which makes the Lime Light method call.

        As we make progress on building out this library we'll need to loose our dependence on the
        bizopp Order model. Doing so will drastically simplify everything as we will no longer be
        munging data inside method calls. Instead we can expect a dict of a certain shape, validate
        what we can and throw an exception if things don't work out.

        :param careers.models.Order order: Order information
        """
        new_order = {k: v for k, v in order.__dict__.items() if k in self.required_fields}
        customer = new_order.pop('customer', order.customer)
        credit_card = new_order.pop('payment_method', order.payment_method)
        response, auth_data = self._authorize_payment(customer, credit_card,
                                                      ip_address=order.ip_address,
                                                      product=order.product,
                                                      campaign=order.campaign)
        new_order.update(auth_data)
        # Process shipping information
        address = new_order.pop('shipping_address', order.shipping_address)
        for k, v in address.__dict__.items():
            if not k in ('id', ):
                key, value = maps.address[k:v]
                new_order['shipping_' + key] = value
        # Process partial data
        partial_ = customer.partial
        if partial_:
            for k, v in partial_.__dict__.items():
                if k in maps.tracking.keys():
                    key, value = maps.tracking[k:v]
                    new_order[key] = value
        # Determine transaction ID
        if hasattr(response, 'transaction_id'):
            new_order['transaction_id'] = response.transaction_id
        elif partial_ and partial_.__dict__.get('transaction_id', None):
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
        :param upsell:
        :param partial:
        """
        new_order = {maps.tracking(k)[0]: maps.tracking[k:v][1]
                     for k, v in partial.__dict__.items() if k in maps.tracking.keys()}
        new_order['product_id'] = product
        new_order['previous_order_id'] = previous_order_id
        new_order['upsell'] = upsell
        return self.__request('new_order_card_on_file', **new_order)

    def new_order_with_prospect(self):
        """

        :return:
        """
        raise NotImplemented

    def _authorize_payment(self, customer, credit_card,
                           ip_address=None, product=None, campaign=None):
        """
        Authorize payment

        :param bizopp.models.User customer:
        :param careers.models.CreditCard credit_card:
        :param careers.models.Product product:
        :param int campaign:
        """
        new_authorization = {}
        for k, v in customer.__dict__.items():
            if k in ('first_name', 'last_name', 'phone_number', 'email_address', ):
                key, value = maps.customer[k:v]
                new_authorization[key] = value
        for k, v in credit_card.__dict__.items():
            if k in maps.credit_card.keys():
                key, value = maps.credit_card[k:v]
                new_authorization[key] = value
        for k, v in credit_card.billing_address.__dict__.items():
            if not k in ('id', ):
                key, value = maps.address[k:v]
                new_authorization['billing_' + key] = value
        new_authorization['ip_address'] = ip_address
        new_authorization['product_id'] = product.id
        new_authorization['campaign_id'] = campaign.id
        new_authorization['shipping_id'] = campaign.shipping_method.id
        response = self.__request('authorize_payment', convert_method=False, **new_authorization)
        return response, new_authorization
