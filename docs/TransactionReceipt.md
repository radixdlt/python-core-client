# TransactionReceipt

The transaction execution receipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**TransactionStatus**](TransactionStatus.md) |  | 
**fee_summary** | [**FeeSummary**](FeeSummary.md) |  | 
**costing_parameters** | [**CostingParameters**](CostingParameters.md) |  | 
**state_updates** | [**StateUpdates**](StateUpdates.md) |  | 
**fee_source** | [**FeeSource**](FeeSource.md) |  | [optional] 
**fee_destination** | [**FeeDestination**](FeeDestination.md) |  | [optional] 
**events** | [**[Event]**](Event.md) |  | [optional] 
**next_epoch** | [**NextEpoch**](NextEpoch.md) |  | [optional] 
**output** | [**[SborData]**](SborData.md) | The manifest line-by-line engine return data (only present if &#x60;status&#x60; is &#x60;Succeeded&#x60;) | [optional] 
**error_message** | **str** | Error message (only present if status is &#x60;Failed&#x60; or &#x60;Rejected&#x60;) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


