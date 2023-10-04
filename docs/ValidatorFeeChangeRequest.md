# ValidatorFeeChangeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epoch_effective** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch at which the fee change becomes effective.  | 
**new_fee_factor** | **str** | A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


