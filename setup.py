#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/ejercicio_combinado.svg
        :target: https://pypi.python.org/pypi/ejercicio_combinado
.. image:: https://img.shields.io/travis/pabloaberbuj/ejercicio_combinado.svg
        :target: https://travis-ci.org/pabloaberbuj/ejercicio_combinado

Es un ejercicio combinado de cookicutter pylint y otros


Links:
---------
* `Github <https://github.com/pabloaberbuj/ejercicio_combinado>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Pablo Aberbuj",
    author_email='pabloaberbuj@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Es un ejercicio combinado de cookicutter pylint y otros",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='ejercicio_combinado',
    name='ejercicio_combinado',
    packages=find_packages(include=['ejercicio_combinado']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pabloaberbuj/ejercicio_combinado',
    version='0.1.2',
    zip_safe=False,
)
