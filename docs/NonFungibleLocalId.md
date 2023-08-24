# NonFungibleLocalId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**simple_rep** | **str** | The simple string representation of the non-fungible id. For string id types, this is simply the string itself; for integer types, this is the integer as a decimal; and for the bytes id type, this is the lower case hex representation. A non-fungible resource has a fixed &#x60;NonFungibleIdType&#x60;, so this representation uniquely identifies this non-fungible under the given resource address.  | 
**id_type** | [**NonFungibleIdType**](NonFungibleIdType.md) |  | 
**sbor_hex** | **str** | The hex-encoded SBOR-encoded bytes of its non-fungible id | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


