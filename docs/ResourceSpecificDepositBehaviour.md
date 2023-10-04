# ResourceSpecificDepositBehaviour


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vault_exists** | **bool** | Whether the account contains a vault for the resource (even if 0 balance). This plays a role when &#x60;DefaultDepositRule&#x60; is &#x60;AllowExisting&#x60;.  | 
**is_xrd** | **bool** | Whether the resource represents the native XRD fungible. XRD is a special case which does not require &#x60;vault_exists &#x3D; true&#x60; to satisfy the &#x60;AllowExisting&#x60; rule.  | 
**allows_try_deposit** | **bool** | The fully resolved &#x60;try_deposit_*&#x60; ability of this resource (which takes all the inputs into account, including the authorized depositor badge, the default deposit rule and the above resource-specific circumstances).  | 
**resource_preference** | [**ResourcePreference**](ResourcePreference.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


