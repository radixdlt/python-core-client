"""
    Radix Core API - Babylon

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.blueprint_payload_def_type import BlueprintPayloadDefType
from core_client.model.generic_blueprint_payload_def import GenericBlueprintPayloadDef
from core_client.model.static_blueprint_payload_def import StaticBlueprintPayloadDef
globals()['BlueprintPayloadDefType'] = BlueprintPayloadDefType
globals()['GenericBlueprintPayloadDef'] = GenericBlueprintPayloadDef
globals()['StaticBlueprintPayloadDef'] = StaticBlueprintPayloadDef
from core_client.model.blueprint_payload_def import BlueprintPayloadDef


class TestBlueprintPayloadDef(unittest.TestCase):
    """BlueprintPayloadDef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBlueprintPayloadDef(self):
        """Test BlueprintPayloadDef"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BlueprintPayloadDef()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
