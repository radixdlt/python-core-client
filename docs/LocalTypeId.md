# LocalTypeId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The location against which to resolve this type reference. | 
**id** | **int** | A reference to a type, interpreted according to &#x60;kind&#x60;: - If &#x60;WellKnown&#x60;, then it is a pointer to a well known scrypto type with that ID, - If &#x60;SchemaLocal&#x60;, then it is an index into the given schema.  | 
**as_sbor** | [**SborData**](SborData.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


