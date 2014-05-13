# -*- coding: utf-8 -*-
"""
Lime Light API Exceptions and Errors
"""


class LimeLightException(Exception): pass


class ImproperlyConfigured(LimeLightException): pass


class RequestError(LimeLightException): pass


class NoPreviousOrder(LimeLightException): pass


class TransactionDeclined(LimeLightException): pass