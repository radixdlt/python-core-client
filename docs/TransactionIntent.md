# TransactionIntent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | [**IntentHash**](IntentHash.md) |  | 
**hash_bech32m** | **str** | The Bech32m-encoded human readable &#x60;IntentHash&#x60;. | 
**header** | [**TransactionHeader**](TransactionHeader.md) |  | 
**instructions** | **str** | The decompiled transaction manifest instructions. Only returned if enabled in &#x60;TransactionFormatOptions&#x60; on your request. | [optional] 
**blobs_hex** | **{str: (str,)}** | A map of the hex-encoded blob hash, to hex-encoded blob content. Only returned if enabled in &#x60;TransactionFormatOptions&#x60; on your request. | [optional] 
**message** | [**TransactionMessage**](TransactionMessage.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


