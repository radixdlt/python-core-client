# LtsEntityFungibleBalanceChanges


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_address** | **str** | The Bech32m-encoded human readable version of the entity&#39;s address | 
**fee_balance_changes** | [**[LtsFeeFungibleResourceBalanceChange]**](LtsFeeFungibleResourceBalanceChange.md) | If present, this field indicates fee-related balance changes, for example:  - Payment of the fee (including tip and royalty) - Distribution of royalties - Distribution of the fee and tip to the consensus-manager, for distributing to the relevant   validator/s at end of epoch  See https://www.radixdlt.com/blog/how-fees-work-in-babylon for further information on how fee payment works at Babylon.  | 
**non_fee_balance_changes** | [**[LtsFungibleResourceBalanceChange]**](LtsFungibleResourceBalanceChange.md) |  | 
**fee_balance_change** | [**LtsFungibleResourceBalanceChange**](LtsFungibleResourceBalanceChange.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


