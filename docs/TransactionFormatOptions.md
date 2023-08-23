# TransactionFormatOptions

Requested transaction formats to include in the response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest** | **bool** | Whether to return the raw manifest (default true) | [optional] 
**blobs** | **bool** | Whether to return the hex-encoded blobs (default false) | [optional] 
**message** | **bool** | Whether to return the transaction message (default false) | [optional] 
**raw_system_transaction** | **bool** | Whether to return the raw hex-encoded system transaction bytes (default false) | [optional] 
**raw_notarized_transaction** | **bool** | Whether to return the raw hex-encoded notarized transaction bytes (default true) | [optional] 
**raw_ledger_transaction** | **bool** | Whether to return the raw hex-encoded ledger transaction bytes (default false) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


