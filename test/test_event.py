"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.event_type_identifier import EventTypeIdentifier
from core_client.model.sbor_data import SborData
globals()['EventTypeIdentifier'] = EventTypeIdentifier
globals()['SborData'] = SborData
from core_client.model.event import Event


class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEvent(self):
        """Test Event"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Event()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
