# StateComponentDescendentNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_entity** | [**EntityReference**](EntityReference.md) |  | 
**parent_partition_number** | **int** |  | 
**parent_substate_key_hex** | **str** | The hex-encoded bytes of the substate key, under the entity partition | 
**parent_substate_db_sort_key_hex** | **str** | The hex-encoded bytes of the partially-hashed DB sort key, under the given entity partition | 
**entity** | [**EntityReference**](EntityReference.md) |  | 
**depth** | **int** | Depth under component | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


