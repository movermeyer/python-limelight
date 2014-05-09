# -*- coding: utf-8 -*-

from django.test import TestCase

from limelight.utils import (to_camel_case,
                             to_underscore,
                             _initial_cap)

from limelight.transaction.maps import Map


class TestUtils(TestCase):
    def setUp(self):
        self.underscore_name = "make_sure_this_is_enough"
        self.camel_name = "makeSureThisIsEnough"
        self.initial_cap_underscore_name = "Make_sure_this_is_enough"
        self.initial_cap_camel_name = "MakeSureThisIsEnough"

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case(self.underscore_name),
                         self.camel_name)
        self.assertEqual(to_camel_case(self.underscore_name, initial_cap=True),
                         self.initial_cap_camel_name)

    def test_to_underscore(self):
        self.assertEqual(to_underscore(self.camel_name), self.underscore_name)
        self.assertEqual(to_underscore(self.camel_name, initial_cap=True),
                         self.initial_cap_underscore_name)

    def test__initial_cap(self):
        self.assertEqual(_initial_cap(self.underscore_name), self.initial_cap_underscore_name)
        self.assertEqual(_initial_cap(self.camel_name), self.initial_cap_camel_name)


class TestMaps(TestCase):
    def setUp(self):
        self.a_to_b = Map(a='b')
        self.a_to_b_to_bb = Map(a=('b', lambda v: v + v))

    def test_a_to_b(self):
        """Map a to b"""
        self.assertEqual(self.a_to_b('a'), 'b')

    def test_a_to_bb(self):
        """Map a to b and convert b to bb"""
        self.assertEqual(self.a_to_b_to_bb('a', 'b')[0], 'b')
        self.assertEqual(self.a_to_b_to_bb('a', 'b')[1], 'bb')