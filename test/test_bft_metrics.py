"""
    Radix System API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import system_client
from system_client.model.bft_pacemaker_metrics import BFTPacemakerMetrics
from system_client.model.bft_sync_metrics import BFTSyncMetrics
from system_client.model.bft_vertex_store_metrics import BFTVertexStoreMetrics
globals()['BFTPacemakerMetrics'] = BFTPacemakerMetrics
globals()['BFTSyncMetrics'] = BFTSyncMetrics
globals()['BFTVertexStoreMetrics'] = BFTVertexStoreMetrics
from system_client.model.bft_metrics import BFTMetrics


class TestBFTMetrics(unittest.TestCase):
    """BFTMetrics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBFTMetrics(self):
        """Test BFTMetrics"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BFTMetrics()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
