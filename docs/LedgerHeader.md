# LedgerHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch. | 
**round** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the current round in an epoch | 
**state_version** | [**StateVersion**](StateVersion.md) |  | 
**hashes** | [**LedgerHashes**](LedgerHashes.md) |  | 
**consensus_parent_round_timestamp_ms** | **int** | An integer between &#x60;0&#x60; and &#x60;10^14&#x60;, marking the consensus parent round timestamp in ms. | 
**proposer_timestamp_ms** | **int** | An integer between &#x60;0&#x60; and &#x60;10^14&#x60;, marking the proposer timestamp in ms. | 
**next_epoch** | [**NextEpoch**](NextEpoch.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


