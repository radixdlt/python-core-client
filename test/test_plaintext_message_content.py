"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.binary_plaintext_message_content import BinaryPlaintextMessageContent
from core_client.model.plaintext_message_content_type import PlaintextMessageContentType
from core_client.model.string_plaintext_message_content import StringPlaintextMessageContent
globals()['BinaryPlaintextMessageContent'] = BinaryPlaintextMessageContent
globals()['PlaintextMessageContentType'] = PlaintextMessageContentType
globals()['StringPlaintextMessageContent'] = StringPlaintextMessageContent
from core_client.model.plaintext_message_content import PlaintextMessageContent


class TestPlaintextMessageContent(unittest.TestCase):
    """PlaintextMessageContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlaintextMessageContent(self):
        """Test PlaintextMessageContent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PlaintextMessageContent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()