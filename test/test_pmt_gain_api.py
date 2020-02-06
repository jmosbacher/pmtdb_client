# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import xepmts
from api.pmt_gain_api import PmtGainApi  # noqa: E501
from xepmts.rest import ApiException


class TestPmtGainApi(unittest.TestCase):
    """PmtGainApi unit test stubs"""

    def setUp(self):
        self.api = api.pmt_gain_api.PmtGainApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deletepmt_gain_item(self):
        """Test case for deletepmt_gain_item

        Deletes a pmt_gain document  # noqa: E501
        """
        pass

    def test_deletepmt_gains(self):
        """Test case for deletepmt_gains

        Deletes all pmt_gains  # noqa: E501
        """
        pass

    def test_getpmt_gain_item(self):
        """Test case for getpmt_gain_item

        Retrieves a pmt_gain document  # noqa: E501
        """
        pass

    def test_getpmt_gains(self):
        """Test case for getpmt_gains

        Retrieves one or more pmt_gains  # noqa: E501
        """
        pass

    def test_postpmt_gains(self):
        """Test case for postpmt_gains

        Stores one or more pmt_gains.  # noqa: E501
        """
        pass

    def test_putpmt_gain_item(self):
        """Test case for putpmt_gain_item

        Replaces a pmt_gain document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
