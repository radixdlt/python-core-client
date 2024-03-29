"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.resource_type import ResourceType
from core_client.model.state_fungible_resource_manager import StateFungibleResourceManager
from core_client.model.state_non_fungible_resource_manager import StateNonFungibleResourceManager
from core_client.model.state_non_fungible_resource_manager_all_of import StateNonFungibleResourceManagerAllOf
from core_client.model.state_resource_manager import StateResourceManager
from core_client.model.substate import Substate
globals()['ResourceType'] = ResourceType
globals()['StateFungibleResourceManager'] = StateFungibleResourceManager
globals()['StateNonFungibleResourceManager'] = StateNonFungibleResourceManager
globals()['StateNonFungibleResourceManagerAllOf'] = StateNonFungibleResourceManagerAllOf
globals()['StateResourceManager'] = StateResourceManager
globals()['Substate'] = Substate
from core_client.model.state_non_fungible_resource_manager import StateNonFungibleResourceManager


class TestStateNonFungibleResourceManager(unittest.TestCase):
    """StateNonFungibleResourceManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStateNonFungibleResourceManager(self):
        """Test StateNonFungibleResourceManager"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StateNonFungibleResourceManager()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
