# NonFungibleVaultContentsIndexEntryValue

This object is empty, and always present on this substate. Note that when a non-fungible is withdrawn from the vault, the full substate is deleted, which is marked by a DeletedSubstate action (rather than deletion of the value property in an UpdateSubstate action). This is because this is an Index entry, not a KeyValueStore entry. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_present** | **bool** | This is a dummy property which is always set to true and means nothing. It exists just to ensure this object has a well-defined type in OpenAPI schemas.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


