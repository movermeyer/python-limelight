# -*- coding: utf-8 -*-
"""
Conditions for Transaction API field values

TODO: Supply useful error messages
"""

import six

from voluptuous import All, Length, Any

from .. import validate

condition_for = {'first_name': All(six.u, Length(max=64)),
                 'last_name': All(six.u, Length(max=64)),
                 'address1': All(six.u, Length(max=64)),
                 'address2': All(six.u, Length(max=64)),
                 'city': All(six.u, Length(max=32)),
                 'state': All(six.u, Length(max=32)),
                 'zip': All(six.u, Length(max=10)),
                 'country': All(six.u, validate.country_code, Length(2)),
                 'phone': All(six.u, Length(max=18)),
                 'email': All(six.u, validate.email_address, Length(max=96)),
                 'credit_card_type': All(six.u, validate.accepted_payment_type),
                 'credit_card_number': All(six.u, validate.credit_card_number, Length(max=20)),
                 'expiration_date': All(validate.expiration_date, Length(4)),
                 'cvv': All(six.u, Length(min=3, max=4)),
                 'tran_type': six.u('Sale'),
                 'ip_address': All(six.u, validate.ip_address, Length(max=15)),
                 'AFID': All(six.u, Length(max=255)),
                 'SID': All(six.u, Length(max=255)),
                 'AFFID': All(six.u, Length(max=255)),
                 'C1': All(six.u, Length(max=255)),
                 'C2': All(six.u, Length(max=255)),
                 'C3': All(six.u, Length(max=255)),
                 'AID': All(six.u, Length(max=255)),
                 'OPT': All(six.u, Length(max=255)),
                 'click_id': All(six.u, Length(max=255)),
                 'product_id': int,
                 'campaign_id': int,
                 'shipping_id': int,
                 'upsell_count': All(bool, validate.bool_to_one_or_zero),
                 'upsell_product_ids': [int],
                 'billing_same_as_shipping': All(bool, validate.bool_to_yes_or_no),
                 'notes': All(six.u, Length(max=512)),
                 'preserve_force_gateway': All(bool, validate.bool_to_one_or_zero),
                 'created_by': All(six.u, Length(max=100)),
                 'thm_session_id': All(six.u, Length(max=255)),
                 'total_installments': int,
                 'alt_pay_token': All(six.u, Length(max=20)),
                 'alt_pay_payer_id': All(six.u, Length(max=20)),
                 'secret_ssn': All(int, Length(max=4)),
                 'force_subscription_cycle': All(bool, validate.bool_to_one_or_zero),
                 'recurring_days': int,
                 'subscription_week': Any(1, 2, 3, 4, 5),
                 'subscription_day': Any(1, 2, 3, 4, 5, 6, 7),
                 'master_order_id': int,
                 'promo_code': All(six.u, Length(max=100)),
                 'temp_customer_id': All(six.u, Length(max=32)),
                 # authorize_payment
                 'auth_amount': validate.decimal,
                 'cascade_enabled': All(bool, validate.bool_to_one_or_zero),
                 'save_customer': All(bool, validate.bool_to_one_or_zero),
                 # NewOrderWithProspect
                 'prospect_id': int,
                 # three_d_redirect
                 'order_id': int, }

# Duplicate conditions
condition_for.update({'shipping_address1': condition_for['address1'],
                      'shipping_address2': condition_for['address2'],
                      'shipping_city': condition_for['city'],
                      'shipping_state': condition_for['state'],
                      'shipping_zip': condition_for['zip'],
                      'shipping_country': condition_for['country'],
                      'billing_first_name': condition_for['first_name'],
                      'billing_last_name': condition_for['last_name'],
                      'billing_address1': condition_for['address1'],
                      'billing_address2': condition_for['address2'],
                      'billing_city': condition_for['city'],
                      'billing_state': condition_for['state'],
                      'billing_zip': condition_for['zip'],
                      'billing_country': condition_for['country'], })