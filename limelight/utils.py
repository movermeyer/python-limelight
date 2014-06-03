# -*- coding: utf-8 -*-

import re

CAMEL_RE = re.compile(r'([A-Z])')
UNDER_RE = re.compile(r'_([a-z])')
NUM_RE = re.compile(r'^[0-9]+$')
FLOAT_RE = re.compile(r'^[0-9]*?\.[0-9]+$')


def _initial_cap(name):
    return name[0].upper() + name[1:]


def to_underscore(name, initial_cap=False):
    """Convert identifiers from camelCase to underscore_style"""
    underscore_name = CAMEL_RE.sub(lambda s: "_" + s.group(1).lower(), name)
    if initial_cap:
        underscore_name = _initial_cap(underscore_name)
    return underscore_name


def to_camel_case(name, initial_cap=False):
    """Convert identifiers from underscore_style to camelCase"""
    camel_case_name = UNDER_RE.sub(lambda s: s.group(1).upper(), name)
    if initial_cap:
        camel_case_name = _initial_cap(camel_case_name)
    return camel_case_name


def to_python(var):
    """
    Converts strings that are really numbers to ints or floats

    May be more generic in the future
    :param var:
    """
    var = var[0] if isinstance(var, list) else var
    if not isinstance(var, str):
        return var
    elif NUM_RE.match(var):
        return int(var)
    elif FLOAT_RE.match(var):
        return float(var)
    else:
        return var

