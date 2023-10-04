"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.ecdsa_secp256k1_signature import EcdsaSecp256k1Signature
from core_client.model.eddsa_ed25519_signature import EddsaEd25519Signature
from core_client.model.eddsa_ed25519_signature_all_of import EddsaEd25519SignatureAllOf
from core_client.model.public_key_type import PublicKeyType
from core_client.model.signature import Signature
globals()['EcdsaSecp256k1Signature'] = EcdsaSecp256k1Signature
globals()['EddsaEd25519Signature'] = EddsaEd25519Signature
globals()['EddsaEd25519SignatureAllOf'] = EddsaEd25519SignatureAllOf
globals()['PublicKeyType'] = PublicKeyType
globals()['Signature'] = Signature
from core_client.model.eddsa_ed25519_signature import EddsaEd25519Signature


class TestEddsaEd25519Signature(unittest.TestCase):
    """EddsaEd25519Signature unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEddsaEd25519Signature(self):
        """Test EddsaEd25519Signature"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EddsaEd25519Signature()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()