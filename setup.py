from setuptools import find_packages, setup

VERSION = "4.0.0"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-messages.svg
    :target: https://pypi.python.org/pypi/pinax-messages/

==============
Pinax Messages
==============

.. image:: https://img.shields.io/pypi/v/pinax-messages.svg
    :target: https://pypi.python.org/pypi/pinax-messages/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-messages.svg
    :target: https://circleci.com/gh/pinax/pinax-messages
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-messages.svg
    :target: https://codecov.io/gh/pinax/pinax-messages
.. image:: https://img.shields.io/github/contributors/pinax/pinax-messages.svg
    :target: https://github.com/pinax/pinax-messages/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-messages.svg
    :target: https://github.com/pinax/pinax-messages/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-messages.svg
    :target: https://github.com/pinax/pinax-messages/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\

`pinax-messages` is a well tested, documented, and proven solution for any site that
that wants to support private user-to-user messaging.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+------+------+
| Django / Python | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 |
+=================+=====+=====+=====+=====+======+======+
|  2.2            |  *  |  *  |  *  |  *  |      |      |
+-----------------+-----+-----+-----+-----+------+------+
|  3.0            |  *  |  *  |  *  |  *  |      |      |
+-----------------+-----+-----+-----+-----+------+------+
|  3.1            |  *  |  *  |  *  |  *  |      |      |
+-----------------+-----+-----+-----+-----+------+------+
|  3.2            |  *  |  *  |  *  |  *  |  *   |      |
+-----------------+-----+-----+-----+-----+------+------+
|  4.0            |     |     |  *  |  *  |  *   |      |
+-----------------+-----+-----+-----+-----+------+------+
|  4.1            |     |     |  *  |  *  |  *   |  *   |
+-----------------+-----+-----+-----+-----+------+------+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a reusable private user messages application for Django",
    name="pinax-messages",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-messages/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "messages": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=2.2",
        "django-appconf>=1.0.2",
    ],
    tests_require=[
        "django-test-plus>=1.0.22",
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
