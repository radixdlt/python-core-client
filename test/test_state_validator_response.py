"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.state_component_descendent_node import StateComponentDescendentNode
from core_client.model.substate import Substate
from core_client.model.vault_balance import VaultBalance
globals()['StateComponentDescendentNode'] = StateComponentDescendentNode
globals()['Substate'] = Substate
globals()['VaultBalance'] = VaultBalance
from core_client.model.state_validator_response import StateValidatorResponse


class TestStateValidatorResponse(unittest.TestCase):
    """StateValidatorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStateValidatorResponse(self):
        """Test StateValidatorResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StateValidatorResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()