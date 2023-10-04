# ValidatorFieldStateValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key** | [**EcdsaSecp256k1PublicKey**](EcdsaSecp256k1PublicKey.md) |  | 
**is_registered** | **bool** |  | 
**accepts_delegated_stake** | **bool** |  | 
**validator_fee_factor** | **str** | A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**stake_unit_resource_address** | **str** | The Bech32m-encoded human readable version of the resource address | 
**stake_xrd_vault** | [**EntityReference**](EntityReference.md) |  | 
**claim_token_resource_address** | **str** | The Bech32m-encoded human readable version of the resource address | 
**pending_xrd_withdraw_vault** | [**EntityReference**](EntityReference.md) |  | 
**locked_owner_stake_unit_vault** | [**EntityReference**](EntityReference.md) |  | 
**pending_owner_stake_unit_unlock_vault** | [**EntityReference**](EntityReference.md) |  | 
**pending_owner_stake_unit_withdrawals** | [**[PendingOwnerStakeWithdrawal]**](PendingOwnerStakeWithdrawal.md) |  | 
**already_unlocked_owner_stake_unit_amount** | **str** | A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**sorted_key** | [**SubstateKey**](SubstateKey.md) |  | [optional] 
**validator_fee_change_request** | [**ValidatorFeeChangeRequest**](ValidatorFeeChangeRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


