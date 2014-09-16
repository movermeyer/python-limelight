# -*- coding: utf-8 -*-

from voluptuous import Required, Optional

from ._schema import condition_for
from ..request import TransactionMethod


class NewProspect(TransactionMethod):
    __name__ = 'NewProspect'
    schema = {Optional('first_name'): condition_for['first_name'],
              Optional('last_name'): condition_for['last_name'],
              Optional('address1'): condition_for['address1'],
              Optional('address2'): condition_for['address2'],
              Optional('city'): condition_for['city'],
              Optional('state'): condition_for['state'],
              Optional('zip'): condition_for['zip'],
              Optional('country'): condition_for['country'],
              Optional('phone'): condition_for['phone'],
              Required('email'): condition_for['email'],
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
              Required('campaign_id'): condition_for['campaign_id'],
              Optional('notes'): condition_for['notes'], }