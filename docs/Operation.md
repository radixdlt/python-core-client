# Operation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of operation: Resource, Data, or ResourceAndData. | 
**entity_identifier** | [**EntityIdentifier**](EntityIdentifier.md) |  | 
**substate** | [**Substate**](Substate.md) |  | [optional] 
**amount** | [**ResourceAmount**](ResourceAmount.md) |  | [optional] 
**data** | [**Data**](Data.md) |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Metadata for the operation. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


