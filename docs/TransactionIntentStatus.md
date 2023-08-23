# TransactionIntentStatus

The status of the transaction intent, as determined by the node. FateUncertain or FateUncertainButLikelyRejection mean that it's still possible that a payload containing the transaction  

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the transaction intent, as determined by the node. FateUncertain or FateUncertainButLikelyRejection mean that it&#39;s still possible that a payload containing the transaction   |  must be one of ["CommittedSuccess", "CommittedFailure", "PermanentRejection", "InMempool", "NotSeen", "FateUncertain", "FateUncertainButLikelyRejection", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


