# -*- coding: utf-8 -*-

from voluptuous import Required, Optional

from._schema import condition_for
from ..request import TransactionMethod


class NewOrderCardOnFile(TransactionMethod):
    __name__ = 'NewOrderCardOnFile'
    schema = {Required('tran_type'): condition_for['tran_type'],
              Optional('click_id'): condition_for['click_id'],
              Required('product_id'): condition_for['product_id'],
              Required('campaign_id'): condition_for['campaign_id'],
              Required('shipping_id'): condition_for['shipping_id'],
              Required('upsell_count'): condition_for['upsell_count'],
              Optional('upsell_product_ids'): condition_for['upsell_product_ids'],
              Optional('notes'): condition_for['notes'],
              Optional('preserve_force_gateway'): condition_for['preserve_force_gateway'],
              Optional('created_by'): condition_for['created_by'],
              Optional('force_subscription_cycle'): condition_for['force_subscription_cycle'],
              Optional('recurring_days'): condition_for['recurring_days'],
              Optional('subscription_week'): condition_for['subscription_week'],
              Optional('subscription_day'): condition_for['subscription_day'],
              Optional('master_order_id'): condition_for['master_order_id'],
              Optional('promo_code'): condition_for['promo_code'],
              Optional('temp_customer_id'): condition_for['temp_customer_id'], }