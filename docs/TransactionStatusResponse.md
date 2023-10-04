# TransactionStatusResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent_status** | [**TransactionIntentStatus**](TransactionIntentStatus.md) |  | 
**status_description** | **str** | An explanation as to why the intent status is resolved as it is.  | 
**known_payloads** | [**[TransactionPayloadDetails]**](TransactionPayloadDetails.md) |  | 
**invalid_from_epoch** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch from which the transaction will no longer be valid, and be permanently rejected. Only present if the intent status is InMempool or Unknown and we know about a payload.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


