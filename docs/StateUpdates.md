# StateUpdates

Transaction state updates (only present if status is Succeeded or Failed)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_partitions** | [**[PartitionId]**](PartitionId.md) |  | 
**created_substates** | [**[CreatedSubstate]**](CreatedSubstate.md) |  | 
**updated_substates** | [**[UpdatedSubstate]**](UpdatedSubstate.md) |  | 
**deleted_substates** | [**[DeletedSubstate]**](DeletedSubstate.md) |  | 
**new_global_entities** | [**[EntityReference]**](EntityReference.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


