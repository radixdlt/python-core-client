# AuthConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_auth_type** | [**FunctionAuthType**](FunctionAuthType.md) |  | 
**method_auth_type** | [**MethodAuthType**](MethodAuthType.md) |  | 
**function_access_rules** | [**{str: (AccessRule,)}**](AccessRule.md) | A map from a function name to AccessRule. Only exists if &#x60;function_auth_type&#x60; is set to &#x60;FunctionAccessRules&#x60;.  | [optional] 
**method_roles** | [**StaticRolesAuthTemplate**](StaticRolesAuthTemplate.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


