# LeaderProposalHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gap_round_leaders** | [**[ActiveValidatorIndex]**](ActiveValidatorIndex.md) | The validators which were leaders of the \&quot;gap\&quot; rounds (i.e. since the previous &#x60;RoundUpdateValidatorTransaction&#x60; - which means that this list will contain exactly &#x60;current.round - previous.round - 1&#x60; elements). The validators on this list should be penalized during emissions at the end of the epoch. | 
**current_leader** | [**ActiveValidatorIndex**](ActiveValidatorIndex.md) |  | 
**is_fallback** | **bool** | Whether the concluded round was conducted in a \&quot;fallback\&quot; mode (i.e. indicating a fault of the current leader). When &#x60;true&#x60;, the &#x60;current_leader&#x60; should be penalized during emissions in the same way as &#x60;gap_round_leaders&#x60;. When &#x60;false&#x60;, the &#x60;current_leader&#x60; is considered to have made this round&#39;s proposal successfully. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


