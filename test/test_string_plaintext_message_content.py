"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.binary_plaintext_message_content import BinaryPlaintextMessageContent
from core_client.model.plaintext_message_content import PlaintextMessageContent
from core_client.model.plaintext_message_content_type import PlaintextMessageContentType
from core_client.model.string_plaintext_message_content import StringPlaintextMessageContent
from core_client.model.string_plaintext_message_content_all_of import StringPlaintextMessageContentAllOf
globals()['BinaryPlaintextMessageContent'] = BinaryPlaintextMessageContent
globals()['PlaintextMessageContent'] = PlaintextMessageContent
globals()['PlaintextMessageContentType'] = PlaintextMessageContentType
globals()['StringPlaintextMessageContent'] = StringPlaintextMessageContent
globals()['StringPlaintextMessageContentAllOf'] = StringPlaintextMessageContentAllOf
from core_client.model.string_plaintext_message_content import StringPlaintextMessageContent


class TestStringPlaintextMessageContent(unittest.TestCase):
    """StringPlaintextMessageContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStringPlaintextMessageContent(self):
        """Test StringPlaintextMessageContent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StringPlaintextMessageContent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()