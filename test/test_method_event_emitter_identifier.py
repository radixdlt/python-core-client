"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.entity_reference import EntityReference
from core_client.model.event_emitter_identifier import EventEmitterIdentifier
from core_client.model.event_emitter_identifier_type import EventEmitterIdentifierType
from core_client.model.function_event_emitter_identifier import FunctionEventEmitterIdentifier
from core_client.model.method_event_emitter_identifier import MethodEventEmitterIdentifier
from core_client.model.method_event_emitter_identifier_all_of import MethodEventEmitterIdentifierAllOf
from core_client.model.object_module_id import ObjectModuleId
globals()['EntityReference'] = EntityReference
globals()['EventEmitterIdentifier'] = EventEmitterIdentifier
globals()['EventEmitterIdentifierType'] = EventEmitterIdentifierType
globals()['FunctionEventEmitterIdentifier'] = FunctionEventEmitterIdentifier
globals()['MethodEventEmitterIdentifier'] = MethodEventEmitterIdentifier
globals()['MethodEventEmitterIdentifierAllOf'] = MethodEventEmitterIdentifierAllOf
globals()['ObjectModuleId'] = ObjectModuleId
from core_client.model.method_event_emitter_identifier import MethodEventEmitterIdentifier


class TestMethodEventEmitterIdentifier(unittest.TestCase):
    """MethodEventEmitterIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMethodEventEmitterIdentifier(self):
        """Test MethodEventEmitterIdentifier"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MethodEventEmitterIdentifier()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
