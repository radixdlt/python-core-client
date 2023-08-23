# Radix Core / System API - Python Clients and Models

- Core API version: 0.4.0
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
from core_client.api import lts_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_state_account_all_fungible_resource_balances_request import LtsStateAccountAllFungibleResourceBalancesRequest
from core_client.model.lts_state_account_all_fungible_resource_balances_response import LtsStateAccountAllFungibleResourceBalancesResponse
from core_client.model.lts_state_account_fungible_resource_balance_request import LtsStateAccountFungibleResourceBalanceRequest
from core_client.model.lts_state_account_fungible_resource_balance_response import LtsStateAccountFungibleResourceBalanceResponse
from core_client.model.lts_stream_account_transaction_outcomes_request import LtsStreamAccountTransactionOutcomesRequest
from core_client.model.lts_stream_account_transaction_outcomes_response import LtsStreamAccountTransactionOutcomesResponse
from core_client.model.lts_stream_transaction_outcomes_request import LtsStreamTransactionOutcomesRequest
from core_client.model.lts_stream_transaction_outcomes_response import LtsStreamTransactionOutcomesResponse
from core_client.model.lts_transaction_construction_request import LtsTransactionConstructionRequest
from core_client.model.lts_transaction_construction_response import LtsTransactionConstructionResponse
from core_client.model.lts_transaction_status_request import LtsTransactionStatusRequest
from core_client.model.lts_transaction_status_response import LtsTransactionStatusResponse
from core_client.model.lts_transaction_submit_request import LtsTransactionSubmitRequest
from core_client.model.lts_transaction_submit_response import LtsTransactionSubmitResponse
from core_client.model.transaction_submit_error_response import TransactionSubmitErrorResponse
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)



