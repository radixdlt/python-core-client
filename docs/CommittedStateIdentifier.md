# CommittedStateIdentifier


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_version** | [**StateVersion**](StateVersion.md) |  | 
**state_tree_hash** | **str** | The hex-encoded root hash of the state tree. This captures the current state of the state on the ledger.  | 
**transaction_tree_hash** | **str** | The hex-encoded root hash of the transaction tree. This captures the ledger transactions committed to the ledger.  | 
**receipt_tree_hash** | **str** | The hex-encoded root hash of the receipt tree. This captures the consensus-agreed output of each transaction on the ledger.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


