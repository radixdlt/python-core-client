"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.key_value_store_type_info_details import KeyValueStoreTypeInfoDetails
from core_client.model.object_type_info_details import ObjectTypeInfoDetails
from core_client.model.type_info_type import TypeInfoType
globals()['KeyValueStoreTypeInfoDetails'] = KeyValueStoreTypeInfoDetails
globals()['ObjectTypeInfoDetails'] = ObjectTypeInfoDetails
globals()['TypeInfoType'] = TypeInfoType
from core_client.model.type_info_details import TypeInfoDetails


class TestTypeInfoDetails(unittest.TestCase):
    """TypeInfoDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTypeInfoDetails(self):
        """Test TypeInfoDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TypeInfoDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
