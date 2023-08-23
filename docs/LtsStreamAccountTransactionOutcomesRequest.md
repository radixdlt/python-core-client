# LtsStreamAccountTransactionOutcomesRequest

A request to retrieve a sublist of committed transactions from the ledger. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The logical name of the network | 
**account_address** | **str** | The Bech32m-encoded human readable version of the account&#39;s address | 
**from_state_version** | [**StateVersion**](StateVersion.md) |  | 
**limit** | **int** | The maximum number of transactions that will be returned. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


