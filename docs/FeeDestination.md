# FeeDestination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_proposer** | **str** | The string-encoded decimal representing the amount of fee in XRD paid to the proposer. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**to_validator_set** | **str** | The string-encoded decimal representing the amount of fee in XRD paid to the validator set. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**to_burn** | **str** | The string-encoded decimal representing the amount of fee burnt, in XRD. A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**to_royalty_recipients** | [**[PaymentToRoyaltyRecipient]**](PaymentToRoyaltyRecipient.md) | A breakdown of where the royalties were paid to.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


