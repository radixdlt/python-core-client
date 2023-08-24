"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.method_accessibility import MethodAccessibility
from core_client.model.method_accessibility_type import MethodAccessibilityType
from core_client.model.outer_object_only_method_accessibility import OuterObjectOnlyMethodAccessibility
from core_client.model.own_package_only_method_accessibility import OwnPackageOnlyMethodAccessibility
from core_client.model.public_method_accessibility import PublicMethodAccessibility
from core_client.model.role_protected_method_accessibility import RoleProtectedMethodAccessibility
globals()['MethodAccessibility'] = MethodAccessibility
globals()['MethodAccessibilityType'] = MethodAccessibilityType
globals()['OuterObjectOnlyMethodAccessibility'] = OuterObjectOnlyMethodAccessibility
globals()['OwnPackageOnlyMethodAccessibility'] = OwnPackageOnlyMethodAccessibility
globals()['PublicMethodAccessibility'] = PublicMethodAccessibility
globals()['RoleProtectedMethodAccessibility'] = RoleProtectedMethodAccessibility
from core_client.model.public_method_accessibility import PublicMethodAccessibility


class TestPublicMethodAccessibility(unittest.TestCase):
    """PublicMethodAccessibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPublicMethodAccessibility(self):
        """Test PublicMethodAccessibility"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PublicMethodAccessibility()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
