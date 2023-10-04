# FeeSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_cost_units_consumed** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, representing the amount of cost units consumed by the transaction execution. | 
**finalization_cost_units_consumed** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, representing the amount of cost units consumed by the transaction finalization. | 
**xrd_total_execution_cost** | **str** | The string-encoded decimal representing the total amount of XRD burned in the transaction as part of execution costs. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**xrd_total_finalization_cost** | **str** | The string-encoded decimal representing the total amount of XRD burned in the transaction as part of finalization costs. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**xrd_total_royalty_cost** | **str** | The string-encoded decimal representing the total amount of XRD paid in royalties as part of the transaction. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**xrd_total_storage_cost** | **str** | The string-encoded decimal representing the total amount of XRD paid in state expansion costs as part of the transaction. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**xrd_total_tipping_cost** | **str** | The string-encoded decimal representing the total amount of XRD tipped to validators in the transaction. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


