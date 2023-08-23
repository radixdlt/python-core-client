# TransactionSubmitErrorResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_type** | [**ErrorResponseType**](ErrorResponseType.md) |  | 
**code** | **int** | A numeric code corresponding to the given HTTP error code. | 
**message** | **str** | A human-readable error message. | 
**details** | [**TransactionSubmitErrorDetails**](TransactionSubmitErrorDetails.md) |  | [optional] 
**trace_id** | **str** | A GUID to be used when reporting errors, to allow correlation with the Core API&#39;s error logs, in the case where the Core API details are hidden. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


