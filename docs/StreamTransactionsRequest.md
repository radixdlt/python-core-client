# StreamTransactionsRequest

A request to retrieve a sublist of committed transactions from the ledger. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The logical name of the network | 
**from_state_version** | [**StateVersion**](StateVersion.md) |  | 
**limit** | **int** | The maximum number of transactions that will be returned. | 
**sbor_format_options** | [**SborFormatOptions**](SborFormatOptions.md) |  | [optional] 
**transaction_format_options** | [**TransactionFormatOptions**](TransactionFormatOptions.md) |  | [optional] 
**substate_format_options** | [**SubstateFormatOptions**](SubstateFormatOptions.md) |  | [optional] 
**include_proofs** | **bool** | Whether to include LedgerProofs (default false) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


