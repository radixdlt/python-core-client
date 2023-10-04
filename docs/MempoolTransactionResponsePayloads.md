# MempoolTransactionResponsePayloads


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | [**NotarizedTransactionHash**](NotarizedTransactionHash.md) |  | 
**hash_bech32m** | **str** | The Bech32m-encoded human readable &#x60;NotarizedTransactionHash&#x60;. | 
**hex** | **str** | The hex-encoded full notarized transaction payload - returned only if found in mempool. | [optional] 
**error** | **str** | Error message why &#x60;hex&#x60; field is missing: the transaction was not found in the mempool or the provided hash is invalid.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


