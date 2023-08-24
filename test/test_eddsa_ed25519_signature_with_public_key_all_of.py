"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.eddsa_ed25519_public_key import EddsaEd25519PublicKey
from core_client.model.eddsa_ed25519_signature import EddsaEd25519Signature
globals()['EddsaEd25519PublicKey'] = EddsaEd25519PublicKey
globals()['EddsaEd25519Signature'] = EddsaEd25519Signature
from core_client.model.eddsa_ed25519_signature_with_public_key_all_of import EddsaEd25519SignatureWithPublicKeyAllOf


class TestEddsaEd25519SignatureWithPublicKeyAllOf(unittest.TestCase):
    """EddsaEd25519SignatureWithPublicKeyAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEddsaEd25519SignatureWithPublicKeyAllOf(self):
        """Test EddsaEd25519SignatureWithPublicKeyAllOf"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EddsaEd25519SignatureWithPublicKeyAllOf()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
