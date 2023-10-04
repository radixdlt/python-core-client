"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.access_rule_node import AccessRuleNode
from core_client.model.access_rule_node_type import AccessRuleNodeType
from core_client.model.all_of_access_rule_node import AllOfAccessRuleNode
from core_client.model.any_of_access_rule_node import AnyOfAccessRuleNode
from core_client.model.proof_access_rule_node import ProofAccessRuleNode
from core_client.model.proof_access_rule_node_all_of import ProofAccessRuleNodeAllOf
from core_client.model.proof_rule import ProofRule
globals()['AccessRuleNode'] = AccessRuleNode
globals()['AccessRuleNodeType'] = AccessRuleNodeType
globals()['AllOfAccessRuleNode'] = AllOfAccessRuleNode
globals()['AnyOfAccessRuleNode'] = AnyOfAccessRuleNode
globals()['ProofAccessRuleNode'] = ProofAccessRuleNode
globals()['ProofAccessRuleNodeAllOf'] = ProofAccessRuleNodeAllOf
globals()['ProofRule'] = ProofRule
from core_client.model.proof_access_rule_node import ProofAccessRuleNode


class TestProofAccessRuleNode(unittest.TestCase):
    """ProofAccessRuleNode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProofAccessRuleNode(self):
        """Test ProofAccessRuleNode"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProofAccessRuleNode()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()