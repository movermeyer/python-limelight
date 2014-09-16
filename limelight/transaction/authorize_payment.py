# -*- coding: utf-8 -*-

from voluptuous import Required, Optional

from ._schema import condition_for
from ..request import TransactionMethod


class AuthorizePayment(TransactionMethod):
    __name__ = 'authorize_payment'
    schema = {Required('billing_first_name'): condition_for['billing_first_name'],
              Optional('billing_last_name'): condition_for['billing_last_name'],
              Required('billing_address1'): condition_for['billing_address1'],
              Required('billing_address2'): condition_for['billing_address2'],
              Required('billing_city'): condition_for['billing_city'],
              Required('billing_state'): condition_for['billing_state'],
              Required('billing_zip'): condition_for['billing_zip'],
              Required('billing_country'): condition_for['billing_country'],
              Required('phone'): condition_for['phone'],
              Required('email'): condition_for['email'],
              Required('credit_card_type'): condition_for['credit_card_type'],
              Required('credit_card_number'): condition_for['credit_card_number'],
              Required('expiration_date'): condition_for['expiration_date'],
              Required('cvv'): condition_for['cvv'],
              Required('ip_address'): condition_for['ip_address'],
              Required('product_id'): condition_for['product_id'],
              Required('campaign_id'): condition_for['campaign_id'],
              Optional('auth_amount'): condition_for['auth_amount'],
              Optional('cascade_enabled'): condition_for['cascade_enabled'],
              Optional('save_customer'): condition_for['save_customer'], }