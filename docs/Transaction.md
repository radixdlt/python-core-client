# Transaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_identifier** | [**TransactionIdentifier**](TransactionIdentifier.md) |  | 
**operation_groups** | [**[OperationGroup]**](OperationGroup.md) | Transactions are split into operation groups which are roughly equivalent to ledger accounting entries where all credits have an equivalent debit amount. | 
**metadata** | [**CommittedTransactionMetadata**](CommittedTransactionMetadata.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


