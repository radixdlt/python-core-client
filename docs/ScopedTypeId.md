# ScopedTypeId

An identifier for a type in the context of a schema.  The location of the schema store to locate the schema is not included, and is known from context. Currently the schema store will be in the schema partition under a node (typically a package).  Note - this type provides scoping to a schema even for well-known types where the schema is irrelevant. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_hash** | [**SchemaHash**](SchemaHash.md) |  | 
**local_type_id** | [**LocalTypeId**](LocalTypeId.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


