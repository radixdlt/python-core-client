# ParsedNotarizedTransactionAllOfValidationError

If the transaction is known to not be valid, this gives a reason. Different levels of validation are performed, dependent on the validation mode. Note that, even if validation mode is Static or Full, the transaction may still be rejected or fail due to issues at runtime (eg if the loan cannot be repaid). 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The error message.  | 
**is_permanent** | **bool** | Whether the error is known to be permanent, or not. This relates to whether the transaction would be rejected permanently or temporarily if submitted.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


