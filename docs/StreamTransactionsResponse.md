# StreamTransactionsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_state_version** | [**StateVersion**](StateVersion.md) |  | 
**count** | **int** | An integer between &#x60;0&#x60; and &#x60;10000&#x60;, giving the total count of transactions in the returned response | 
**max_ledger_state_version** | [**StateVersion**](StateVersion.md) |  | 
**transactions** | [**[CommittedTransaction]**](CommittedTransaction.md) | A committed transactions list starting from the &#x60;from_state_version&#x60; (inclusive). | 
**previous_state_identifiers** | [**CommittedStateIdentifier**](CommittedStateIdentifier.md) |  | [optional] 
**proofs** | [**[LedgerProof]**](LedgerProof.md) | A ledger proof list starting from &#x60;from_state_version&#x60; (inclusive) stored by this node. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


