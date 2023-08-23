# DefaultDepositRule

This setting has the following interpretations: - Allow: Allows the deposit of all resources - the deny list is honored in this state. - Reject: Disallows the deposit of all resources - the allow list is honored in this state. - AllowExisting: Only deposits of existing resources is accepted - both allow and deny lists are honored in this mode. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | This setting has the following interpretations: - Allow: Allows the deposit of all resources - the deny list is honored in this state. - Reject: Disallows the deposit of all resources - the allow list is honored in this state. - AllowExisting: Only deposits of existing resources is accepted - both allow and deny lists are honored in this mode.  |  must be one of ["Accept", "Reject", "AllowExisting", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


