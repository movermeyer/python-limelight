#!/usr/env python
# -*- coding: utf-8 -*-

from setuptools import setup

from limelight import (__version__ as version,
                       __license__ as license,
                       __author__ as author,
                       __email__ as author_email, )

setup(
    name="python-limelight",
    version=version,
    description="A pythonic Lime Light API wrapper",
    long_description=open("README.txt", 'rb').read().decode('utf-8'),
    url="https://bitbucket.org/zulumarketing/python-limelight",
    license=license,
    author=author,
    author_email=author_email,
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
