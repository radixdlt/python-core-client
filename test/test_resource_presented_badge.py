"""
    Radix Core API - Babylon

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.non_fungible_presented_badge import NonFungiblePresentedBadge
from core_client.model.presented_badge import PresentedBadge
from core_client.model.presented_badge_type import PresentedBadgeType
from core_client.model.resource_presented_badge import ResourcePresentedBadge
globals()['NonFungiblePresentedBadge'] = NonFungiblePresentedBadge
globals()['PresentedBadge'] = PresentedBadge
globals()['PresentedBadgeType'] = PresentedBadgeType
globals()['ResourcePresentedBadge'] = ResourcePresentedBadge
from core_client.model.resource_presented_badge import ResourcePresentedBadge


class TestResourcePresentedBadge(unittest.TestCase):
    """ResourcePresentedBadge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResourcePresentedBadge(self):
        """Test ResourcePresentedBadge"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ResourcePresentedBadge()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
