# -*- coding: utf-8 -*-

from voluptuous import Required, Optional

from ._schema import condition_for
from ..request import TransactionMethod


class NewOrder(TransactionMethod):
    __name__ = 'NewOrder'
    schema = {Required('first_name'): condition_for['first_name'],
              Required('last_name'): condition_for['last_name'],
              Required('shipping_address1'): condition_for['shipping_address1'],
              Optional('shipping_address2'): condition_for['shipping_address2'],
              Required('shipping_city'): condition_for['shipping_city'],
              Required('shipping_state'): condition_for['shipping_state'],
              Required('shipping_zip'): condition_for['shipping_zip'],
              Required('shipping_country'): condition_for['shipping_country'],
              Optional('billing_first_name'): condition_for['billing_first_name'],
              Optional('billing_last_name'): condition_for['billing_last_name'],
              Optional('billing_address1'): condition_for['billing_address1'],
              Optional('billing_address2'): condition_for['billing_address2'],
              Optional('billing_city'): condition_for['billing_city'],
              Optional('billing_state'): condition_for['billing_state'],
              Optional('billing_zip'): condition_for['billing_zip'],
              Optional('billing_country'): condition_for['billing_country'],
              Required('phone'): condition_for['phone'],
              Required('email'): condition_for['email'],
              Required('credit_card_type'): condition_for['credit_card_type'],
              Required('credit_card_number'): condition_for['credit_card_number'],
              Required('expiration_date'): condition_for['expiration_date'],
              Required('cvv'): condition_for['cvv'],
              Required('tran_type'): condition_for['tran_type'],
              Required('ip_address'): condition_for['ip_address'],
              Optional('AFID'): condition_for['AFID'],
              Optional('SID'): condition_for['SID'],
              Optional('AFFID'): condition_for['AFFID'],
              Optional('C1'): condition_for['C1'],
              Optional('C2'): condition_for['C2'],
              Optional('C3'): condition_for['C3'],
              Optional('AID'): condition_for['AID'],
              Optional('OPT'): condition_for['OPT'],
              Optional('click_id'): condition_for['click_id'],
              Required('product_id'): condition_for['product_id'],
              Required('campaign_id'): condition_for['campaign_id'],
              Required('shipping_id'): condition_for['shipping_id'],
              Required('upsell_count'): condition_for['upsell_count'],
              Optional('upsell_product_ids'): condition_for['upsell_product_ids'],
              Optional('billing_same_as_shipping'): condition_for['billing_same_as_shipping'],
              Optional('notes'): condition_for['notes'],
              Optional('preserve_force_gateway'): condition_for['preserve_force_gateway'],
              Optional('created_by'): condition_for['created_by'],
              Optional('thm_session_id'): condition_for['thm_session_id'],
              Optional('total_installments'): condition_for['total_installments'],
              Optional('alt_pay_token'): condition_for['alt_pay_token'],
              Optional('alt_pay_payer_id'): condition_for['alt_pay_payer_id'],
              Optional('secret_ssn'): condition_for['secret_ssn'],
              Optional('force_subscription_cycle'): condition_for['force_subscription_cycle'],
              Optional('recurring_days'): condition_for['recurring_days'],
              Optional('subscription_week'): condition_for['subscription_week'],
              Optional('subscription_day'): condition_for['subscription_day'],
              Optional('master_order_id'): condition_for['master_order_id'],
              Optional('promo_code'): condition_for['promo_code'],
              Optional('temp_customer_id'): condition_for['temp_customer_id'], }