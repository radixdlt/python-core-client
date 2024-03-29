"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.encrypted_transaction_message import EncryptedTransactionMessage
from core_client.model.plaintext_message_content import PlaintextMessageContent
from core_client.model.plaintext_transaction_message import PlaintextTransactionMessage
from core_client.model.plaintext_transaction_message_all_of import PlaintextTransactionMessageAllOf
from core_client.model.transaction_message import TransactionMessage
from core_client.model.transaction_message_type import TransactionMessageType
globals()['EncryptedTransactionMessage'] = EncryptedTransactionMessage
globals()['PlaintextMessageContent'] = PlaintextMessageContent
globals()['PlaintextTransactionMessage'] = PlaintextTransactionMessage
globals()['PlaintextTransactionMessageAllOf'] = PlaintextTransactionMessageAllOf
globals()['TransactionMessage'] = TransactionMessage
globals()['TransactionMessageType'] = TransactionMessageType
from core_client.model.plaintext_transaction_message import PlaintextTransactionMessage


class TestPlaintextTransactionMessage(unittest.TestCase):
    """PlaintextTransactionMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlaintextTransactionMessage(self):
        """Test PlaintextTransactionMessage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PlaintextTransactionMessage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
