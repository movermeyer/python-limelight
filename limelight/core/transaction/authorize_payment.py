# -*- coding: utf-8 -*-

from ..method import TransactionMethod
from .. import validations


class AuthorizePayment(TransactionMethod):
    required_fields = {'billing_first_name', 'billing_last_name', 'billing_address1',
                       'billing_address2', 'billing_city', 'billing_state', 'billing_zip',
                       'phone', 'email', 'credit_card_type', 'credit_card_number', 'cvv',
                       'ip_address', 'product_id', 'campaign_id'}
    unconverted_field_labels = {'auth_amount', 'cascade_enabled', 'save_customer'}
    validate = {'billing_first_name': validations.is_alphanumeric(64),
                'billing_last_name': validations.is_alphanumeric(64),
                'billing_address1': validations.is_alphanumeric(64),
                'billing_address2': validations.is_alphanumeric(64),
                'billing_city': validations.is_alphanumeric(32),
                'billing_state': validations.is_alphanumeric(32),
                'billing_zip': validations.is_numeric(10),
                'billing_country': validations.is_valid_country_code,
                'phone': validations.is_numeric(18),
                'email': validations.is_email_address(96),
                'credit_card_type': validations.is_accepted_payment_type,
                'credit_card_number': validations.is_valid_credit_card_number(20),
                'cvv': validations.is_numeric(4),
                'ip_address': validations.is_valid_ip_address(15),
                'product_id': validations.is_numeric(),
                'campaign_id': validations.is_numeric(),
                'auth_amount': validations.is_decimal,
                'cascade_enabled': validations.is_boolean,
                'save_customer': validations.is_boolean, }