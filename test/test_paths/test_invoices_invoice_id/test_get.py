# coding: utf-8

"""
    The Helcim API

    This API covers publicly accessible merchant actions

    The version of the OpenAPI document: 2.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import helcim_python_sdk
from helcim_python_sdk.paths.invoices_invoice_id import get
from helcim_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestInvoicesInvoiceId(ApiTestMixin, unittest.TestCase):
    """
    InvoicesInvoiceId unit test stubs
        Get invoice
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
