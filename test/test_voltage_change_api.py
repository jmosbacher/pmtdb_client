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
from api.voltage_change_api import VoltageChangeApi  # noqa: E501
from xepmts.rest import ApiException


class TestVoltageChangeApi(unittest.TestCase):
    """VoltageChangeApi unit test stubs"""

    def setUp(self):
        self.api = api.voltage_change_api.VoltageChangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_voltage_change_item(self):
        """Test case for delete_voltage_change_item

        Deletes a VoltageChange document  # noqa: E501
        """
        pass

    def test_get_voltage_change_item(self):
        """Test case for get_voltage_change_item

        Retrieves a VoltageChange document  # noqa: E501
        """
        pass

    def test_get_voltage_changes(self):
        """Test case for get_voltage_changes

        Retrieves one or more VoltageChanges  # noqa: E501
        """
        pass

    def test_post_voltage_changes(self):
        """Test case for post_voltage_changes

        Stores one or more VoltageChanges.  # noqa: E501
        """
        pass

    def test_put_voltage_change_item(self):
        """Test case for put_voltage_change_item

        Replaces a VoltageChange document  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
