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


def dist():
    with settings(warn_only=True):
        local("rm -r dist build")
    local("env3/bin/python setup.py sdist bdist_wheel --universal")
    local("env3/bin/twine upload -s -i DA4C68141DF3B0AA dist/*")

