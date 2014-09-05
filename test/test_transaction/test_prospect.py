# -*- coding: utf-8 -*-

import os

from unittest import TestCase

from ..test_data import test_order, test_user

from limelight.api import TransactionClient


class TestProspect(TestCase):
    client = TransactionClient(host=os.environ['LIMELIGHT_HOST'],
                               username=os.environ['LIMELIGHT_USER'],
                               password=os.environ['LIMELIGHT_PASSWORD'])

    def test_new_prospect(self):
        new_prospect_result = self.client.NewProspect(campaign_id=test_order['campaign_id'],
                                                      ip_address=test_order['ip_address'],
                                                      **test_user)
        self.assertEqual(new_prospect_result.response_code, 100)
        result = self.client.NewOrderWithProspect(prospect_id=new_prospect_result.prospect_id,
                                                  **test_order)
        self.assertEqual(result.response_code, 100)