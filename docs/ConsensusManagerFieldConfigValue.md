# ConsensusManagerFieldConfigValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_validators** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, specifying the maximum number of validators in the active validator set.  | 
**epoch_change_condition** | [**EpochChangeCondition**](EpochChangeCondition.md) |  | 
**num_unstake_epochs** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, specifying the minimum number of epochs before an unstaker can withdraw their XRD.  | 
**total_emission_xrd_per_epoch** | **str** | A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**min_validator_reliability** | **str** | A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**num_owner_stake_units_unlock_epochs** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, specifying the minimum number of epochs before an owner can take their stake units after attempting to withdraw them.  | 
**num_fee_increase_delay_epochs** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, specifying the minimum number of epochs before a fee increase takes effect.  | 
**validator_creation_usd_equivalent_cost** | **str** | The defining decimal cost of a validator in USD. This is turned into an XRD cost through the current protocol-based USD/XRD multiplier. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**validator_creation_xrd_cost** | **str** | The decimal amount of XRD required to be passed in a bucket to create a validator. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


