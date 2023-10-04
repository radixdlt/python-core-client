"""
    Radix Core API - Babylon

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.ledger_hashes import LedgerHashes
from core_client.model.next_epoch import NextEpoch
from core_client.model.state_version import StateVersion
globals()['LedgerHashes'] = LedgerHashes
globals()['NextEpoch'] = NextEpoch
globals()['StateVersion'] = StateVersion
from core_client.model.ledger_header import LedgerHeader


class TestLedgerHeader(unittest.TestCase):
    """LedgerHeader unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLedgerHeader(self):
        """Test LedgerHeader"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LedgerHeader()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()