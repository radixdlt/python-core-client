# ResourceChange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_address** | **str** | The Bech32m-encoded human readable version of the resource address | 
**component_entity** | [**EntityReference**](EntityReference.md) |  | 
**vault_entity** | [**EntityReference**](EntityReference.md) |  | 
**amount** | **str** | The string-encoded decimal representing the XRD amount put or taken from the vault. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


