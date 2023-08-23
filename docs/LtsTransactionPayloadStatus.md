# LtsTransactionPayloadStatus

The status of the transaction payload, as per this node. A NotInMempool status means that it wasn't rejected at last execution attempt, but it's not currently in the mempool either. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The status of the transaction payload, as per this node. A NotInMempool status means that it wasn&#39;t rejected at last execution attempt, but it&#39;s not currently in the mempool either.  |  must be one of ["CommittedSuccess", "CommittedFailure", "PermanentlyRejected", "TransientlyRejected", "InMempool", "NotInMempool", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


