# -*- coding: utf-8 -*-

import os

from copy import copy
from unittest import TestCase

from ..test_data import test_order, test_credit_card_decline

from limelight.api import TransactionClient
from limelight.errors import TransactionDeclined


class TestNewOrder(TestCase):
    client = TransactionClient(host=os.environ['LIMELIGHT_HOST'],
                               username=os.environ['LIMELIGHT_USER'],
                               password=os.environ['LIMELIGHT_PASSWORD'])
    test_order = test_order

    def setUp(self):
        self.declined_order = copy(self.test_order)
        self.declined_order['credit_card_number'] = test_credit_card_decline['credit_card_number']

    def test_place_order(self):
        result = self.client.NewOrder(**self.test_order)
        self.assertEqual(result.error_found, 0)
        self.assertEqual(result.response_code, 100)
        self.assertIsInstance(result.customer_id, int)
        self.assertIsInstance(result.order_id, int)

    def test_place_declined_order(self):
        try:
            self.client.NewOrder(**self.declined_order)
        except TransactionDeclined as e:
            self.assertEqual(e.response.error_found, 1)
            self.assertEqual(e.response.response_code, 800)
            with self.assertRaises(TransactionDeclined):
                raise e
