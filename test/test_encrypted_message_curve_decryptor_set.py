"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.encrypted_message_decryptor import EncryptedMessageDecryptor
from core_client.model.public_key import PublicKey
globals()['EncryptedMessageDecryptor'] = EncryptedMessageDecryptor
globals()['PublicKey'] = PublicKey
from core_client.model.encrypted_message_curve_decryptor_set import EncryptedMessageCurveDecryptorSet


class TestEncryptedMessageCurveDecryptorSet(unittest.TestCase):
    """EncryptedMessageCurveDecryptorSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEncryptedMessageCurveDecryptorSet(self):
        """Test EncryptedMessageCurveDecryptorSet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EncryptedMessageCurveDecryptorSet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
