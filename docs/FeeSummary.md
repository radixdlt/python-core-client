# FeeSummary

Fees paid

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost_unit_price** | **str** | The string-encoded decimal representing the XRD price of a single cost unit. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(256 - 1) &lt;&#x3D; m &lt; 2^(256 - 1)&#x60;.  | 
**tip_percentage** | **int** | An integer between &#x60;0&#x60; and &#x60;255&#x60;, giving the validator tip as a percentage amount. A value of &#x60;1&#x60; corresponds to 1% of the fee. | 
**cost_unit_limit** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, representing the maximum amount of cost units available for the transaction execution. | 
**cost_units_consumed** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, representing the amount of cost units consumed by the transaction execution. | 
**cost_unit_execution_breakdown** | **{str: (int,)}** | A breakdown of where the execution cost went.  | 
**xrd_total_execution_cost** | **str** | The string-encoded decimal representing the total amount of XRD burned in the transaction as part of execution costs. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(256 - 1) &lt;&#x3D; m &lt; 2^(256 - 1)&#x60;.  | 
**xrd_total_royalty_cost** | **str** | The string-encoded decimal representing the total amount of XRD paid in royalties as part of the transaction. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(256 - 1) &lt;&#x3D; m &lt; 2^(256 - 1)&#x60;.  | 
**xrd_total_state_expansion_cost** | **str** | The string-encoded decimal representing the total amount of XRD paid in state expansion costs as part of the transaction. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(256 - 1) &lt;&#x3D; m &lt; 2^(256 - 1)&#x60;.  | 
**xrd_total_tipped** | **str** | The string-encoded decimal representing the total amount of XRD tipped to validators in the transaction. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(256 - 1) &lt;&#x3D; m &lt; 2^(256 - 1)&#x60;.  | 
**xrd_vault_payments** | [**[VaultPayment]**](VaultPayment.md) | A breakdown of which vaults were used to pay the fee.  | 
**xrd_royalty_receivers** | [**[RoyaltyPayment]**](RoyaltyPayment.md) | A breakdown of where the royalties were paid to.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


