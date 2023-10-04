# RemoteGenericSubstitutionAllOf

The generic substitution is provided remotely by a blueprint type. The `resolved_full_type_id` is added by the node, and is always present in the model returned from the transaction stream API. Other APIs may not resolve the type from the blueprint definition.  

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprint_type_identifier** | [**BlueprintTypeIdentifier**](BlueprintTypeIdentifier.md) |  | 
**resolved_full_type_id** | [**FullyScopedTypeId**](FullyScopedTypeId.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


