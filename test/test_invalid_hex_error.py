"""
    Radix Core API

    This API provides endpoints for Radix network integrators.  # Overview  > WARNING > > The Core API is __NOT__ intended to be available on the public web. It is > mainly designed to be accessed in a private network for integration use.  Welcome to the Radix Core API version 0.9.0 for Integrators. Version 0.9.0 is intended for integrators who wish to begin the process of developing an integration between the Radix ledger and their own systems.  The Core API is separated into two: * The **Data API** is a read-only api which allows integrators to view and sync to the state of the ledger. * The **Construction API** allows integrators to construct and submit a transaction to the network on behalf of a key holder.  The Core API is primarily designed for network integrations such as exchanges, ledger analytics providers, or hosted ledger data dashboards where detailed ledger data is required and the integrator can be expected to run their node to provide the Core API for their own consumption.  The Core API is not a full replacement for the current Node and Archive [APIs](https://docs.radixdlt.com). We are also working on a public-facing Gateway API that will be part of a full \"new API\", but is yet to be finalised.  We should stress that this API is in preview, and should __not__ be deployed into production until version 1.0.0 has been finalised in an official Radix node release.  ## Backwards Compatibility  The OpenAPI specification of all endpoints in Version 0.9.0 is intended to be backwards compatible with version 1.0.0 once released, so that there is little risk that clients working with this spec will break after the release of 1.0.0. Additional endpoints (such as retrieving mempool contents) are planned to be added.  ## Rosetta  The Data API and Construction API is inspired from [Rosetta API](https://www.rosetta-api.org/) most notably:   * Use of a JSON-Based RPC protocol on top of HTTP Post requests   * Use of Operations, Amounts, and Identifiers as universal language to   express asset movement for reading and writing  There are a few notable exceptions to note:   * Fetching of ledger data is through a Transaction stream rather than a   Block stream   * Use of `EntityIdentifier` rather than `AccountIdentifier`   * Use of `OperationGroup` rather than `related_operations` to express related   operations   * Construction endpoints perform coin selection on behalf of the caller.   This has the unfortunate effect of not being able to support high frequency   transactions from a single account. This will be addressed in future updates.   * Construction endpoints are online rather than offline as required by Rosetta  Future versions of the api will aim towards a fully-compliant Rosetta API.  ## Client Reference Implementation  > IMPORTANT > > The Network Gateway service is subject to substantial change before official release in v1.  We are currently working on a client reference implementation to the Core API, which we are happy to share with you for reference, as a demonstration of how to interpret responses from the Core API:  * [Latest - more functionality, no guarantees of correctness](https://github.com/radixdlt/radixdlt-network-gateway/) * [Stable - old code, ingesting balance and transfer data, manually tested against stokenet](https://github.com/radixdlt/radixdlt-network-gateway/tree/v0.1_BalanceSubstatesAndHistory)  As a starter, check out the folder `./src/DataAggregator/LedgerExtension` for understanding how to parse the contents of the transaction stream.  ## Client Code Generation  We have found success with generating clients against the [api.yaml specification](https://raw.githubusercontent.com/radixdlt/radixdlt/feature/open-api/radixdlt-core/radixdlt/src/main/java/com/radixdlt/api/core/api.yaml) in the core folder. See https://openapi-generator.tech/ for more details.  The OpenAPI generator only supports openapi version 3.0.0 at present, but you can change 3.1.0 to 3.0.0 in the first line of the spec without affecting generation.  # Data API Flow  Integrators can make use of the Data API to synchronize a full or partial view of the ledger, transaction by transaction.  ![Data API Flow](https://raw.githubusercontent.com/radixdlt/radixdlt/feature/open-api/radixdlt-core/radixdlt/src/main/java/com/radixdlt/api/core/documentation/data_sequence_flow.png)  # Construction API Flow  Integrators can make use of the Construction API to construct and submit transactions to the network.  ![Construction API Flow](https://raw.githubusercontent.com/radixdlt/radixdlt/feature/open-api/radixdlt-core/radixdlt/src/main/java/com/radixdlt/api/core/documentation/construction_sequence_flow.png)  Unlike the Rosetta Construction API [specification](https://www.rosetta-api.org/docs/construction_api_introduction.html), this Construction API selects UTXOs on behalf of the caller. This has the unfortunate side effect of not being able to support high frequency transactions from a single account due to UTXO conflicts. This will be addressed in a future release.   # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.above_maximum_validator_fee_increase_error import AboveMaximumValidatorFeeIncreaseError
from openapi_client.model.below_minimum_stake_error import BelowMinimumStakeError
from openapi_client.model.core_error import CoreError
from openapi_client.model.data_object_not_supported_by_entity_error import DataObjectNotSupportedByEntityError
from openapi_client.model.fee_construction_error import FeeConstructionError
from openapi_client.model.internal_server_error import InternalServerError
from openapi_client.model.invalid_address_error import InvalidAddressError
from openapi_client.model.invalid_data_object_error import InvalidDataObjectError
from openapi_client.model.invalid_fee_payer_entity_error import InvalidFeePayerEntityError
from openapi_client.model.invalid_hex_error import InvalidHexError
from openapi_client.model.invalid_hex_error_all_of import InvalidHexErrorAllOf
from openapi_client.model.invalid_json_error import InvalidJsonError
from openapi_client.model.invalid_partial_state_identifier_error import InvalidPartialStateIdentifierError
from openapi_client.model.invalid_public_key_error import InvalidPublicKeyError
from openapi_client.model.invalid_signature_error import InvalidSignatureError
from openapi_client.model.invalid_sub_entity_error import InvalidSubEntityError
from openapi_client.model.invalid_transaction_error import InvalidTransactionError
from openapi_client.model.invalid_transaction_hash_error import InvalidTransactionHashError
from openapi_client.model.message_too_long_error import MessageTooLongError
from openapi_client.model.network_not_supported_error import NetworkNotSupportedError
from openapi_client.model.not_enough_resources_error import NotEnoughResourcesError
from openapi_client.model.not_validator_owner_error import NotValidatorOwnerError
from openapi_client.model.public_key_not_supported_error import PublicKeyNotSupportedError
from openapi_client.model.resource_deposit_operation_not_supported_by_entity_error import ResourceDepositOperationNotSupportedByEntityError
from openapi_client.model.resource_withdraw_operation_not_supported_by_entity_error import ResourceWithdrawOperationNotSupportedByEntityError
from openapi_client.model.state_identifier_not_found_error import StateIdentifierNotFoundError
from openapi_client.model.substate_dependency_not_found_error import SubstateDependencyNotFoundError
from openapi_client.model.transaction_not_found_error import TransactionNotFoundError
globals()['AboveMaximumValidatorFeeIncreaseError'] = AboveMaximumValidatorFeeIncreaseError
globals()['BelowMinimumStakeError'] = BelowMinimumStakeError
globals()['CoreError'] = CoreError
globals()['DataObjectNotSupportedByEntityError'] = DataObjectNotSupportedByEntityError
globals()['FeeConstructionError'] = FeeConstructionError
globals()['InternalServerError'] = InternalServerError
globals()['InvalidAddressError'] = InvalidAddressError
globals()['InvalidDataObjectError'] = InvalidDataObjectError
globals()['InvalidFeePayerEntityError'] = InvalidFeePayerEntityError
globals()['InvalidHexError'] = InvalidHexError
globals()['InvalidHexErrorAllOf'] = InvalidHexErrorAllOf
globals()['InvalidJsonError'] = InvalidJsonError
globals()['InvalidPartialStateIdentifierError'] = InvalidPartialStateIdentifierError
globals()['InvalidPublicKeyError'] = InvalidPublicKeyError
globals()['InvalidSignatureError'] = InvalidSignatureError
globals()['InvalidSubEntityError'] = InvalidSubEntityError
globals()['InvalidTransactionError'] = InvalidTransactionError
globals()['InvalidTransactionHashError'] = InvalidTransactionHashError
globals()['MessageTooLongError'] = MessageTooLongError
globals()['NetworkNotSupportedError'] = NetworkNotSupportedError
globals()['NotEnoughResourcesError'] = NotEnoughResourcesError
globals()['NotValidatorOwnerError'] = NotValidatorOwnerError
globals()['PublicKeyNotSupportedError'] = PublicKeyNotSupportedError
globals()['ResourceDepositOperationNotSupportedByEntityError'] = ResourceDepositOperationNotSupportedByEntityError
globals()['ResourceWithdrawOperationNotSupportedByEntityError'] = ResourceWithdrawOperationNotSupportedByEntityError
globals()['StateIdentifierNotFoundError'] = StateIdentifierNotFoundError
globals()['SubstateDependencyNotFoundError'] = SubstateDependencyNotFoundError
globals()['TransactionNotFoundError'] = TransactionNotFoundError
from openapi_client.model.invalid_hex_error import InvalidHexError


class TestInvalidHexError(unittest.TestCase):
    """InvalidHexError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvalidHexError(self):
        """Test InvalidHexError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InvalidHexError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
