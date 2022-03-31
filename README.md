# Radix Core / System API - Python Clients and Models

- Core API version: 1.0.0
- Package version: 1.0.0

This Core/System API client is generated from the Core/System API spec using an Open API Generator. However, the current python generator is rather buggy,
so we've had to customise the generation with templates to get a working client.

For more information on this, or to regenerate, check out the [regeneration](./regeneration) folder.

Both of the API clients are generated over the top of each other, so

## API Docs

See [the API specifications](https://docs.radixdlt.com/main/apis/api-specification.html) on the Radix docs site.

# Open API Autogen'd Docs (from Core API generation)

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
                                    validator_address="validator_address_example",
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
                            resource_identifier=ResourceIdentifier(),
                        ),
                        data=Data(
                            action="CREATE",
                            data_object=DataObject(),
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
                    validator_address="validator_address_example",
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
*KeyApi* | [**key_list_post**](docs/KeyApi.md#key_list_post) | **POST** /key/list | Get public keys
*KeyApi* | [**key_sign_post**](docs/KeyApi.md#key_sign_post) | **POST** /key/sign | Sign transaction
*MempoolApi* | [**mempool_post**](docs/MempoolApi.md#mempool_post) | **POST** /mempool | Get Mempool Transactions
*MempoolApi* | [**mempool_transaction_post**](docs/MempoolApi.md#mempool_transaction_post) | **POST** /mempool/transaction | Get Mempool Transaction
*NetworkApi* | [**network_configuration_post**](docs/NetworkApi.md#network_configuration_post) | **POST** /network/configuration | Get Network Configuration
*NetworkApi* | [**network_status_post**](docs/NetworkApi.md#network_status_post) | **POST** /network/status | Get Network Status
*TransactionsApi* | [**transactions_post**](docs/TransactionsApi.md#transactions_post) | **POST** /transactions | Get Committed Transactions


## Documentation For Models

 - [AboveMaximumValidatorFeeIncreaseError](docs/AboveMaximumValidatorFeeIncreaseError.md)
 - [AboveMaximumValidatorFeeIncreaseErrorAllOf](docs/AboveMaximumValidatorFeeIncreaseErrorAllOf.md)
 - [Bech32HRPs](docs/Bech32HRPs.md)
 - [BelowMinimumStakeError](docs/BelowMinimumStakeError.md)
 - [BelowMinimumStakeErrorAllOf](docs/BelowMinimumStakeErrorAllOf.md)
 - [BigInteger](docs/BigInteger.md)
 - [CommittedTransaction](docs/CommittedTransaction.md)
 - [CommittedTransactionMetadata](docs/CommittedTransactionMetadata.md)
 - [CommittedTransactionsRequest](docs/CommittedTransactionsRequest.md)
 - [CommittedTransactionsResponse](docs/CommittedTransactionsResponse.md)
 - [ConstructionBuildRequest](docs/ConstructionBuildRequest.md)
 - [ConstructionBuildResponse](docs/ConstructionBuildResponse.md)
 - [ConstructionDeriveRequest](docs/ConstructionDeriveRequest.md)
 - [ConstructionDeriveRequestMetadata](docs/ConstructionDeriveRequestMetadata.md)
 - [ConstructionDeriveRequestMetadataAccount](docs/ConstructionDeriveRequestMetadataAccount.md)
 - [ConstructionDeriveRequestMetadataExitingUnstakes](docs/ConstructionDeriveRequestMetadataExitingUnstakes.md)
 - [ConstructionDeriveRequestMetadataExitingUnstakesAllOf](docs/ConstructionDeriveRequestMetadataExitingUnstakesAllOf.md)
 - [ConstructionDeriveRequestMetadataPreparedStakes](docs/ConstructionDeriveRequestMetadataPreparedStakes.md)
 - [ConstructionDeriveRequestMetadataPreparedStakesAllOf](docs/ConstructionDeriveRequestMetadataPreparedStakesAllOf.md)
 - [ConstructionDeriveRequestMetadataPreparedUnstakes](docs/ConstructionDeriveRequestMetadataPreparedUnstakes.md)
 - [ConstructionDeriveRequestMetadataToken](docs/ConstructionDeriveRequestMetadataToken.md)
 - [ConstructionDeriveRequestMetadataTokenAllOf](docs/ConstructionDeriveRequestMetadataTokenAllOf.md)
 - [ConstructionDeriveRequestMetadataValidator](docs/ConstructionDeriveRequestMetadataValidator.md)
 - [ConstructionDeriveRequestMetadataValidatorSystem](docs/ConstructionDeriveRequestMetadataValidatorSystem.md)
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
 - [DataObjectNotSupportedByEntityErrorAllOf](docs/DataObjectNotSupportedByEntityErrorAllOf.md)
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
 - [EpochDataAllOf](docs/EpochDataAllOf.md)
 - [FeeConstructionError](docs/FeeConstructionError.md)
 - [FeeConstructionErrorAllOf](docs/FeeConstructionErrorAllOf.md)
 - [FeeTable](docs/FeeTable.md)
 - [Fork](docs/Fork.md)
 - [InternalServerError](docs/InternalServerError.md)
 - [InternalServerErrorAllOf](docs/InternalServerErrorAllOf.md)
 - [InvalidAddressError](docs/InvalidAddressError.md)
 - [InvalidAddressErrorAllOf](docs/InvalidAddressErrorAllOf.md)
 - [InvalidDataObjectError](docs/InvalidDataObjectError.md)
 - [InvalidDataObjectErrorAllOf](docs/InvalidDataObjectErrorAllOf.md)
 - [InvalidFeePayerEntityError](docs/InvalidFeePayerEntityError.md)
 - [InvalidFeePayerEntityErrorAllOf](docs/InvalidFeePayerEntityErrorAllOf.md)
 - [InvalidHexError](docs/InvalidHexError.md)
 - [InvalidHexErrorAllOf](docs/InvalidHexErrorAllOf.md)
 - [InvalidJsonError](docs/InvalidJsonError.md)
 - [InvalidJsonErrorAllOf](docs/InvalidJsonErrorAllOf.md)
 - [InvalidPartialStateIdentifierError](docs/InvalidPartialStateIdentifierError.md)
 - [InvalidPartialStateIdentifierErrorAllOf](docs/InvalidPartialStateIdentifierErrorAllOf.md)
 - [InvalidPublicKeyError](docs/InvalidPublicKeyError.md)
 - [InvalidPublicKeyErrorAllOf](docs/InvalidPublicKeyErrorAllOf.md)
 - [InvalidSignatureError](docs/InvalidSignatureError.md)
 - [InvalidSignatureErrorAllOf](docs/InvalidSignatureErrorAllOf.md)
 - [InvalidSubEntityError](docs/InvalidSubEntityError.md)
 - [InvalidSubEntityErrorAllOf](docs/InvalidSubEntityErrorAllOf.md)
 - [InvalidTransactionError](docs/InvalidTransactionError.md)
 - [InvalidTransactionErrorAllOf](docs/InvalidTransactionErrorAllOf.md)
 - [InvalidTransactionHashError](docs/InvalidTransactionHashError.md)
 - [InvalidTransactionHashErrorAllOf](docs/InvalidTransactionHashErrorAllOf.md)
 - [KeyListRequest](docs/KeyListRequest.md)
 - [KeyListResponse](docs/KeyListResponse.md)
 - [KeySignRequest](docs/KeySignRequest.md)
 - [KeySignResponse](docs/KeySignResponse.md)
 - [MempoolFullError](docs/MempoolFullError.md)
 - [MempoolFullErrorAllOf](docs/MempoolFullErrorAllOf.md)
 - [MempoolRequest](docs/MempoolRequest.md)
 - [MempoolResponse](docs/MempoolResponse.md)
 - [MempoolTransactionRequest](docs/MempoolTransactionRequest.md)
 - [MempoolTransactionResponse](docs/MempoolTransactionResponse.md)
 - [MessageTooLongError](docs/MessageTooLongError.md)
 - [MessageTooLongErrorAllOf](docs/MessageTooLongErrorAllOf.md)
 - [NetworkConfigurationResponse](docs/NetworkConfigurationResponse.md)
 - [NetworkConfigurationResponseVersion](docs/NetworkConfigurationResponseVersion.md)
 - [NetworkIdentifier](docs/NetworkIdentifier.md)
 - [NetworkNotSupportedError](docs/NetworkNotSupportedError.md)
 - [NetworkNotSupportedErrorAllOf](docs/NetworkNotSupportedErrorAllOf.md)
 - [NetworkStatusRequest](docs/NetworkStatusRequest.md)
 - [NetworkStatusResponse](docs/NetworkStatusResponse.md)
 - [NotEnoughNativeTokensForFeesError](docs/NotEnoughNativeTokensForFeesError.md)
 - [NotEnoughNativeTokensForFeesErrorAllOf](docs/NotEnoughNativeTokensForFeesErrorAllOf.md)
 - [NotEnoughResourcesError](docs/NotEnoughResourcesError.md)
 - [NotEnoughResourcesErrorAllOf](docs/NotEnoughResourcesErrorAllOf.md)
 - [NotValidatorEntityError](docs/NotValidatorEntityError.md)
 - [NotValidatorEntityErrorAllOf](docs/NotValidatorEntityErrorAllOf.md)
 - [NotValidatorOwnerError](docs/NotValidatorOwnerError.md)
 - [NotValidatorOwnerErrorAllOf](docs/NotValidatorOwnerErrorAllOf.md)
 - [Operation](docs/Operation.md)
 - [OperationGroup](docs/OperationGroup.md)
 - [ParsedTransactionMetadata](docs/ParsedTransactionMetadata.md)
 - [PartialStateIdentifier](docs/PartialStateIdentifier.md)
 - [Peer](docs/Peer.md)
 - [PreparedValidatorFee](docs/PreparedValidatorFee.md)
 - [PreparedValidatorFeeAllOf](docs/PreparedValidatorFeeAllOf.md)
 - [PreparedValidatorOwner](docs/PreparedValidatorOwner.md)
 - [PreparedValidatorOwnerAllOf](docs/PreparedValidatorOwnerAllOf.md)
 - [PreparedValidatorRegistered](docs/PreparedValidatorRegistered.md)
 - [PreparedValidatorRegisteredAllOf](docs/PreparedValidatorRegisteredAllOf.md)
 - [PublicKey](docs/PublicKey.md)
 - [PublicKeyEntry](docs/PublicKeyEntry.md)
 - [PublicKeyIdentifiers](docs/PublicKeyIdentifiers.md)
 - [PublicKeyNotSupportedError](docs/PublicKeyNotSupportedError.md)
 - [PublicKeyNotSupportedErrorAllOf](docs/PublicKeyNotSupportedErrorAllOf.md)
 - [ResourceAmount](docs/ResourceAmount.md)
 - [ResourceDepositOperationNotSupportedByEntityError](docs/ResourceDepositOperationNotSupportedByEntityError.md)
 - [ResourceDepositOperationNotSupportedByEntityErrorAllOf](docs/ResourceDepositOperationNotSupportedByEntityErrorAllOf.md)
 - [ResourceIdentifier](docs/ResourceIdentifier.md)
 - [ResourceWithdrawOperationNotSupportedByEntityError](docs/ResourceWithdrawOperationNotSupportedByEntityError.md)
 - [ResourceWithdrawOperationNotSupportedByEntityErrorAllOf](docs/ResourceWithdrawOperationNotSupportedByEntityErrorAllOf.md)
 - [RoundData](docs/RoundData.md)
 - [RoundDataAllOf](docs/RoundDataAllOf.md)
 - [Signature](docs/Signature.md)
 - [StakeUnitResourceIdentifier](docs/StakeUnitResourceIdentifier.md)
 - [StakeUnitResourceIdentifierAllOf](docs/StakeUnitResourceIdentifierAllOf.md)
 - [StateIdentifier](docs/StateIdentifier.md)
 - [StateIdentifierNotFoundError](docs/StateIdentifierNotFoundError.md)
 - [StateIdentifierNotFoundErrorAllOf](docs/StateIdentifierNotFoundErrorAllOf.md)
 - [SubEntity](docs/SubEntity.md)
 - [SubEntityMetadata](docs/SubEntityMetadata.md)
 - [Substate](docs/Substate.md)
 - [SubstateDependencyNotFoundError](docs/SubstateDependencyNotFoundError.md)
 - [SubstateDependencyNotFoundErrorAllOf](docs/SubstateDependencyNotFoundErrorAllOf.md)
 - [SubstateIdentifier](docs/SubstateIdentifier.md)
 - [SubstateTypeIdentifier](docs/SubstateTypeIdentifier.md)
 - [SyncStatus](docs/SyncStatus.md)
 - [TokenData](docs/TokenData.md)
 - [TokenDataAllOf](docs/TokenDataAllOf.md)
 - [TokenMetadata](docs/TokenMetadata.md)
 - [TokenMetadataAllOf](docs/TokenMetadataAllOf.md)
 - [TokenResourceIdentifier](docs/TokenResourceIdentifier.md)
 - [TokenResourceIdentifierAllOf](docs/TokenResourceIdentifierAllOf.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionIdentifier](docs/TransactionIdentifier.md)
 - [TransactionIdentifierHash](docs/TransactionIdentifierHash.md)
 - [TransactionNotFoundError](docs/TransactionNotFoundError.md)
 - [TransactionNotFoundErrorAllOf](docs/TransactionNotFoundErrorAllOf.md)
 - [UnclaimedRadixEngineAddress](docs/UnclaimedRadixEngineAddress.md)
 - [UnexpectedError](docs/UnexpectedError.md)
 - [UpSubstateFeeEntry](docs/UpSubstateFeeEntry.md)
 - [Validator](docs/Validator.md)
 - [ValidatorAllowDelegation](docs/ValidatorAllowDelegation.md)
 - [ValidatorAllowDelegationAllOf](docs/ValidatorAllowDelegationAllOf.md)
 - [ValidatorBFTData](docs/ValidatorBFTData.md)
 - [ValidatorBFTDataAllOf](docs/ValidatorBFTDataAllOf.md)
 - [ValidatorData](docs/ValidatorData.md)
 - [ValidatorDataAllOf](docs/ValidatorDataAllOf.md)
 - [ValidatorMetadata](docs/ValidatorMetadata.md)
 - [ValidatorMetadataAllOf](docs/ValidatorMetadataAllOf.md)
 - [ValidatorSystemMetadata](docs/ValidatorSystemMetadata.md)
 - [ValidatorSystemMetadataAllOf](docs/ValidatorSystemMetadataAllOf.md)
 - [VirtualParentData](docs/VirtualParentData.md)
 - [VirtualParentDataAllOf](docs/VirtualParentDataAllOf.md)


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

