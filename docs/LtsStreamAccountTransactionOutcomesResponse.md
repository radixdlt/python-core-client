# LtsStreamAccountTransactionOutcomesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_state_version** | [**StateVersion**](StateVersion.md) |  | 
**count** | **int** | An integer between &#x60;0&#x60; and &#x60;10000&#x60;, giving the total count of transactions in the returned response | 
**max_ledger_state_version** | [**StateVersion**](StateVersion.md) |  | 
**committed_transaction_outcomes** | [**[LtsCommittedTransactionOutcome]**](LtsCommittedTransactionOutcome.md) | A committed transaction outcomes list starting from the &#x60;from_state_version&#x60; (inclusive). | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


