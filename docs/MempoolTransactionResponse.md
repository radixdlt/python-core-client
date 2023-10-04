# MempoolTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | An integer giving the total count of payload hashes checked in the returned response. | 
**payloads** | [**[MempoolTransactionResponsePayloads]**](MempoolTransactionResponsePayloads.md) | An array containing pairs of payload hash (query) and payload hex or error (response). Note that this response is bounded - this means it is not guaranteed all queries will be processed. Please query missing payload hashes again.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


