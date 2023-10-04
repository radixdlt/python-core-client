"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.access_rule import AccessRule
from core_client.model.access_rule_node import AccessRuleNode
from core_client.model.access_rule_type import AccessRuleType
from core_client.model.allow_all_access_rule import AllowAllAccessRule
from core_client.model.deny_all_access_rule import DenyAllAccessRule
from core_client.model.protected_access_rule import ProtectedAccessRule
from core_client.model.protected_access_rule_all_of import ProtectedAccessRuleAllOf
globals()['AccessRule'] = AccessRule
globals()['AccessRuleNode'] = AccessRuleNode
globals()['AccessRuleType'] = AccessRuleType
globals()['AllowAllAccessRule'] = AllowAllAccessRule
globals()['DenyAllAccessRule'] = DenyAllAccessRule
globals()['ProtectedAccessRule'] = ProtectedAccessRule
globals()['ProtectedAccessRuleAllOf'] = ProtectedAccessRuleAllOf
from core_client.model.protected_access_rule import ProtectedAccessRule


class TestProtectedAccessRule(unittest.TestCase):
    """ProtectedAccessRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProtectedAccessRule(self):
        """Test ProtectedAccessRule"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProtectedAccessRule()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()