"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.public_key import PublicKey
from core_client.model.transaction_message import TransactionMessage
from core_client.model.transaction_preview_request_flags import TransactionPreviewRequestFlags
globals()['PublicKey'] = PublicKey
globals()['TransactionMessage'] = TransactionMessage
globals()['TransactionPreviewRequestFlags'] = TransactionPreviewRequestFlags
from core_client.model.transaction_preview_request import TransactionPreviewRequest


class TestTransactionPreviewRequest(unittest.TestCase):
    """TransactionPreviewRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTransactionPreviewRequest(self):
        """Test TransactionPreviewRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TransactionPreviewRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
