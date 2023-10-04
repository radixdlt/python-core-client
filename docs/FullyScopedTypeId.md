# FullyScopedTypeId

An identifier for a type in the context of a schema in an entity's schema partition.  Note - this type provides a schema context even for well-known types where this context is effectively irrelevant. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_address** | **str** | Bech32m-encoded human readable version of the entity&#39;s address (ie the entity&#39;s node id) | 
**schema_hash** | [**SchemaHash**](SchemaHash.md) |  | 
**local_type_id** | [**LocalTypeId**](LocalTypeId.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


