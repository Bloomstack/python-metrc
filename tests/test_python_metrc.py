#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_metrc` package."""

import pytest

from python_metrc import METRC

HOST = 'localhost'
PORT = 8000
BASE_URL = 'http://{}:{}'.format(HOST, PORT)
PATH = '/resource/v2/endpoint/extension'
URL = BASE_URL + PATH


@pytest.fixture(scope="module")
def metrc():
    return METRC(BASE_URL, vendor_key="", user_key="", license_number="", api_version="v2")


def test_urls(metrc):
    combs = [
        metrc.resource.endpoint.extension,
        metrc('resource', 'endpoint').extension,
        metrc('resource', 'endpoint', 'extension'),
        metrc('resource')('endpoint')('extension'),
        metrc.resource('endpoint', 'extension'),
        metrc('resource',).endpoint.extension
    ]

    for comb in combs:
        assert str(comb) == URL
