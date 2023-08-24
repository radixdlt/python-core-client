# PlaintextTransactionMessageAllOf

An unencrypted message.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mime_type** | **str** | Intended to represent the RFC 2046 MIME type of the &#x60;content&#x60;. A client cannot trust that this field is a valid mime type - in particular, the choice between &#x60;String&#x60; or &#x60;Binary&#x60; representation of the content is not enforced by this &#x60;mime_type&#x60;.  | 
**content** | [**PlaintextMessageContent**](PlaintextMessageContent.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


