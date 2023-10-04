# BlueprintInterface


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generic_type_parameters** | [**[GenericTypeParameter]**](GenericTypeParameter.md) | Generic (SBOR) type parameters which need to be filled by a concrete instance of this blueprint.  | 
**is_transient** | **bool** | If true, an instantiation of this blueprint cannot be persisted. EG buckets and proofs are transient. | 
**features** | **[str]** |  | 
**state** | [**IndexedStateSchema**](IndexedStateSchema.md) |  | 
**functions** | [**{str: (FunctionSchema,)}**](FunctionSchema.md) | A map from the function name to the FunctionSchema | 
**events** | [**{str: (BlueprintPayloadDef,)}**](BlueprintPayloadDef.md) | A map from the event name to the event payload type reference. | 
**types** | [**{str: (ScopedTypeId,)}**](ScopedTypeId.md) | A map from the registered type name to the concrete type, resolved against a schema from the package&#39;s schema partition.  | 
**outer_blueprint** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


