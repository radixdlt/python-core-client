# ConsensusManagerFieldStateValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the current epoch | 
**round** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the current round in an epoch | 
**is_started** | **bool** |  | 
**effective_epoch_start** | [**Instant**](Instant.md) |  | 
**actual_epoch_start** | [**Instant**](Instant.md) |  | 
**current_leader** | [**ActiveValidatorIndex**](ActiveValidatorIndex.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