# Enter a context with an instance of the API client
with core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_state_account_all_fungible_resource_balances_request = LtsStateAccountAllFungibleResourceBalancesRequest(
        network="{{network}}",
        account_address="account_address_example",
    ) # LtsStateAccountAllFungibleResourceBalancesRequest | 

    try:
        # Get All Account Balances
        api_response = api_instance.lts_state_account_all_fungible_resource_balances_post(lts_state_account_all_fungible_resource_balances_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_state_account_all_fungible_resource_balances_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:3333/core*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LTSApi* | [**lts_state_account_all_fungible_resource_balances_post**](docs/LTSApi.md#lts_state_account_all_fungible_resource_balances_post) | **POST** /lts/state/account-all-fungible-resource-balances | Get All Account Balances
*LTSApi* | [**lts_state_account_fungible_resource_balance_post**](docs/LTSApi.md#lts_state_account_fungible_resource_balance_post) | **POST** /lts/state/account-fungible-resource-balance | Get Single Account Balance
*LTSApi* | [**lts_stream_account_transaction_outcomes_post**](docs/LTSApi.md#lts_stream_account_transaction_outcomes_post) | **POST** /lts/stream/account-transaction-outcomes | Get Account Transaction Outcomes
*LTSApi* | [**lts_stream_transaction_outcomes_post**](docs/LTSApi.md#lts_stream_transaction_outcomes_post) | **POST** /lts/stream/transaction-outcomes | Get Transaction Outcomes
*LTSApi* | [**lts_transaction_construction_post**](docs/LTSApi.md#lts_transaction_construction_post) | **POST** /lts/transaction/construction | Get Construction Metadata
*LTSApi* | [**lts_transaction_status_post**](docs/LTSApi.md#lts_transaction_status_post) | **POST** /lts/transaction/status | Get Transaction Status
*LTSApi* | [**lts_transaction_submit_post**](docs/LTSApi.md#lts_transaction_submit_post) | **POST** /lts/transaction/submit | Submit Transaction
*MempoolApi* | [**mempool_list_post**](docs/MempoolApi.md#mempool_list_post) | **POST** /mempool/list | Get Mempool List
*MempoolApi* | [**mempool_transaction_post**](docs/MempoolApi.md#mempool_transaction_post) | **POST** /mempool/transaction | Get Mempool Transaction
*StateApi* | [**state_access_controller_post**](docs/StateApi.md#state_access_controller_post) | **POST** /state/access-controller | Get Access Controller Details
*StateApi* | [**state_account_post**](docs/StateApi.md#state_account_post) | **POST** /state/account | Get Account Details
*StateApi* | [**state_component_post**](docs/StateApi.md#state_component_post) | **POST** /state/component | Get Component Details
*StateApi* | [**state_consensus_manager_post**](docs/StateApi.md#state_consensus_manager_post) | **POST** /state/consensus-manager | Get Consensus Manager Details
*StateApi* | [**state_non_fungible_post**](docs/StateApi.md#state_non_fungible_post) | **POST** /state/non-fungible | Get Non-Fungible Details
*StateApi* | [**state_package_post**](docs/StateApi.md#state_package_post) | **POST** /state/package | Get Package Details
*StateApi* | [**state_resource_post**](docs/StateApi.md#state_resource_post) | **POST** /state/resource | Get Resource Details
*StateApi* | [**state_validator_post**](docs/StateApi.md#state_validator_post) | **POST** /state/validator | Get Validator Details
*StatusApi* | [**status_network_configuration_post**](docs/StatusApi.md#status_network_configuration_post) | **POST** /status/network-configuration | Get Network Configuration
*StatusApi* | [**status_network_status_post**](docs/StatusApi.md#status_network_status_post) | **POST** /status/network-status | Get Network Status
*StatusApi* | [**status_scenarios_post**](docs/StatusApi.md#status_scenarios_post) | **POST** /status/scenarios | Get Scenarios&#39; results.
*StreamApi* | [**stream_transactions_post**](docs/StreamApi.md#stream_transactions_post) | **POST** /stream/transactions | Get Committed Transactions
*TransactionApi* | [**transaction_call_preview_post**](docs/TransactionApi.md#transaction_call_preview_post) | **POST** /transaction/call-preview | Scrypto Call Preview
*TransactionApi* | [**transaction_parse_post**](docs/TransactionApi.md#transaction_parse_post) | **POST** /transaction/parse | Parse Transaction Payload
*TransactionApi* | [**transaction_preview_post**](docs/TransactionApi.md#transaction_preview_post) | **POST** /transaction/preview | Transaction Preview
*TransactionApi* | [**transaction_receipt_post**](docs/TransactionApi.md#transaction_receipt_post) | **POST** /transaction/receipt | Get Transaction Receipt
*TransactionApi* | [**transaction_status_post**](docs/TransactionApi.md#transaction_status_post) | **POST** /transaction/status | Get Transaction Status
*TransactionApi* | [**transaction_submit_post**](docs/TransactionApi.md#transaction_submit_post) | **POST** /transaction/submit | Transaction Submit


## Documentation For Models

 - [AccessControllerFieldStateSubstate](docs/AccessControllerFieldStateSubstate.md)
 - [AccessControllerFieldStateSubstateAllOf](docs/AccessControllerFieldStateSubstateAllOf.md)
 - [AccessControllerFieldStateValue](docs/AccessControllerFieldStateValue.md)
 - [AccessRule](docs/AccessRule.md)
 - [AccessRuleNode](docs/AccessRuleNode.md)
 - [AccessRuleNodeType](docs/AccessRuleNodeType.md)
 - [AccessRuleType](docs/AccessRuleType.md)
 - [AccessRulesModuleFieldOwnerRoleSubstate](docs/AccessRulesModuleFieldOwnerRoleSubstate.md)
 - [AccessRulesModuleFieldOwnerRoleSubstateAllOf](docs/AccessRulesModuleFieldOwnerRoleSubstateAllOf.md)
 - [AccessRulesModuleFieldOwnerRoleValue](docs/AccessRulesModuleFieldOwnerRoleValue.md)
 - [AccessRulesModuleRuleEntrySubstate](docs/AccessRulesModuleRuleEntrySubstate.md)
 - [AccessRulesModuleRuleEntrySubstateAllOf](docs/AccessRulesModuleRuleEntrySubstateAllOf.md)
 - [AccessRulesModuleRuleEntryValue](docs/AccessRulesModuleRuleEntryValue.md)
 - [AccountDepositRuleIndexEntrySubstate](docs/AccountDepositRuleIndexEntrySubstate.md)
 - [AccountDepositRuleIndexEntrySubstateAllOf](docs/AccountDepositRuleIndexEntrySubstateAllOf.md)
 - [AccountDepositRuleIndexEntryValue](docs/AccountDepositRuleIndexEntryValue.md)
 - [AccountFieldStateSubstate](docs/AccountFieldStateSubstate.md)
 - [AccountFieldStateSubstateAllOf](docs/AccountFieldStateSubstateAllOf.md)
 - [AccountFieldStateValue](docs/AccountFieldStateValue.md)
 - [AccountVaultIndexEntrySubstate](docs/AccountVaultIndexEntrySubstate.md)
 - [AccountVaultIndexEntrySubstateAllOf](docs/AccountVaultIndexEntrySubstateAllOf.md)
 - [AccountVaultIndexEntryValue](docs/AccountVaultIndexEntryValue.md)
 - [ActiveValidator](docs/ActiveValidator.md)
 - [ActiveValidatorIndex](docs/ActiveValidatorIndex.md)
 - [ActiveValidatorKey](docs/ActiveValidatorKey.md)
 - [AddressType](docs/AddressType.md)
 - [AllOfAccessRuleNode](docs/AllOfAccessRuleNode.md)
 - [AllOfProofRule](docs/AllOfProofRule.md)
 - [AllOfProofRuleAllOf](docs/AllOfProofRuleAllOf.md)
 - [AllowAllAccessRule](docs/AllowAllAccessRule.md)
 - [AmountOfProofRule](docs/AmountOfProofRule.md)
 - [AmountOfProofRuleAllOf](docs/AmountOfProofRuleAllOf.md)
 - [AnyOfAccessRuleNode](docs/AnyOfAccessRuleNode.md)
 - [AnyOfAccessRuleNodeAllOf](docs/AnyOfAccessRuleNodeAllOf.md)
 - [AnyOfProofRule](docs/AnyOfProofRule.md)
 - [AuthConfig](docs/AuthConfig.md)
 - [BasicErrorResponse](docs/BasicErrorResponse.md)
 - [BinaryPlaintextMessageContent](docs/BinaryPlaintextMessageContent.md)
 - [BinaryPlaintextMessageContentAllOf](docs/BinaryPlaintextMessageContentAllOf.md)
 - [BlueprintCollectionSchema](docs/BlueprintCollectionSchema.md)
 - [BlueprintCollectionSchemaType](docs/BlueprintCollectionSchemaType.md)
 - [BlueprintDefinition](docs/BlueprintDefinition.md)
 - [BlueprintDependencies](docs/BlueprintDependencies.md)
 - [BlueprintFunctionTargetIdentifier](docs/BlueprintFunctionTargetIdentifier.md)
 - [BlueprintFunctionTargetIdentifierAllOf](docs/BlueprintFunctionTargetIdentifierAllOf.md)
 - [BlueprintInterface](docs/BlueprintInterface.md)
 - [BlueprintMethodRoyalty](docs/BlueprintMethodRoyalty.md)
 - [BlueprintRoyaltyConfig](docs/BlueprintRoyaltyConfig.md)
 - [BlueprintSchemaBlueprintTypeReference](docs/BlueprintSchemaBlueprintTypeReference.md)
 - [BlueprintSchemaBlueprintTypeReferenceAllOf](docs/BlueprintSchemaBlueprintTypeReferenceAllOf.md)
 - [BlueprintSchemaCollectionPartition](docs/BlueprintSchemaCollectionPartition.md)
 - [BlueprintSchemaFieldPartition](docs/BlueprintSchemaFieldPartition.md)
 - [BlueprintTypeReference](docs/BlueprintTypeReference.md)
 - [BlueprintTypeReferenceKind](docs/BlueprintTypeReferenceKind.md)
 - [BlueprintVersionKey](docs/BlueprintVersionKey.md)
 - [CodeHash](docs/CodeHash.md)
 - [CommittedStateIdentifier](docs/CommittedStateIdentifier.md)
 - [CommittedTransaction](docs/CommittedTransaction.md)
 - [ComponentMethodTargetIdentifier](docs/ComponentMethodTargetIdentifier.md)
 - [ComponentMethodTargetIdentifierAllOf](docs/ComponentMethodTargetIdentifierAllOf.md)
 - [ConsensusManagerFieldConfigSubstate](docs/ConsensusManagerFieldConfigSubstate.md)
 - [ConsensusManagerFieldConfigSubstateAllOf](docs/ConsensusManagerFieldConfigSubstateAllOf.md)
 - [ConsensusManagerFieldConfigValue](docs/ConsensusManagerFieldConfigValue.md)
 - [ConsensusManagerFieldCurrentProposalStatisticSubstate](docs/ConsensusManagerFieldCurrentProposalStatisticSubstate.md)
 - [ConsensusManagerFieldCurrentProposalStatisticSubstateAllOf](docs/ConsensusManagerFieldCurrentProposalStatisticSubstateAllOf.md)
 - [ConsensusManagerFieldCurrentProposalStatisticValue](docs/ConsensusManagerFieldCurrentProposalStatisticValue.md)
 - [ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate](docs/ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate.md)
 - [ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstateAllOf](docs/ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstateAllOf.md)
 - [ConsensusManagerFieldCurrentTimeRoundedToMinutesValue](docs/ConsensusManagerFieldCurrentTimeRoundedToMinutesValue.md)
 - [ConsensusManagerFieldCurrentTimeSubstate](docs/ConsensusManagerFieldCurrentTimeSubstate.md)
 - [ConsensusManagerFieldCurrentTimeSubstateAllOf](docs/ConsensusManagerFieldCurrentTimeSubstateAllOf.md)
 - [ConsensusManagerFieldCurrentTimeValue](docs/ConsensusManagerFieldCurrentTimeValue.md)
 - [ConsensusManagerFieldCurrentValidatorSetSubstate](docs/ConsensusManagerFieldCurrentValidatorSetSubstate.md)
 - [ConsensusManagerFieldCurrentValidatorSetSubstateAllOf](docs/ConsensusManagerFieldCurrentValidatorSetSubstateAllOf.md)
 - [ConsensusManagerFieldCurrentValidatorSetValue](docs/ConsensusManagerFieldCurrentValidatorSetValue.md)
 - [ConsensusManagerFieldStateSubstate](docs/ConsensusManagerFieldStateSubstate.md)
 - [ConsensusManagerFieldStateSubstateAllOf](docs/ConsensusManagerFieldStateSubstateAllOf.md)
 - [ConsensusManagerFieldStateValue](docs/ConsensusManagerFieldStateValue.md)
 - [ConsensusManagerFieldValidatorRewardsSubstate](docs/ConsensusManagerFieldValidatorRewardsSubstate.md)
 - [ConsensusManagerFieldValidatorRewardsSubstateAllOf](docs/ConsensusManagerFieldValidatorRewardsSubstateAllOf.md)
 - [ConsensusManagerFieldValidatorRewardsValue](docs/ConsensusManagerFieldValidatorRewardsValue.md)
 - [ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstate](docs/ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstate.md)
 - [ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstateAllOf](docs/ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstateAllOf.md)
 - [ConsensusManagerRegisteredValidatorsByStakeIndexEntryValue](docs/ConsensusManagerRegisteredValidatorsByStakeIndexEntryValue.md)
 - [CountOfProofRule](docs/CountOfProofRule.md)
 - [CountOfProofRuleAllOf](docs/CountOfProofRuleAllOf.md)
 - [CreatedSubstate](docs/CreatedSubstate.md)
 - [DataStruct](docs/DataStruct.md)
 - [DefaultDepositRule](docs/DefaultDepositRule.md)
 - [DeletedSubstate](docs/DeletedSubstate.md)
 - [DenyAllAccessRule](docs/DenyAllAccessRule.md)
 - [DepositRule](docs/DepositRule.md)
 - [EcdsaSecp256k1PublicKey](docs/EcdsaSecp256k1PublicKey.md)
 - [EcdsaSecp256k1PublicKeyAllOf](docs/EcdsaSecp256k1PublicKeyAllOf.md)
 - [EcdsaSecp256k1Signature](docs/EcdsaSecp256k1Signature.md)
 - [EcdsaSecp256k1SignatureAllOf](docs/EcdsaSecp256k1SignatureAllOf.md)
 - [EcdsaSecp256k1SignatureWithPublicKey](docs/EcdsaSecp256k1SignatureWithPublicKey.md)
 - [EcdsaSecp256k1SignatureWithPublicKeyAllOf](docs/EcdsaSecp256k1SignatureWithPublicKeyAllOf.md)
 - [EddsaEd25519PublicKey](docs/EddsaEd25519PublicKey.md)
 - [EddsaEd25519PublicKeyAllOf](docs/EddsaEd25519PublicKeyAllOf.md)
 - [EddsaEd25519Signature](docs/EddsaEd25519Signature.md)
 - [EddsaEd25519SignatureAllOf](docs/EddsaEd25519SignatureAllOf.md)
 - [EddsaEd25519SignatureWithPublicKey](docs/EddsaEd25519SignatureWithPublicKey.md)
 - [EddsaEd25519SignatureWithPublicKeyAllOf](docs/EddsaEd25519SignatureWithPublicKeyAllOf.md)
 - [EncryptedMessageCurveDecryptorSet](docs/EncryptedMessageCurveDecryptorSet.md)
 - [EncryptedMessageDecryptor](docs/EncryptedMessageDecryptor.md)
 - [EncryptedTransactionMessage](docs/EncryptedTransactionMessage.md)
 - [EncryptedTransactionMessageAllOf](docs/EncryptedTransactionMessageAllOf.md)
 - [EntityModule](docs/EntityModule.md)
 - [EntityReference](docs/EntityReference.md)
 - [EntityType](docs/EntityType.md)
 - [EpochChangeCondition](docs/EpochChangeCondition.md)
 - [EpochRound](docs/EpochRound.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ErrorResponseType](docs/ErrorResponseType.md)
 - [Event](docs/Event.md)
 - [EventEmitterIdentifier](docs/EventEmitterIdentifier.md)
 - [EventEmitterIdentifierType](docs/EventEmitterIdentifierType.md)
 - [EventTypeIdentifier](docs/EventTypeIdentifier.md)
 - [ExecutedGenesisScenario](docs/ExecutedGenesisScenario.md)
 - [ExecutedScenarioTransaction](docs/ExecutedScenarioTransaction.md)
 - [FeeSummary](docs/FeeSummary.md)
 - [FieldSchema](docs/FieldSchema.md)
 - [FieldSchemaFeatureCondition](docs/FieldSchemaFeatureCondition.md)
 - [FieldSchemaFeatureConditionAlways](docs/FieldSchemaFeatureConditionAlways.md)
 - [FieldSchemaFeatureConditionIfOuterObjectFeature](docs/FieldSchemaFeatureConditionIfOuterObjectFeature.md)
 - [FieldSchemaFeatureConditionIfOwnFeature](docs/FieldSchemaFeatureConditionIfOwnFeature.md)
 - [FieldSchemaFeatureConditionIfOwnFeatureAllOf](docs/FieldSchemaFeatureConditionIfOwnFeatureAllOf.md)
 - [FieldSchemaFeatureConditionType](docs/FieldSchemaFeatureConditionType.md)
 - [FieldSubstateKey](docs/FieldSubstateKey.md)
 - [FieldSubstateKeyAllOf](docs/FieldSubstateKeyAllOf.md)
 - [FrozenStatus](docs/FrozenStatus.md)
 - [FunctionAuthType](docs/FunctionAuthType.md)
 - [FunctionEventEmitterIdentifier](docs/FunctionEventEmitterIdentifier.md)
 - [FunctionEventEmitterIdentifierAllOf](docs/FunctionEventEmitterIdentifierAllOf.md)
 - [FunctionSchema](docs/FunctionSchema.md)
 - [FungibleResourceAmount](docs/FungibleResourceAmount.md)
 - [FungibleResourceAmountAllOf](docs/FungibleResourceAmountAllOf.md)
 - [FungibleResourceManagerFieldDivisibilitySubstate](docs/FungibleResourceManagerFieldDivisibilitySubstate.md)
 - [FungibleResourceManagerFieldDivisibilitySubstateAllOf](docs/FungibleResourceManagerFieldDivisibilitySubstateAllOf.md)
 - [FungibleResourceManagerFieldDivisibilityValue](docs/FungibleResourceManagerFieldDivisibilityValue.md)
 - [FungibleResourceManagerFieldTotalSupplySubstate](docs/FungibleResourceManagerFieldTotalSupplySubstate.md)
 - [FungibleResourceManagerFieldTotalSupplySubstateAllOf](docs/FungibleResourceManagerFieldTotalSupplySubstateAllOf.md)
 - [FungibleResourceManagerFieldTotalSupplyValue](docs/FungibleResourceManagerFieldTotalSupplyValue.md)
 - [FungibleVaultFieldBalanceSubstate](docs/FungibleVaultFieldBalanceSubstate.md)
 - [FungibleVaultFieldBalanceSubstateAllOf](docs/FungibleVaultFieldBalanceSubstateAllOf.md)
 - [FungibleVaultFieldBalanceValue](docs/FungibleVaultFieldBalanceValue.md)
 - [FungibleVaultFieldFrozenStatusSubstate](docs/FungibleVaultFieldFrozenStatusSubstate.md)
 - [FungibleVaultFieldFrozenStatusSubstateAllOf](docs/FungibleVaultFieldFrozenStatusSubstateAllOf.md)
 - [FungibleVaultFieldFrozenStatusValue](docs/FungibleVaultFieldFrozenStatusValue.md)
 - [GenericKey](docs/GenericKey.md)
 - [GenericKeyValueStoreEntrySubstate](docs/GenericKeyValueStoreEntrySubstate.md)
 - [GenericKeyValueStoreEntrySubstateAllOf](docs/GenericKeyValueStoreEntrySubstateAllOf.md)
 - [GenericKeyValueStoreEntryValue](docs/GenericKeyValueStoreEntryValue.md)
 - [GenericScryptoComponentFieldStateSubstate](docs/GenericScryptoComponentFieldStateSubstate.md)
 - [GenericScryptoComponentFieldStateSubstateAllOf](docs/GenericScryptoComponentFieldStateSubstateAllOf.md)
 - [GenericScryptoComponentFieldStateValue](docs/GenericScryptoComponentFieldStateValue.md)
 - [GenericTypeParameter](docs/GenericTypeParameter.md)
 - [GenericTypeParameterContraints](docs/GenericTypeParameterContraints.md)
 - [GenesisLedgerTransaction](docs/GenesisLedgerTransaction.md)
 - [GenesisLedgerTransactionAllOf](docs/GenesisLedgerTransactionAllOf.md)
 - [IndexBlueprintCollectionSchema](docs/IndexBlueprintCollectionSchema.md)
 - [IndexedStateSchema](docs/IndexedStateSchema.md)
 - [InstanceSchema](docs/InstanceSchema.md)
 - [InstanceSchemaBlueprintTypeReference](docs/InstanceSchemaBlueprintTypeReference.md)
 - [InstanceSchemaBlueprintTypeReferenceAllOf](docs/InstanceSchemaBlueprintTypeReferenceAllOf.md)
 - [InstanceTypePointer](docs/InstanceTypePointer.md)
 - [InstanceTypePointerAllOf](docs/InstanceTypePointerAllOf.md)
 - [Instant](docs/Instant.md)
 - [InstructionResourceChanges](docs/InstructionResourceChanges.md)
 - [IntentHash](docs/IntentHash.md)
 - [KeyValueBlueprintCollectionSchema](docs/KeyValueBlueprintCollectionSchema.md)
 - [KeyValueBlueprintCollectionSchemaAllOf](docs/KeyValueBlueprintCollectionSchemaAllOf.md)
 - [KeyValueStoreInfo](docs/KeyValueStoreInfo.md)
 - [KeyValueStoreSchema](docs/KeyValueStoreSchema.md)
 - [KeyValueStoreTypeInfoDetails](docs/KeyValueStoreTypeInfoDetails.md)
 - [KeyValueStoreTypeInfoDetailsAllOf](docs/KeyValueStoreTypeInfoDetailsAllOf.md)
 - [LeaderProposalHistory](docs/LeaderProposalHistory.md)
 - [LedgerPayloadHash](docs/LedgerPayloadHash.md)
 - [LedgerTransaction](docs/LedgerTransaction.md)
 - [LedgerTransactionType](docs/LedgerTransactionType.md)
 - [LocalNonFungibleKey](docs/LocalNonFungibleKey.md)
 - [LocalTypeIndex](docs/LocalTypeIndex.md)
 - [LtsCommittedTransactionOutcome](docs/LtsCommittedTransactionOutcome.md)
 - [LtsCommittedTransactionStatus](docs/LtsCommittedTransactionStatus.md)
 - [LtsEntityFungibleBalanceChanges](docs/LtsEntityFungibleBalanceChanges.md)
 - [LtsFeeFungibleResourceBalanceChange](docs/LtsFeeFungibleResourceBalanceChange.md)
 - [LtsFeeFungibleResourceBalanceChangeType](docs/LtsFeeFungibleResourceBalanceChangeType.md)
 - [LtsFungibleResourceBalance](docs/LtsFungibleResourceBalance.md)
 - [LtsFungibleResourceBalanceChange](docs/LtsFungibleResourceBalanceChange.md)
 - [LtsResultantAccountFungibleBalances](docs/LtsResultantAccountFungibleBalances.md)
 - [LtsResultantFungibleBalance](docs/LtsResultantFungibleBalance.md)
 - [LtsStateAccountAllFungibleResourceBalancesRequest](docs/LtsStateAccountAllFungibleResourceBalancesRequest.md)
 - [LtsStateAccountAllFungibleResourceBalancesResponse](docs/LtsStateAccountAllFungibleResourceBalancesResponse.md)
 - [LtsStateAccountFungibleResourceBalanceRequest](docs/LtsStateAccountFungibleResourceBalanceRequest.md)
 - [LtsStateAccountFungibleResourceBalanceResponse](docs/LtsStateAccountFungibleResourceBalanceResponse.md)
 - [LtsStreamAccountTransactionOutcomesRequest](docs/LtsStreamAccountTransactionOutcomesRequest.md)
 - [LtsStreamAccountTransactionOutcomesResponse](docs/LtsStreamAccountTransactionOutcomesResponse.md)
 - [LtsStreamTransactionOutcomesRequest](docs/LtsStreamTransactionOutcomesRequest.md)
 - [LtsStreamTransactionOutcomesResponse](docs/LtsStreamTransactionOutcomesResponse.md)
 - [LtsTransactionConstructionRequest](docs/LtsTransactionConstructionRequest.md)
 - [LtsTransactionConstructionResponse](docs/LtsTransactionConstructionResponse.md)
 - [LtsTransactionIntentStatus](docs/LtsTransactionIntentStatus.md)
 - [LtsTransactionPayloadDetails](docs/LtsTransactionPayloadDetails.md)
 - [LtsTransactionPayloadStatus](docs/LtsTransactionPayloadStatus.md)
 - [LtsTransactionStatusRequest](docs/LtsTransactionStatusRequest.md)
 - [LtsTransactionStatusResponse](docs/LtsTransactionStatusResponse.md)
 - [LtsTransactionSubmitErrorDetails](docs/LtsTransactionSubmitErrorDetails.md)
 - [LtsTransactionSubmitErrorDetailsType](docs/LtsTransactionSubmitErrorDetailsType.md)
 - [LtsTransactionSubmitErrorResponse](docs/LtsTransactionSubmitErrorResponse.md)
 - [LtsTransactionSubmitErrorResponseAllOf](docs/LtsTransactionSubmitErrorResponseAllOf.md)
 - [LtsTransactionSubmitPriorityThresholdNotMetErrorDetails](docs/LtsTransactionSubmitPriorityThresholdNotMetErrorDetails.md)
 - [LtsTransactionSubmitPriorityThresholdNotMetErrorDetailsAllOf](docs/LtsTransactionSubmitPriorityThresholdNotMetErrorDetailsAllOf.md)
 - [LtsTransactionSubmitRejectedErrorDetails](docs/LtsTransactionSubmitRejectedErrorDetails.md)
 - [LtsTransactionSubmitRejectedErrorDetailsAllOf](docs/LtsTransactionSubmitRejectedErrorDetailsAllOf.md)
 - [LtsTransactionSubmitRequest](docs/LtsTransactionSubmitRequest.md)
 - [LtsTransactionSubmitResponse](docs/LtsTransactionSubmitResponse.md)
 - [MainMethodKey](docs/MainMethodKey.md)
 - [MapSubstateKey](docs/MapSubstateKey.md)
 - [MapSubstateKeyAllOf](docs/MapSubstateKeyAllOf.md)
 - [MempoolListRequest](docs/MempoolListRequest.md)
 - [MempoolListResponse](docs/MempoolListResponse.md)
 - [MempoolTransactionHashes](docs/MempoolTransactionHashes.md)
 - [MempoolTransactionRequest](docs/MempoolTransactionRequest.md)
 - [MempoolTransactionResponse](docs/MempoolTransactionResponse.md)
 - [MetadataKey](docs/MetadataKey.md)
 - [MetadataModuleEntrySubstate](docs/MetadataModuleEntrySubstate.md)
 - [MetadataModuleEntrySubstateAllOf](docs/MetadataModuleEntrySubstateAllOf.md)
 - [MetadataModuleEntryValue](docs/MetadataModuleEntryValue.md)
 - [MethodAccessibility](docs/MethodAccessibility.md)
 - [MethodAccessibilityType](docs/MethodAccessibilityType.md)
 - [MethodAuthType](docs/MethodAuthType.md)
 - [MethodEventEmitterIdentifier](docs/MethodEventEmitterIdentifier.md)
 - [MethodEventEmitterIdentifierAllOf](docs/MethodEventEmitterIdentifierAllOf.md)
 - [MultiResourcePoolFieldStateSubstate](docs/MultiResourcePoolFieldStateSubstate.md)
 - [MultiResourcePoolFieldStateSubstateAllOf](docs/MultiResourcePoolFieldStateSubstateAllOf.md)
 - [MultiResourcePoolFieldStateValue](docs/MultiResourcePoolFieldStateValue.md)
 - [NetworkConfigurationResponse](docs/NetworkConfigurationResponse.md)
 - [NetworkConfigurationResponseVersion](docs/NetworkConfigurationResponseVersion.md)
 - [NetworkConfigurationResponseWellKnownAddresses](docs/NetworkConfigurationResponseWellKnownAddresses.md)
 - [NetworkIdentifierByte](docs/NetworkIdentifierByte.md)
 - [NetworkStatusRequest](docs/NetworkStatusRequest.md)
 - [NetworkStatusResponse](docs/NetworkStatusResponse.md)
 - [NextEpoch](docs/NextEpoch.md)
 - [NonFungibleGlobalId](docs/NonFungibleGlobalId.md)
 - [NonFungibleIdType](docs/NonFungibleIdType.md)
 - [NonFungibleLocalId](docs/NonFungibleLocalId.md)
 - [NonFungibleRequirement](docs/NonFungibleRequirement.md)
 - [NonFungibleRequirementAllOf](docs/NonFungibleRequirementAllOf.md)
 - [NonFungibleResourceAmount](docs/NonFungibleResourceAmount.md)
 - [NonFungibleResourceAmountAllOf](docs/NonFungibleResourceAmountAllOf.md)
 - [NonFungibleResourceManagerDataEntrySubstate](docs/NonFungibleResourceManagerDataEntrySubstate.md)
 - [NonFungibleResourceManagerDataEntrySubstateAllOf](docs/NonFungibleResourceManagerDataEntrySubstateAllOf.md)
 - [NonFungibleResourceManagerDataEntryValue](docs/NonFungibleResourceManagerDataEntryValue.md)
 - [NonFungibleResourceManagerFieldIdTypeSubstate](docs/NonFungibleResourceManagerFieldIdTypeSubstate.md)
 - [NonFungibleResourceManagerFieldIdTypeSubstateAllOf](docs/NonFungibleResourceManagerFieldIdTypeSubstateAllOf.md)
 - [NonFungibleResourceManagerFieldIdTypeValue](docs/NonFungibleResourceManagerFieldIdTypeValue.md)
 - [NonFungibleResourceManagerFieldMutableFieldsSubstate](docs/NonFungibleResourceManagerFieldMutableFieldsSubstate.md)
 - [NonFungibleResourceManagerFieldMutableFieldsSubstateAllOf](docs/NonFungibleResourceManagerFieldMutableFieldsSubstateAllOf.md)
 - [NonFungibleResourceManagerFieldMutableFieldsValue](docs/NonFungibleResourceManagerFieldMutableFieldsValue.md)
 - [NonFungibleResourceManagerFieldTotalSupplySubstate](docs/NonFungibleResourceManagerFieldTotalSupplySubstate.md)
 - [NonFungibleResourceManagerFieldTotalSupplySubstateAllOf](docs/NonFungibleResourceManagerFieldTotalSupplySubstateAllOf.md)
 - [NonFungibleResourceManagerFieldTotalSupplyValue](docs/NonFungibleResourceManagerFieldTotalSupplyValue.md)
 - [NonFungibleVaultContentsIndexEntrySubstate](docs/NonFungibleVaultContentsIndexEntrySubstate.md)
 - [NonFungibleVaultContentsIndexEntrySubstateAllOf](docs/NonFungibleVaultContentsIndexEntrySubstateAllOf.md)
 - [NonFungibleVaultContentsIndexEntryValue](docs/NonFungibleVaultContentsIndexEntryValue.md)
 - [NonFungibleVaultFieldBalanceSubstate](docs/NonFungibleVaultFieldBalanceSubstate.md)
 - [NonFungibleVaultFieldBalanceSubstateAllOf](docs/NonFungibleVaultFieldBalanceSubstateAllOf.md)
 - [NonFungibleVaultFieldBalanceValue](docs/NonFungibleVaultFieldBalanceValue.md)
 - [NonFungibleVaultFieldFrozenStatusSubstate](docs/NonFungibleVaultFieldFrozenStatusSubstate.md)
 - [NonFungibleVaultFieldFrozenStatusSubstateAllOf](docs/NonFungibleVaultFieldFrozenStatusSubstateAllOf.md)
 - [NonFungibleVaultFieldFrozenStatusValue](docs/NonFungibleVaultFieldFrozenStatusValue.md)
 - [NotarizedTransaction](docs/NotarizedTransaction.md)
 - [NotarizedTransactionHash](docs/NotarizedTransactionHash.md)
 - [ObjectModuleId](docs/ObjectModuleId.md)
 - [ObjectRoleKey](docs/ObjectRoleKey.md)
 - [ObjectTypeInfoDetails](docs/ObjectTypeInfoDetails.md)
 - [ObjectTypeInfoDetailsAllOf](docs/ObjectTypeInfoDetailsAllOf.md)
 - [OneResourcePoolFieldStateSubstate](docs/OneResourcePoolFieldStateSubstate.md)
 - [OneResourcePoolFieldStateSubstateAllOf](docs/OneResourcePoolFieldStateSubstateAllOf.md)
 - [OneResourcePoolFieldStateValue](docs/OneResourcePoolFieldStateValue.md)
 - [OuterObjectOnlyMethodAccessibility](docs/OuterObjectOnlyMethodAccessibility.md)
 - [OwnPackageOnlyMethodAccessibility](docs/OwnPackageOnlyMethodAccessibility.md)
 - [OwnerRole](docs/OwnerRole.md)
 - [OwnerRoleUpdater](docs/OwnerRoleUpdater.md)
 - [PackageBlueprintAuthTemplateEntrySubstate](docs/PackageBlueprintAuthTemplateEntrySubstate.md)
 - [PackageBlueprintAuthTemplateEntrySubstateAllOf](docs/PackageBlueprintAuthTemplateEntrySubstateAllOf.md)
 - [PackageBlueprintAuthTemplateEntryValue](docs/PackageBlueprintAuthTemplateEntryValue.md)
 - [PackageBlueprintDefinitionEntrySubstate](docs/PackageBlueprintDefinitionEntrySubstate.md)
 - [PackageBlueprintDefinitionEntrySubstateAllOf](docs/PackageBlueprintDefinitionEntrySubstateAllOf.md)
 - [PackageBlueprintDefinitionEntryValue](docs/PackageBlueprintDefinitionEntryValue.md)
 - [PackageBlueprintDependenciesEntrySubstate](docs/PackageBlueprintDependenciesEntrySubstate.md)
 - [PackageBlueprintDependenciesEntrySubstateAllOf](docs/PackageBlueprintDependenciesEntrySubstateAllOf.md)
 - [PackageBlueprintDependenciesEntryValue](docs/PackageBlueprintDependenciesEntryValue.md)
 - [PackageBlueprintRoyaltyEntrySubstate](docs/PackageBlueprintRoyaltyEntrySubstate.md)
 - [PackageBlueprintRoyaltyEntrySubstateAllOf](docs/PackageBlueprintRoyaltyEntrySubstateAllOf.md)
 - [PackageBlueprintRoyaltyEntryValue](docs/PackageBlueprintRoyaltyEntryValue.md)
 - [PackageCodeInstrumentedCodeEntrySubstate](docs/PackageCodeInstrumentedCodeEntrySubstate.md)
 - [PackageCodeInstrumentedCodeEntrySubstateAllOf](docs/PackageCodeInstrumentedCodeEntrySubstateAllOf.md)
 - [PackageCodeInstrumentedCodeEntryValue](docs/PackageCodeInstrumentedCodeEntryValue.md)
 - [PackageCodeKey](docs/PackageCodeKey.md)
 - [PackageCodeOriginalCodeEntrySubstate](docs/PackageCodeOriginalCodeEntrySubstate.md)
 - [PackageCodeOriginalCodeEntrySubstateAllOf](docs/PackageCodeOriginalCodeEntrySubstateAllOf.md)
 - [PackageCodeOriginalCodeEntryValue](docs/PackageCodeOriginalCodeEntryValue.md)
 - [PackageCodeVmTypeEntrySubstate](docs/PackageCodeVmTypeEntrySubstate.md)
 - [PackageCodeVmTypeEntrySubstateAllOf](docs/PackageCodeVmTypeEntrySubstateAllOf.md)
 - [PackageCodeVmTypeEntryValue](docs/PackageCodeVmTypeEntryValue.md)
 - [PackageExport](docs/PackageExport.md)
 - [PackageFieldRoyaltyAccumulatorSubstate](docs/PackageFieldRoyaltyAccumulatorSubstate.md)
 - [PackageFieldRoyaltyAccumulatorSubstateAllOf](docs/PackageFieldRoyaltyAccumulatorSubstateAllOf.md)
 - [PackageFieldRoyaltyAccumulatorValue](docs/PackageFieldRoyaltyAccumulatorValue.md)
 - [PackageSchemaEntrySubstate](docs/PackageSchemaEntrySubstate.md)
 - [PackageSchemaEntrySubstateAllOf](docs/PackageSchemaEntrySubstateAllOf.md)
 - [PackageSchemaEntryValue](docs/PackageSchemaEntryValue.md)
 - [PackageTypePointer](docs/PackageTypePointer.md)
 - [PackageTypePointerAllOf](docs/PackageTypePointerAllOf.md)
 - [ParsedLedgerTransaction](docs/ParsedLedgerTransaction.md)
 - [ParsedLedgerTransactionAllOf](docs/ParsedLedgerTransactionAllOf.md)
 - [ParsedLedgerTransactionIdentifiers](docs/ParsedLedgerTransactionIdentifiers.md)
 - [ParsedNotarizedTransaction](docs/ParsedNotarizedTransaction.md)
 - [ParsedNotarizedTransactionAllOf](docs/ParsedNotarizedTransactionAllOf.md)
 - [ParsedNotarizedTransactionAllOfValidationError](docs/ParsedNotarizedTransactionAllOfValidationError.md)
 - [ParsedNotarizedTransactionIdentifiers](docs/ParsedNotarizedTransactionIdentifiers.md)
 - [ParsedSignedTransactionIntent](docs/ParsedSignedTransactionIntent.md)
 - [ParsedSignedTransactionIntentAllOf](docs/ParsedSignedTransactionIntentAllOf.md)
 - [ParsedSignedTransactionIntentIdentifiers](docs/ParsedSignedTransactionIntentIdentifiers.md)
 - [ParsedTransaction](docs/ParsedTransaction.md)
 - [ParsedTransactionIntent](docs/ParsedTransactionIntent.md)
 - [ParsedTransactionIntentAllOf](docs/ParsedTransactionIntentAllOf.md)
 - [ParsedTransactionIntentIdentifiers](docs/ParsedTransactionIntentIdentifiers.md)
 - [ParsedTransactionType](docs/ParsedTransactionType.md)
 - [PartitionKind](docs/PartitionKind.md)
 - [PendingOwnerStakeWithdrawal](docs/PendingOwnerStakeWithdrawal.md)
 - [PlaintextMessageContent](docs/PlaintextMessageContent.md)
 - [PlaintextMessageContentType](docs/PlaintextMessageContentType.md)
 - [PlaintextTransactionMessage](docs/PlaintextTransactionMessage.md)
 - [PlaintextTransactionMessageAllOf](docs/PlaintextTransactionMessageAllOf.md)
 - [PoolVault](docs/PoolVault.md)
 - [ProofAccessRuleNode](docs/ProofAccessRuleNode.md)
 - [ProofAccessRuleNodeAllOf](docs/ProofAccessRuleNodeAllOf.md)
 - [ProofRule](docs/ProofRule.md)
 - [ProofRuleType](docs/ProofRuleType.md)
 - [ProposerReward](docs/ProposerReward.md)
 - [ProtectedAccessRule](docs/ProtectedAccessRule.md)
 - [ProtectedAccessRuleAllOf](docs/ProtectedAccessRuleAllOf.md)
 - [PublicKey](docs/PublicKey.md)
 - [PublicKeyType](docs/PublicKeyType.md)
 - [PublicMethodAccessibility](docs/PublicMethodAccessibility.md)
 - [ReceiverInfo](docs/ReceiverInfo.md)
 - [ReferenceType](docs/ReferenceType.md)
 - [RequireProofRule](docs/RequireProofRule.md)
 - [RequireProofRuleAllOf](docs/RequireProofRuleAllOf.md)
 - [Requirement](docs/Requirement.md)
 - [RequirementType](docs/RequirementType.md)
 - [ResourceAmount](docs/ResourceAmount.md)
 - [ResourceChange](docs/ResourceChange.md)
 - [ResourceKey](docs/ResourceKey.md)
 - [ResourceRequirement](docs/ResourceRequirement.md)
 - [ResourceRequirementAllOf](docs/ResourceRequirementAllOf.md)
 - [ResourceType](docs/ResourceType.md)
 - [RoleDetails](docs/RoleDetails.md)
 - [RoleProtectedMethodAccessibility](docs/RoleProtectedMethodAccessibility.md)
 - [RoleProtectedMethodAccessibilityAllOf](docs/RoleProtectedMethodAccessibilityAllOf.md)
 - [RoleSpecification](docs/RoleSpecification.md)
 - [RoundUpdateLedgerTransaction](docs/RoundUpdateLedgerTransaction.md)
 - [RoundUpdateLedgerTransactionAllOf](docs/RoundUpdateLedgerTransactionAllOf.md)
 - [RoundUpdateTransaction](docs/RoundUpdateTransaction.md)
 - [RoyaltyAmount](docs/RoyaltyAmount.md)
 - [RoyaltyModuleFieldStateSubstate](docs/RoyaltyModuleFieldStateSubstate.md)
 - [RoyaltyModuleFieldStateSubstateAllOf](docs/RoyaltyModuleFieldStateSubstateAllOf.md)
 - [RoyaltyModuleFieldStateValue](docs/RoyaltyModuleFieldStateValue.md)
 - [RoyaltyModuleMethodRoyaltyEntrySubstate](docs/RoyaltyModuleMethodRoyaltyEntrySubstate.md)
 - [RoyaltyModuleMethodRoyaltyEntrySubstateAllOf](docs/RoyaltyModuleMethodRoyaltyEntrySubstateAllOf.md)
 - [RoyaltyModuleMethodRoyaltyEntryValue](docs/RoyaltyModuleMethodRoyaltyEntryValue.md)
 - [RoyaltyPayment](docs/RoyaltyPayment.md)
 - [SborData](docs/SborData.md)
 - [SborFormatOptions](docs/SborFormatOptions.md)
 - [ScenariosRequest](docs/ScenariosRequest.md)
 - [ScenariosResponse](docs/ScenariosResponse.md)
 - [SchemaHash](docs/SchemaHash.md)
 - [SchemaKey](docs/SchemaKey.md)
 - [ScryptoSchema](docs/ScryptoSchema.md)
 - [Signature](docs/Signature.md)
 - [SignatureWithPublicKey](docs/SignatureWithPublicKey.md)
 - [SignedIntentHash](docs/SignedIntentHash.md)
 - [SignedTransactionIntent](docs/SignedTransactionIntent.md)
 - [SortedIndexBlueprintCollectionSchema](docs/SortedIndexBlueprintCollectionSchema.md)
 - [SortedSubstateKey](docs/SortedSubstateKey.md)
 - [SortedSubstateKeyAllOf](docs/SortedSubstateKeyAllOf.md)
 - [StateAccessControllerRequest](docs/StateAccessControllerRequest.md)
 - [StateAccessControllerResponse](docs/StateAccessControllerResponse.md)
 - [StateAccountRequest](docs/StateAccountRequest.md)
 - [StateAccountResponse](docs/StateAccountResponse.md)
 - [StateComponentDescendentNode](docs/StateComponentDescendentNode.md)
 - [StateComponentRequest](docs/StateComponentRequest.md)
 - [StateComponentResponse](docs/StateComponentResponse.md)
 - [StateConsensusManagerRequest](docs/StateConsensusManagerRequest.md)
 - [StateConsensusManagerResponse](docs/StateConsensusManagerResponse.md)
 - [StateFungibleResourceManager](docs/StateFungibleResourceManager.md)
 - [StateFungibleResourceManagerAllOf](docs/StateFungibleResourceManagerAllOf.md)
 - [StateNonFungibleRequest](docs/StateNonFungibleRequest.md)
 - [StateNonFungibleResourceManager](docs/StateNonFungibleResourceManager.md)
 - [StateNonFungibleResourceManagerAllOf](docs/StateNonFungibleResourceManagerAllOf.md)
 - [StateNonFungibleResponse](docs/StateNonFungibleResponse.md)
 - [StatePackageRequest](docs/StatePackageRequest.md)
 - [StatePackageResponse](docs/StatePackageResponse.md)
 - [StateResourceManager](docs/StateResourceManager.md)
 - [StateResourceRequest](docs/StateResourceRequest.md)
 - [StateResourceResponse](docs/StateResourceResponse.md)
 - [StateUpdates](docs/StateUpdates.md)
 - [StateValidatorRequest](docs/StateValidatorRequest.md)
 - [StateValidatorResponse](docs/StateValidatorResponse.md)
 - [StateVersion](docs/StateVersion.md)
 - [StaticRolesAuthTemplate](docs/StaticRolesAuthTemplate.md)
 - [StreamTransactionsRequest](docs/StreamTransactionsRequest.md)
 - [StreamTransactionsResponse](docs/StreamTransactionsResponse.md)
 - [StringPlaintextMessageContent](docs/StringPlaintextMessageContent.md)
 - [StringPlaintextMessageContentAllOf](docs/StringPlaintextMessageContentAllOf.md)
 - [Substate](docs/Substate.md)
 - [SubstateFormatOptions](docs/SubstateFormatOptions.md)
 - [SubstateId](docs/SubstateId.md)
 - [SubstateKey](docs/SubstateKey.md)
 - [SubstateKeyType](docs/SubstateKeyType.md)
 - [SubstateType](docs/SubstateType.md)
 - [SubstateValue](docs/SubstateValue.md)
 - [SystemTransaction](docs/SystemTransaction.md)
 - [TargetIdentifier](docs/TargetIdentifier.md)
 - [TargetIdentifierType](docs/TargetIdentifierType.md)
 - [TransactionCallPreviewRequest](docs/TransactionCallPreviewRequest.md)
 - [TransactionCallPreviewResponse](docs/TransactionCallPreviewResponse.md)
 - [TransactionFormatOptions](docs/TransactionFormatOptions.md)
 - [TransactionHeader](docs/TransactionHeader.md)
 - [TransactionIdKey](docs/TransactionIdKey.md)
 - [TransactionIdentifiers](docs/TransactionIdentifiers.md)
 - [TransactionIntent](docs/TransactionIntent.md)
 - [TransactionIntentStatus](docs/TransactionIntentStatus.md)
 - [TransactionMessage](docs/TransactionMessage.md)
 - [TransactionMessageType](docs/TransactionMessageType.md)
 - [TransactionParseRequest](docs/TransactionParseRequest.md)
 - [TransactionParseResponse](docs/TransactionParseResponse.md)
 - [TransactionPayloadStatus](docs/TransactionPayloadStatus.md)
 - [TransactionPreviewRequest](docs/TransactionPreviewRequest.md)
 - [TransactionPreviewRequestFlags](docs/TransactionPreviewRequestFlags.md)
 - [TransactionPreviewResponse](docs/TransactionPreviewResponse.md)
 - [TransactionPreviewResponseLogs](docs/TransactionPreviewResponseLogs.md)
 - [TransactionReceipt](docs/TransactionReceipt.md)
 - [TransactionReceiptRequest](docs/TransactionReceiptRequest.md)
 - [TransactionReceiptResponse](docs/TransactionReceiptResponse.md)
 - [TransactionStatus](docs/TransactionStatus.md)
 - [TransactionStatusRequest](docs/TransactionStatusRequest.md)
 - [TransactionStatusResponse](docs/TransactionStatusResponse.md)
 - [TransactionSubmitErrorDetails](docs/TransactionSubmitErrorDetails.md)
 - [TransactionSubmitErrorDetailsType](docs/TransactionSubmitErrorDetailsType.md)
 - [TransactionSubmitErrorResponse](docs/TransactionSubmitErrorResponse.md)
 - [TransactionSubmitErrorResponseAllOf](docs/TransactionSubmitErrorResponseAllOf.md)
 - [TransactionSubmitPriorityThresholdNotMetErrorDetails](docs/TransactionSubmitPriorityThresholdNotMetErrorDetails.md)
 - [TransactionSubmitRejectedErrorDetails](docs/TransactionSubmitRejectedErrorDetails.md)
 - [TransactionSubmitRequest](docs/TransactionSubmitRequest.md)
 - [TransactionSubmitResponse](docs/TransactionSubmitResponse.md)
 - [TransactionTrackerCollectionEntrySubstate](docs/TransactionTrackerCollectionEntrySubstate.md)
 - [TransactionTrackerCollectionEntrySubstateAllOf](docs/TransactionTrackerCollectionEntrySubstateAllOf.md)
 - [TransactionTrackerCollectionEntryValue](docs/TransactionTrackerCollectionEntryValue.md)
 - [TransactionTrackerFieldStateSubstate](docs/TransactionTrackerFieldStateSubstate.md)
 - [TransactionTrackerFieldStateSubstateAllOf](docs/TransactionTrackerFieldStateSubstateAllOf.md)
 - [TransactionTrackerFieldStateValue](docs/TransactionTrackerFieldStateValue.md)
 - [TransactionTrackerTransactionStatus](docs/TransactionTrackerTransactionStatus.md)
 - [TwoResourcePoolFieldStateSubstate](docs/TwoResourcePoolFieldStateSubstate.md)
 - [TwoResourcePoolFieldStateSubstateAllOf](docs/TwoResourcePoolFieldStateSubstateAllOf.md)
 - [TwoResourcePoolFieldStateValue](docs/TwoResourcePoolFieldStateValue.md)
 - [TypeInfoDetails](docs/TypeInfoDetails.md)
 - [TypeInfoModuleFieldTypeInfoSubstate](docs/TypeInfoModuleFieldTypeInfoSubstate.md)
 - [TypeInfoModuleFieldTypeInfoSubstateAllOf](docs/TypeInfoModuleFieldTypeInfoSubstateAllOf.md)
 - [TypeInfoModuleFieldTypeInfoValue](docs/TypeInfoModuleFieldTypeInfoValue.md)
 - [TypeInfoType](docs/TypeInfoType.md)
 - [TypePointer](docs/TypePointer.md)
 - [TypePointerType](docs/TypePointerType.md)
 - [UpdatedSubstate](docs/UpdatedSubstate.md)
 - [UserLedgerTransaction](docs/UserLedgerTransaction.md)
 - [UserLedgerTransactionAllOf](docs/UserLedgerTransactionAllOf.md)
 - [ValidatorFeeChangeRequest](docs/ValidatorFeeChangeRequest.md)
 - [ValidatorFieldProtocolUpdateReadinessSignalSubstate](docs/ValidatorFieldProtocolUpdateReadinessSignalSubstate.md)
 - [ValidatorFieldProtocolUpdateReadinessSignalSubstateAllOf](docs/ValidatorFieldProtocolUpdateReadinessSignalSubstateAllOf.md)
 - [ValidatorFieldProtocolUpdateReadinessSignalValue](docs/ValidatorFieldProtocolUpdateReadinessSignalValue.md)
 - [ValidatorFieldStateSubstate](docs/ValidatorFieldStateSubstate.md)
 - [ValidatorFieldStateSubstateAllOf](docs/ValidatorFieldStateSubstateAllOf.md)
 - [ValidatorFieldStateValue](docs/ValidatorFieldStateValue.md)
 - [VaultBalance](docs/VaultBalance.md)
 - [VaultPayment](docs/VaultPayment.md)
 - [VirtualLazyLoadSchema](docs/VirtualLazyLoadSchema.md)
 - [VmType](docs/VmType.md)


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

