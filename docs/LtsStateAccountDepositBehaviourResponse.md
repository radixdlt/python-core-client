# LtsStateAccountDepositBehaviourResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_version** | [**StateVersion**](StateVersion.md) |  | 
**ledger_header_summary** | [**LedgerHeaderSummary**](LedgerHeaderSummary.md) |  | 
**default_deposit_rule** | [**DefaultDepositRule**](DefaultDepositRule.md) |  | 
**is_badge_authorized_depositor** | **bool** | Whether the input &#x60;badge&#x60; belongs to the account&#39;s set of authorized depositors. This field will only be present if any badge was passed in the request.  | [optional] 
**resource_specific_behaviours** | [**{str: (ResourceSpecificDepositBehaviour,)}**](ResourceSpecificDepositBehaviour.md) | A map from one of the input &#x60;resource_addresses&#x60; to its specific deposit behavior configured for this account. This field will only be present if an array of specific resource addresses was passed in the request (even if empty).  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


