# -*- coding: utf-8 -*-

from voluptuous import Schema, Required, Optional, All, Length

from ..method import TransactionMethod
from ..validation_functions import (email_address, valid_ip_address, valid_country_code,
                                    valid_credit_card_number, accepted_payment_type,
                                    datetime, decimal)


class AuthorizePayment(TransactionMethod):
    unconverted_field_labels = {'auth_amount', 'cascade_enabled', 'save_customer'}
    schema = Schema({Required('billing_first_name'): All(str, Length(min=1, max=64)),
                     Optional('billing_last_name'): All(str, Length(min=1, max=64)),
                     Required('billing_address1'): All(str, Length(min=1, max=64)),
                     Required('billing_address2'): All(str, Length(min=1, max=64)),
                     Required('billing_city'): All(str, Length(max=32)),
                     Required('billing_state'): All(str, Length(max=32)),
                     Required('billing_zip'): All(int, Length(max=10)),
                     Required('billing_country'): valid_country_code,
                     Required('phone'): All(int, Length(max=18)),
                     Required('email'): All(email_address, Length(max=96)),
                     Required('credit_card_type'): All(str, accepted_payment_type),
                     Required('credit_card_number'): All(valid_credit_card_number, Length(max=20)),
                     Required('expiration_date'): datetime,
                     Required('cvv'): All(int, Length(min=3, max=4)),
                     Required('ip_address'): All(valid_ip_address, Length(max=15)),
                     Required('product_id'): int,
                     Required('campaign_id'): int,
                     Optional('auth_amount'): decimal,
                     Optional('cascade_enabled'): bool,
                     Optional('save_customer'): bool, })