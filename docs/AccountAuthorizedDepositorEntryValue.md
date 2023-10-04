# AccountAuthorizedDepositorEntryValue

Empty value. The existence of the key implies the depositor is authorized.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_authorized** | **bool** | This is always true. This field is just added to ensure we return some data as the value, so a present entry is not confused by clients for a deleted/missing entry (which would imply not authorized).  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


