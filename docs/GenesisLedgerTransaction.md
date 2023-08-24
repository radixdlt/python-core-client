# GenesisLedgerTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_flash** | **bool** | The first genesis \&quot;transaction\&quot; flashes state into the database to prepare for the bootstrap transaction. Such a transaction does not have an associated &#x60;system_transaction&#x60;  | 
**type** | [**LedgerTransactionType**](LedgerTransactionType.md) |  | 
**system_transaction** | [**SystemTransaction**](SystemTransaction.md) |  | [optional] 
**payload_hex** | **str** | The hex-encoded full ledger transaction payload. Only returned if enabled in TransactionFormatOptions on your request. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


