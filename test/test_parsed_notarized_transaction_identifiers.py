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
from core_client.model.parsed_notarized_transaction_identifiers import ParsedNotarizedTransactionIdentifiers


class TestParsedNotarizedTransactionIdentifiers(unittest.TestCase):
    """ParsedNotarizedTransactionIdentifiers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParsedNotarizedTransactionIdentifiers(self):
        """Test ParsedNotarizedTransactionIdentifiers"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ParsedNotarizedTransactionIdentifiers()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
