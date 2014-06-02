# -*- coding: utf-8 -*-

from unittest import TestCase

from limelight.types import Map


class TestMaps(TestCase):
    def setUp(self):
        self.a_to_b = Map(a='b')
        self.a_to_b_to_bb = Map(a=('b', lambda v: v + v))

    def test_a_to_b(self):
        """Map a to b"""
        self.assertEqual(self.a_to_b['a'], 'b')

    def test_a_to_bb(self):
        """Map a to b and convert b to bb"""
        self.assertEqual(self.a_to_b_to_bb['a':'b'], ('b', 'bb'))
