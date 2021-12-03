# core-client
This API provides endpoints for Radix network integrators.

# Overview

> WARNING
>
> The Core API is __NOT__ intended to be available on the public web. It is
> mainly designed to be accessed in a private network for integration use.

Welcome to the Radix Core API version 0.9.0 for Integrators. Version 0.9.0
is intended for integrators who wish to begin the process of developing an
integration between the Radix ledger and their own systems.

The Core API is separated into two:
* The **Data API** is a read-only api which allows integrators to view and
sync to the state of the ledger.
* The **Construction API** allows integrators to construct and submit a
transaction to the network on behalf of a key holder.

The Core API is primarily designed for network integrations such as exchanges,
ledger analytics providers, or hosted ledger data dashboards where detailed
ledger data is required and the integrator can be expected to run their node
to provide the Core API for their own consumption.

The Core API is not a full replacement for the current Node and Archive
[APIs](https://docs.radixdlt.com). We are also working on a public-facing
Gateway API that will be part of a full \"new API\", but is yet to be finalised.

We should stress that this API is in preview, and should __not__ be deployed
into production until version 1.0.0 has been finalised in an official Radix node
release.

## Backwards Compatibility

The OpenAPI specification of all endpoints in Version 0.9.0 is intended to be
backwards compatible with version 1.0.0 once released, so that there is little
risk that clients working with this spec will break after the release of 1.0.0.
Additional endpoints (such as retrieving mempool contents) are planned to be added.

## Rosetta

The Data API and Construction API is inspired from [Rosetta API](https://www.rosetta-api.org/)
most notably:
  * Use of a JSON-Based RPC protocol on top of HTTP Post requests
  * Use of Operations, Amounts, and Identifiers as universal language to
  express asset movement for reading and writing

There are a few notable exceptions to note:
  * Fetching of ledger data is through a Transaction stream rather than a
  Block stream
  * Use of `EntityIdentifier` rather than `AccountIdentifier`
  * Use of `OperationGroup` rather than `related_operations` to express related
  operations
  * Construction endpoints perform coin selection on behalf of the caller.
  This has the unfortunate effect of not being able to support high frequency
  transactions from a single account. This will be addressed in future updates.
  * Construction endpoints are online rather than offline as required by Rosetta

Future versions of the api will aim towards a fully-compliant Rosetta API.

## Client Reference Implementation

> IMPORTANT
>
> The Network Gateway service is subject to substantial change before official release in v1.

We are currently working on a client reference implementation to the Core API, which we are happy to share
with you for reference, as a demonstration of how to interpret responses from the Core API:

* [Latest - more functionality, no guarantees of correctness](https://github.com/radixdlt/radixdlt-network-gateway/)
* [Stable - old code, ingesting balance and transfer data, manually tested against stokenet](https://github.com/radixdlt/radixdlt-network-gateway/tree/v0.1_BalanceSubstatesAndHistory)

As a starter, check out the folder `./src/DataAggregator/LedgerExtension` for understanding how to parse
the contents of the transaction stream.

## Client Code Generation

We have found success with generating clients against the [api.yaml specification](https://raw.githubusercontent.com/radixdlt/radixdlt/feature/open-api/radixdlt-core/radixdlt/src/main/java/com/radixdlt/api/core/api.yaml)
in the core folder. See https://openapi-generator.tech/ for more details.

The OpenAPI generator only supports openapi version 3.0.0 at present, but you can
change 3.1.0 to 3.0.0 in the first line of the spec without affecting generation.

# Data API Flow

Integrators can make use of the Data API to synchronize a full or partial view of
the ledger, transaction by transaction.

![Data API Flow](https://raw.githubusercontent.com/radixdlt/radixdlt/feature/open-api/radixdlt-core/radixdlt/src/main/java/com/radixdlt/api/core/documentation/data_sequence_flow.png)

# Construction API Flow

Integrators can make use of the Construction API to construct and submit transactions
to the network.

![Construction API Flow](https://raw.githubusercontent.com/radixdlt/radixdlt/feature/open-api/radixdlt-core/radixdlt/src/main/java/com/radixdlt/api/core/documentation/construction_sequence_flow.png)

Unlike the Rosetta Construction API [specification](https://www.rosetta-api.org/docs/construction_api_introduction.html),
this Construction API selects UTXOs on behalf of the caller. This has the unfortunate
side effect of not being able to support high frequency transactions from a single
account due to UTXO conflicts. This will be addressed in a future release.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.9.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import core_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import core_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import core_client
from pprint import pprint
from core_client.api import construction_api
from core_client.model.construction_build_request import ConstructionBuildRequest
from core_client.model.construction_build_response import ConstructionBuildResponse
from core_client.model.construction_derive_request import ConstructionDeriveRequest
from core_client.model.construction_derive_response import ConstructionDeriveResponse
from core_client.model.construction_finalize_request import ConstructionFinalizeRequest
from core_client.model.construction_finalize_response import ConstructionFinalizeResponse
from core_client.model.construction_hash_request import ConstructionHashRequest
from core_client.model.construction_hash_response import ConstructionHashResponse
from core_client.model.construction_parse_request import ConstructionParseRequest
from core_client.model.construction_parse_response import ConstructionParseResponse
from core_client.model.construction_submit_request import ConstructionSubmitRequest
from core_client.model.construction_submit_response import ConstructionSubmitResponse
from core_client.model.unexpected_error import UnexpectedError
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)



# Enter a context with an instance of the API client
with core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = construction_api.ConstructionApi(api_client)
    construction_build_request = ConstructionBuildRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        operation_groups=[
            OperationGroup(
                operations=[
                    Operation(
                        type="type_example",
                        entity_identifier=EntityIdentifier(
                            address="address_example",
                            sub_entity=SubEntity(
                                address="address_example",
                                metadata=SubEntityMetadata(
                                    validator=ValidatorAddress("dv81QQFc9HeZTQLkQ2g5R"),
                                    epoch_unlock=1,
                                ),
                            ),
                        ),
                        substate=Substate(
                            substate_operation="BOOTUP",
                            substate_identifier=SubstateIdentifier(
                                identifier="identifier_example",
                            ),
                        ),
                        amount=ResourceAmount(
                            value=BigInteger("-80728"),
                            resource_identifier=ResourceIdentifier(
                                type="type_example",
                            ),
                        ),
                        data=Data(
                            action="CREATE",
                            data_object=DataObject(
                                type="type_example",
                            ),
                        ),
                        metadata={},
                    ),
                ],
                metadata={},
            ),
        ],
        fee_payer=EntityIdentifier(
            address="address_example",
            sub_entity=SubEntity(
                address="address_example",
                metadata=SubEntityMetadata(
                    validator=ValidatorAddress("dv81QQFc9HeZTQLkQ2g5R"),
                    epoch_unlock=1,
                ),
            ),
        ),
        message="message_example",
        disable_resource_allocate_and_destroy=True,
    ) # ConstructionBuildRequest | 

    try:
        # Build Transaction
        api_response = api_instance.construction_build_post(construction_build_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_build_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:3333*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConstructionApi* | [**construction_build_post**](docs/ConstructionApi.md#construction_build_post) | **POST** /construction/build | Build Transaction
*ConstructionApi* | [**construction_derive_post**](docs/ConstructionApi.md#construction_derive_post) | **POST** /construction/derive | Derive Entity Identifier
*ConstructionApi* | [**construction_finalize_post**](docs/ConstructionApi.md#construction_finalize_post) | **POST** /construction/finalize | Finalize Transaction
*ConstructionApi* | [**construction_hash_post**](docs/ConstructionApi.md#construction_hash_post) | **POST** /construction/hash | Get Transaction Hash
*ConstructionApi* | [**construction_parse_post**](docs/ConstructionApi.md#construction_parse_post) | **POST** /construction/parse | Parse Transaction
*ConstructionApi* | [**construction_submit_post**](docs/ConstructionApi.md#construction_submit_post) | **POST** /construction/submit | Submit Transaction
*EngineApi* | [**engine_configuration_post**](docs/EngineApi.md#engine_configuration_post) | **POST** /engine/configuration | Get Engine Configuration
*EngineApi* | [**engine_status_post**](docs/EngineApi.md#engine_status_post) | **POST** /engine/status | Get Engine Current Status
*EntityApi* | [**entity_post**](docs/EntityApi.md#entity_post) | **POST** /entity | Get Entity Information
*MempoolApi* | [**mempool_post**](docs/MempoolApi.md#mempool_post) | **POST** /mempool | Get Mempool Transactions
*MempoolApi* | [**mempool_transaction_post**](docs/MempoolApi.md#mempool_transaction_post) | **POST** /mempool/transaction | Get Mempool Transaction
*NetworkApi* | [**network_configuration_post**](docs/NetworkApi.md#network_configuration_post) | **POST** /network/configuration | Get Network Configuration
*NetworkApi* | [**network_status_post**](docs/NetworkApi.md#network_status_post) | **POST** /network/status | Get Network Status
*SignApi* | [**sign_post**](docs/SignApi.md#sign_post) | **POST** /sign | Sign a transaction with the node&#39;s key
*TransactionsApi* | [**transactions_post**](docs/TransactionsApi.md#transactions_post) | **POST** /transactions | Get Committed Transactions


## Documentation For Models

 - [AboveMaximumValidatorFeeIncreaseError](docs/AboveMaximumValidatorFeeIncreaseError.md)
 - [AccountAddress](docs/AccountAddress.md)
 - [Bech32HRPs](docs/Bech32HRPs.md)
 - [BelowMinimumStakeError](docs/BelowMinimumStakeError.md)
 - [BigInteger](docs/BigInteger.md)
 - [CommittedTransaction](docs/CommittedTransaction.md)
 - [CommittedTransactionMetadata](docs/CommittedTransactionMetadata.md)
 - [CommittedTransactionsRequest](docs/CommittedTransactionsRequest.md)
 - [CommittedTransactionsResponse](docs/CommittedTransactionsResponse.md)
 - [ConstructionBuildRequest](docs/ConstructionBuildRequest.md)
 - [ConstructionBuildResponse](docs/ConstructionBuildResponse.md)
 - [ConstructionDeriveRequest](docs/ConstructionDeriveRequest.md)
 - [ConstructionDeriveRequestMetadata](docs/ConstructionDeriveRequestMetadata.md)
 - [ConstructionDeriveRequestMetadataToken](docs/ConstructionDeriveRequestMetadataToken.md)
 - [ConstructionDeriveResponse](docs/ConstructionDeriveResponse.md)
 - [ConstructionFinalizeRequest](docs/ConstructionFinalizeRequest.md)
 - [ConstructionFinalizeResponse](docs/ConstructionFinalizeResponse.md)
 - [ConstructionHashRequest](docs/ConstructionHashRequest.md)
 - [ConstructionHashResponse](docs/ConstructionHashResponse.md)
 - [ConstructionParseRequest](docs/ConstructionParseRequest.md)
 - [ConstructionParseResponse](docs/ConstructionParseResponse.md)
 - [ConstructionSubmitRequest](docs/ConstructionSubmitRequest.md)
 - [ConstructionSubmitResponse](docs/ConstructionSubmitResponse.md)
 - [CoreError](docs/CoreError.md)
 - [Data](docs/Data.md)
 - [DataObject](docs/DataObject.md)
 - [DataObjectNotSupportedByEntityError](docs/DataObjectNotSupportedByEntityError.md)
 - [EngineCheckpoint](docs/EngineCheckpoint.md)
 - [EngineConfiguration](docs/EngineConfiguration.md)
 - [EngineConfigurationRequest](docs/EngineConfigurationRequest.md)
 - [EngineConfigurationResponse](docs/EngineConfigurationResponse.md)
 - [EngineIdentifier](docs/EngineIdentifier.md)
 - [EngineStateIdentifier](docs/EngineStateIdentifier.md)
 - [EngineStatusRequest](docs/EngineStatusRequest.md)
 - [EngineStatusResponse](docs/EngineStatusResponse.md)
 - [EntityIdentifier](docs/EntityIdentifier.md)
 - [EntityRequest](docs/EntityRequest.md)
 - [EntityResponse](docs/EntityResponse.md)
 - [EntitySetIdentifier](docs/EntitySetIdentifier.md)
 - [EpochData](docs/EpochData.md)
 - [FeeConstructionError](docs/FeeConstructionError.md)
 - [FeeTable](docs/FeeTable.md)
 - [Fork](docs/Fork.md)
 - [ForkIdentifier](docs/ForkIdentifier.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [InvalidAddressError](docs/InvalidAddressError.md)
 - [InvalidDataObjectError](docs/InvalidDataObjectError.md)
 - [InvalidFeePayerEntityError](docs/InvalidFeePayerEntityError.md)
 - [InvalidHexError](docs/InvalidHexError.md)
 - [InvalidJsonError](docs/InvalidJsonError.md)
 - [InvalidPartialStateIdentifierError](docs/InvalidPartialStateIdentifierError.md)
 - [InvalidPublicKeyError](docs/InvalidPublicKeyError.md)
 - [InvalidSignatureError](docs/InvalidSignatureError.md)
 - [InvalidSubEntityError](docs/InvalidSubEntityError.md)
 - [InvalidTransactionError](docs/InvalidTransactionError.md)
 - [InvalidTransactionHashError](docs/InvalidTransactionHashError.md)
 - [MempoolRequest](docs/MempoolRequest.md)
 - [MempoolResponse](docs/MempoolResponse.md)
 - [MempoolTransactionRequest](docs/MempoolTransactionRequest.md)
 - [MempoolTransactionResponse](docs/MempoolTransactionResponse.md)
 - [MessageTooLongError](docs/MessageTooLongError.md)
 - [NetworkConfigurationResponse](docs/NetworkConfigurationResponse.md)
 - [NetworkConfigurationResponseVersion](docs/NetworkConfigurationResponseVersion.md)
 - [NetworkIdentifier](docs/NetworkIdentifier.md)
 - [NetworkNotSupportedError](docs/NetworkNotSupportedError.md)
 - [NetworkStatusRequest](docs/NetworkStatusRequest.md)
 - [NetworkStatusResponse](docs/NetworkStatusResponse.md)
 - [NetworkStatusResponseNodeIdentifiers](docs/NetworkStatusResponseNodeIdentifiers.md)
 - [NotEnoughResourcesError](docs/NotEnoughResourcesError.md)
 - [NotValidatorOwnerError](docs/NotValidatorOwnerError.md)
 - [Operation](docs/Operation.md)
 - [OperationGroup](docs/OperationGroup.md)
 - [ParsedTransactionMetadata](docs/ParsedTransactionMetadata.md)
 - [PartialStateIdentifier](docs/PartialStateIdentifier.md)
 - [Peer](docs/Peer.md)
 - [PreparedValidatorFee](docs/PreparedValidatorFee.md)
 - [PreparedValidatorOwner](docs/PreparedValidatorOwner.md)
 - [PreparedValidatorRegistered](docs/PreparedValidatorRegistered.md)
 - [PublicKey](docs/PublicKey.md)
 - [PublicKeyNotSupportedError](docs/PublicKeyNotSupportedError.md)
 - [RRI](docs/RRI.md)
 - [ResourceAmount](docs/ResourceAmount.md)
 - [ResourceDepositOperationNotSupportedByEntityError](docs/ResourceDepositOperationNotSupportedByEntityError.md)
 - [ResourceIdentifier](docs/ResourceIdentifier.md)
 - [ResourceWithdrawOperationNotSupportedByEntityError](docs/ResourceWithdrawOperationNotSupportedByEntityError.md)
 - [RoundData](docs/RoundData.md)
 - [SignRequest](docs/SignRequest.md)
 - [SignResponse](docs/SignResponse.md)
 - [Signature](docs/Signature.md)
 - [StakeUnitResourceIdentifier](docs/StakeUnitResourceIdentifier.md)
 - [StateIdentifier](docs/StateIdentifier.md)
 - [StateIdentifierNotFoundError](docs/StateIdentifierNotFoundError.md)
 - [SubEntity](docs/SubEntity.md)
 - [SubEntityMetadata](docs/SubEntityMetadata.md)
 - [Substate](docs/Substate.md)
 - [SubstateDependencyNotFoundError](docs/SubstateDependencyNotFoundError.md)
 - [SubstateIdentifier](docs/SubstateIdentifier.md)
 - [SubstateTypeIdentifier](docs/SubstateTypeIdentifier.md)
 - [SyncStatus](docs/SyncStatus.md)
 - [TokenData](docs/TokenData.md)
 - [TokenMetadata](docs/TokenMetadata.md)
 - [TokenResourceIdentifier](docs/TokenResourceIdentifier.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionIdentifier](docs/TransactionIdentifier.md)
 - [TransactionIdentifierHash](docs/TransactionIdentifierHash.md)
 - [TransactionNotFoundError](docs/TransactionNotFoundError.md)
 - [UnclaimedRadixEngineAddress](docs/UnclaimedRadixEngineAddress.md)
 - [UnexpectedError](docs/UnexpectedError.md)
 - [UpSubstateFeeEntry](docs/UpSubstateFeeEntry.md)
 - [Validator](docs/Validator.md)
 - [ValidatorAddress](docs/ValidatorAddress.md)
 - [ValidatorAllowDelegation](docs/ValidatorAllowDelegation.md)
 - [ValidatorBFTData](docs/ValidatorBFTData.md)
 - [ValidatorData](docs/ValidatorData.md)
 - [ValidatorMetadata](docs/ValidatorMetadata.md)
 - [ValidatorSystemMetadata](docs/ValidatorSystemMetadata.md)
 - [VirtualParentData](docs/VirtualParentData.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in core_client.apis and core_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from core_client.api.default_api import DefaultApi`
- `from core_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import core_client
from core_client.apis import *
from core_client.models import *
```

