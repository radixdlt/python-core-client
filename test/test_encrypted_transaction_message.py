"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.encrypted_message_curve_decryptor_set import EncryptedMessageCurveDecryptorSet
from core_client.model.encrypted_transaction_message import EncryptedTransactionMessage
from core_client.model.encrypted_transaction_message_all_of import EncryptedTransactionMessageAllOf
from core_client.model.plaintext_transaction_message import PlaintextTransactionMessage
from core_client.model.transaction_message import TransactionMessage
from core_client.model.transaction_message_type import TransactionMessageType
globals()['EncryptedMessageCurveDecryptorSet'] = EncryptedMessageCurveDecryptorSet
globals()['EncryptedTransactionMessage'] = EncryptedTransactionMessage
globals()['EncryptedTransactionMessageAllOf'] = EncryptedTransactionMessageAllOf
globals()['PlaintextTransactionMessage'] = PlaintextTransactionMessage
globals()['TransactionMessage'] = TransactionMessage
globals()['TransactionMessageType'] = TransactionMessageType
from core_client.model.encrypted_transaction_message import EncryptedTransactionMessage


class TestEncryptedTransactionMessage(unittest.TestCase):
    """EncryptedTransactionMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEncryptedTransactionMessage(self):
        """Test EncryptedTransactionMessage"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EncryptedTransactionMessage()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
