##############################################################################
#
# Copyright (c) 2008-2011 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os
import platform

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
except IOError:
    README = CHANGES = ''

install_requires=[
    'pyramid>=1.0.2', # wsgiref paste entry point
    'zope.configuration>=3.8.0dev', # dict actions
    ]

if platform.system() == 'Java':
    tests_require = install_requires + ['WebTest', 'venusian']
else:
    tests_require= install_requires + ['Sphinx', 'docutils', 
                                       'repoze.sphinx.autointerface',
                                       'WebTest', 'venusian']

setup(name='pyramid_zcml',
      version='0.9.2',
      description='Zope Config Markup Language support for Pyramid',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: Repoze Public License",
        ],
      keywords='web wsgi pylons pyramid',
      author="Chris McDonough, Agendaless Consulting",
      author_email="pylons-devel@googlegroups.com",
      url="http://docs.pylonsproject.org",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = install_requires,
      tests_require = tests_require,
      test_suite="pyramid_zcml",
      entry_points = """
      [paste.paster_create_template]
      pyramid_starter_zcml=pyramid_zcml.scaffolds:StarterZCMLProjectTemplate
      [pyramid.scaffold]
      pyramid_starter_zcml=pyramid_zcml.scaffolds:StarterZCMLProjectTemplate
      """
      )

