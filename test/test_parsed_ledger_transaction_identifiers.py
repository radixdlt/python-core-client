"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.intent_hash import IntentHash
from core_client.model.ledger_payload_hash import LedgerPayloadHash
from core_client.model.notarized_transaction_hash import NotarizedTransactionHash
from core_client.model.signed_intent_hash import SignedIntentHash
globals()['IntentHash'] = IntentHash
globals()['LedgerPayloadHash'] = LedgerPayloadHash
globals()['NotarizedTransactionHash'] = NotarizedTransactionHash
globals()['SignedIntentHash'] = SignedIntentHash
from core_client.model.parsed_ledger_transaction_identifiers import ParsedLedgerTransactionIdentifiers


class TestParsedLedgerTransactionIdentifiers(unittest.TestCase):
    """ParsedLedgerTransactionIdentifiers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParsedLedgerTransactionIdentifiers(self):
        """Test ParsedLedgerTransactionIdentifiers"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ParsedLedgerTransactionIdentifiers()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
