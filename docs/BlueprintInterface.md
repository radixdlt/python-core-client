# BlueprintInterface


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generic_type_parameters** | [**[GenericTypeParameter]**](GenericTypeParameter.md) | Generic (SBOR) type parameters which need to be filled by a concrete instance of this blueprint.  | 
**features** | **[str]** |  | 
**state** | [**IndexedStateSchema**](IndexedStateSchema.md) |  | 
**functions** | [**{str: (FunctionSchema,)}**](FunctionSchema.md) | A map from the function name to the FunctionSchema | 
**events** | [**{str: (TypePointer,)}**](TypePointer.md) | A map from the event name to the local type index for the event payload under the blueprint schema. | 
**outer_blueprint** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


