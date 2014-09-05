#!/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *


def test():
    local("nosetests --with-coverage --cover-package=limelight")

