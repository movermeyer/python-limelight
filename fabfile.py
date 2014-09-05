#!/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *


def clean():
    local('find . -name "*.pyc" -delete')


def test():
    clean()
    local("env/bin/nosetests --with-coverage --cover-package=limelight")
    clean()
    local("env3/bin/nosetests --with-coverage --cover-package=limelight")

