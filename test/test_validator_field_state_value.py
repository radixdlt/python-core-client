"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.ecdsa_secp256k1_public_key import EcdsaSecp256k1PublicKey
from core_client.model.entity_reference import EntityReference
from core_client.model.pending_owner_stake_withdrawal import PendingOwnerStakeWithdrawal
from core_client.model.substate_key import SubstateKey
from core_client.model.validator_fee_change_request import ValidatorFeeChangeRequest
globals()['EcdsaSecp256k1PublicKey'] = EcdsaSecp256k1PublicKey
globals()['EntityReference'] = EntityReference
globals()['PendingOwnerStakeWithdrawal'] = PendingOwnerStakeWithdrawal
globals()['SubstateKey'] = SubstateKey
globals()['ValidatorFeeChangeRequest'] = ValidatorFeeChangeRequest
from core_client.model.validator_field_state_value import ValidatorFieldStateValue


class TestValidatorFieldStateValue(unittest.TestCase):
    """ValidatorFieldStateValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidatorFieldStateValue(self):
        """Test ValidatorFieldStateValue"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ValidatorFieldStateValue()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
