"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.event_emitter_identifier_type import EventEmitterIdentifierType
from core_client.model.function_event_emitter_identifier import FunctionEventEmitterIdentifier
from core_client.model.method_event_emitter_identifier import MethodEventEmitterIdentifier
globals()['EventEmitterIdentifierType'] = EventEmitterIdentifierType
globals()['FunctionEventEmitterIdentifier'] = FunctionEventEmitterIdentifier
globals()['MethodEventEmitterIdentifier'] = MethodEventEmitterIdentifier
from core_client.model.event_emitter_identifier import EventEmitterIdentifier


class TestEventEmitterIdentifier(unittest.TestCase):
    """EventEmitterIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventEmitterIdentifier(self):
        """Test EventEmitterIdentifier"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventEmitterIdentifier()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()