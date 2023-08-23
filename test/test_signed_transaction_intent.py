"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.signature_with_public_key import SignatureWithPublicKey
from core_client.model.signed_intent_hash import SignedIntentHash
from core_client.model.transaction_intent import TransactionIntent
globals()['SignatureWithPublicKey'] = SignatureWithPublicKey
globals()['SignedIntentHash'] = SignedIntentHash
globals()['TransactionIntent'] = TransactionIntent
from core_client.model.signed_transaction_intent import SignedTransactionIntent


class TestSignedTransactionIntent(unittest.TestCase):
    """SignedTransactionIntent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSignedTransactionIntent(self):
        """Test SignedTransactionIntent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SignedTransactionIntent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
