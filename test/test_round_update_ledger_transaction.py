"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.genesis_ledger_transaction import GenesisLedgerTransaction
from core_client.model.ledger_transaction import LedgerTransaction
from core_client.model.ledger_transaction_type import LedgerTransactionType
from core_client.model.round_update_ledger_transaction import RoundUpdateLedgerTransaction
from core_client.model.round_update_ledger_transaction_all_of import RoundUpdateLedgerTransactionAllOf
from core_client.model.round_update_transaction import RoundUpdateTransaction
from core_client.model.user_ledger_transaction import UserLedgerTransaction
globals()['GenesisLedgerTransaction'] = GenesisLedgerTransaction
globals()['LedgerTransaction'] = LedgerTransaction
globals()['LedgerTransactionType'] = LedgerTransactionType
globals()['RoundUpdateLedgerTransaction'] = RoundUpdateLedgerTransaction
globals()['RoundUpdateLedgerTransactionAllOf'] = RoundUpdateLedgerTransactionAllOf
globals()['RoundUpdateTransaction'] = RoundUpdateTransaction
globals()['UserLedgerTransaction'] = UserLedgerTransaction
from core_client.model.round_update_ledger_transaction import RoundUpdateLedgerTransaction


class TestRoundUpdateLedgerTransaction(unittest.TestCase):
    """RoundUpdateLedgerTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRoundUpdateLedgerTransaction(self):
        """Test RoundUpdateLedgerTransaction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RoundUpdateLedgerTransaction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
