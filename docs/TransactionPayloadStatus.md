# TransactionPayloadStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload_hash** | [**NotarizedTransactionHash**](NotarizedTransactionHash.md) |  | 
**status** | **str** | The status of the transaction payload, as per this node. A NotInMempool status means that it wasn&#39;t rejected at last execution attempt, but it&#39;s not currently in the mempool either.  | 
**error_message** | **str** | An explanation for the error, if failed or rejected | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


