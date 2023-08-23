# LocalTypeIndex


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The location against which to resolve this type reference against a given schema. WellKnown indicates the index is a pointer to a well known scrypto type with that id. SchemaLocal indicates the index is a pointer into the given schema.  | 
**index** | **int** | Either the well known identifier, of the schema-local index, depending on the kind.  | 
**as_sbor** | [**SborData**](SborData.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


