# -*- coding: utf-8 -*-

import re

from validate_email import validate_email

import decorator

import ipaddress

import pycountry

__all__ = ['is_numeric', 'is_alphanumeric', 'is_accepted_payment_type', 'is_email_address',
           'is_boolean', 'is_decimal', 'is_valid_country_code', 'is_valid_credit_card_number',
           'is_valid_ip_address', ]

ALPHANUMERIC_RE = re.compile(r'^(?:[\w ](?!_))+$')
NUMERIC_RE = re.compile(r'^[0-9]+$')
DECIMAL_RE = re.compile(r'^\d+\.\d{2}$')
CREDIT_CARD_RE = re.compile(r'''^(?:4[0-9]{12}(?:[0-9]{3})?
                                   |5[1-5][0-9]{14}
                                   |6(?:011|5[0-9][0-9])[0-9]{12}
                                   |3[47][0-9]{13}
                                   |3(?:0[0-5]|[68][0-9])[0-9]{11}
                                   |(?:2131|1800|35\\d{3})\d{11})$''',
                            re.X)

@decorator.decorator
def check_length():
    pass


def is_alphanumeric(length=None):
    """
    Verifies that the given value of a specified length contains only letters and numbers.
    """
    def _is_alphanumeric(string, alphanumeric_re=ALPHANUMERIC_RE):
        if len(string) == length or length is None:
            return bool(re.match(alphanumeric_re, string))
        else:
            return False
    return _is_alphanumeric


def is_numeric(length=None):
    """
    Verifies that a given value of a specified length contains only numbers.
    """
    def _is_numeric(number, numeric_re=NUMERIC_RE):
        if len(str(number)) == length or length is None:
            return bool(re.match(numeric_re, str(number)))
        else:
            return False
    return _is_numeric


def is_email_address(length=None):
    """
    Verifies that a given value of a specified length is a valid RFC 2822 email address
    """
    def _is_email_address(email_address):
        if len(email_address) == length or length is None:
            return validate_email(email_address)
        else:
            return False
    return _is_email_address


def is_accepted_payment_type(credit_card_type):
    """
    Verifies that the given payment type is supported by Lime Light
    """
    return bool(credit_card_type in {'amex', 'visa', 'master', 'discover', 'checking', 'offline',
                                     'solo', 'maestro', 'switch', 'boleto', 'paypal', 'diners',
                                     'hipercard', 'aura', 'eft_germany', 'giro'})


def is_valid_credit_card_number(length=None):
    """
    Verifies that the given credit card number is valid.
    """
    def _is_valid_credit_card_number(number, credit_card_re=CREDIT_CARD_RE):
        if len(number) == length or length is None:
            return bool(re.match(credit_card_re, number))
        else:
            return False
    return _is_valid_credit_card_number


def is_valid_ip_address(length=None):
    """
    Verifies that the given IP address is valid.
    """
    def _is_valid_ip_address(ip_address):
        if len(ip_address) == length or length is None:
            return isinstance(ipaddress.ip_address(ip_address), (ipaddress.IPv4Address,
                                                                 ipaddress.IPv6Address))
        else:
            return False
    return _is_valid_ip_address


def is_decimal(number, decimal_re=DECIMAL_RE):
    return bool(re.match(decimal_re, number))


def is_boolean(value):
    return isinstance(value, bool)


def is_valid_country_code(country_code):
    try:
        return bool(pycountry.countries.get(alpha2=country_code))
    except KeyError:
        return False