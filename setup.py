#!/usr/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="python-limelight",
    version="0.0.1.dev1",
    description="A pythonic Lime Light API wrapper",
    long_description=open("README.rst", 'rb').read().decode('utf-8'),
    url="https://bitbucket.org/zulumarketing/python-limelight",
    license="MIT",
    author="Carlos Killpack",
    author_email="carlos@zulumarketing.com",
    packages=[
        "limelight",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Topic :: Internet",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        "us",
    ]
)
