"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.created_substate import CreatedSubstate
from core_client.model.deleted_substate import DeletedSubstate
from core_client.model.entity_reference import EntityReference
from core_client.model.updated_substate import UpdatedSubstate
globals()['CreatedSubstate'] = CreatedSubstate
globals()['DeletedSubstate'] = DeletedSubstate
globals()['EntityReference'] = EntityReference
globals()['UpdatedSubstate'] = UpdatedSubstate
from core_client.model.state_updates import StateUpdates


class TestStateUpdates(unittest.TestCase):
    """StateUpdates unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStateUpdates(self):
        """Test StateUpdates"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StateUpdates()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()