# CommittedIntentMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_version** | [**StateVersion**](StateVersion.md) |  | 
**payload_hash** | [**NotarizedTransactionHash**](NotarizedTransactionHash.md) |  | 
**payload_hash_bech32m** | **str** | The Bech32m-encoded human readable &#x60;NotarizedTransactionHash&#x60;. | 
**is_same_transaction** | **bool** | Whether the intent was committed in a transaction with the same payload. This is a convenience field, which can also be computed using &#x60;payload_hash&#x60; by a client knowing the payload of the submitted transaction.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


