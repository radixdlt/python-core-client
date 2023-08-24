# TransactionParseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The logical name of the network | 
**payload_hex** | **str** | A hex-encoded payload of a full transaction or a partial transaction - either a notarized transaction, a signed transaction intent an unsigned transaction intent, or a ledger payload.  | 
**parse_mode** | **str** | The type of transaction payload that should be assumed. If omitted, \&quot;Any\&quot; is used - where the payload is attempted to be parsed as each of the following in turn: Notarized, Signed, Unsigned, Ledger.  | [optional] 
**validation_mode** | **str** | The type of validation that should be performed, if the payload correctly decompiles as a Notarized Transaction. This is only relevant for Notarized payloads. If omitted, \&quot;Static\&quot; is used.  | [optional] 
**response_mode** | **str** | The amount of information to return in the response. \&quot;Basic\&quot; includes the type, validity information, and any relevant identifiers. \&quot;Full\&quot; also includes the fully parsed information. If omitted, \&quot;Full\&quot; is used.  | [optional] 
**transaction_format_options** | [**TransactionFormatOptions**](TransactionFormatOptions.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


