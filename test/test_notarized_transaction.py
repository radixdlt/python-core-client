"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.notarized_transaction_hash import NotarizedTransactionHash
from core_client.model.signature import Signature
from core_client.model.signed_transaction_intent import SignedTransactionIntent
globals()['NotarizedTransactionHash'] = NotarizedTransactionHash
globals()['Signature'] = Signature
globals()['SignedTransactionIntent'] = SignedTransactionIntent
from core_client.model.notarized_transaction import NotarizedTransaction


class TestNotarizedTransaction(unittest.TestCase):
    """NotarizedTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNotarizedTransaction(self):
        """Test NotarizedTransaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NotarizedTransaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
