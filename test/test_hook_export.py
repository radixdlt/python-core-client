"""
    Radix Core API - Babylon

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.object_hook import ObjectHook
from core_client.model.package_export import PackageExport
globals()['ObjectHook'] = ObjectHook
globals()['PackageExport'] = PackageExport
from core_client.model.hook_export import HookExport


class TestHookExport(unittest.TestCase):
    """HookExport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHookExport(self):
        """Test HookExport"""
        # FIXME: construct object with mandatory attributes with example values
        # model = HookExport()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
