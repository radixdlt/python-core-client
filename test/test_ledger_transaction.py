"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.genesis_ledger_transaction import GenesisLedgerTransaction
from core_client.model.ledger_transaction_type import LedgerTransactionType
from core_client.model.round_update_ledger_transaction import RoundUpdateLedgerTransaction
from core_client.model.user_ledger_transaction import UserLedgerTransaction
globals()['GenesisLedgerTransaction'] = GenesisLedgerTransaction
globals()['LedgerTransactionType'] = LedgerTransactionType
globals()['RoundUpdateLedgerTransaction'] = RoundUpdateLedgerTransaction
globals()['UserLedgerTransaction'] = UserLedgerTransaction
from core_client.model.ledger_transaction import LedgerTransaction


class TestLedgerTransaction(unittest.TestCase):
    """LedgerTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLedgerTransaction(self):
        """Test LedgerTransaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LedgerTransaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
