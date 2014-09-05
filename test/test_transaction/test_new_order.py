# -*- coding: utf-8 -*-

import os

from unittest import TestCase

from ..test_data import test_order

from limelight.api import TransactionClient


class TestNewOrder(TestCase):
    client = TransactionClient(host=os.environ['LIMELIGHT_HOST'],
                               username=os.environ['LIMELIGHT_USER'],
                               password=os.environ['LIMELIGHT_PASSWORD'])

    def test_place_order(self):
        result = self.client.NewOrder(**test_order)
        self.assertEqual(result.response_code, 100)
