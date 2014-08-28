#!/usr/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='python-limelight',
      version='1.dev1',
      description='A pythonic Lime Light API wrapper',
      long_description=open('README.rst', 'rb').read().decode('utf-8'),
      url='https://github.com/heropunch/python-limelight',
      license='MIT',
      author='Carlos Killpack',
      author_email='carlos.killpack@rocketmail.com',
      packages=['limelight', ],
      classifiers=['Environment :: Web Environment',
                   'Topic :: Internet',
                   'Topic :: Office/Business',
                   'Topic :: Office/Business :: Financial',
                   'Topic :: Office/Business :: Financial :: Accounting',
                   'Topic :: Office/Business :: Financial :: Investment',
                   'Topic :: Office/Business :: Financial :: Point-Of-Sale',
                   'License :: OSI Approved',
                   'License :: OSI Approved :: MIT', ],
      install_requires=['decorator',
                        'validate_email',
                        'ipaddress',
                        'voluptuous',
                        'pycountry',
                        'six', ])
