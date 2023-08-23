# LtsTransactionSubmitPriorityThresholdNotMetErrorDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tip_percentage** | **int** | Tip percentage of the submitted (and rejected) transaction.  | 
**type** | [**LtsTransactionSubmitErrorDetailsType**](LtsTransactionSubmitErrorDetailsType.md) |  | 
**min_tip_percentage_required** | **int** | A lower bound for tip percentage at current mempool state. Anything lower than this will very likely result in a mempool rejection. A missing value means there is no tip that can guarantee submission.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


