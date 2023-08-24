# TransactionHeader


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_id** | [**NetworkIdentifierByte**](NetworkIdentifierByte.md) |  | 
**start_epoch_inclusive** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch from which the transaction can be submitted. In the case of uncommitted transactions, a value of &#x60;10^10&#x60; indicates that the epoch was &gt;&#x3D; &#x60;10^10&#x60;.  | 
**end_epoch_exclusive** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch from which the transaction will no longer be valid, and be rejected. In the case of uncommitted transactions, a value of &#x60;10^10&#x60; indicates that the epoch was &gt;&#x3D; &#x60;10^10&#x60;.  | 
**nonce** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, chosen to allow a unique intent to be created (to enable submitting an otherwise identical/duplicate intent).  | 
**notary_public_key** | [**PublicKey**](PublicKey.md) |  | 
**notary_is_signatory** | **bool** | Specifies whether the notary public key should be included in the transaction signers list | 
**tip_percentage** | **int** | An integer between &#x60;0&#x60; and &#x60;255&#x60;, giving the validator tip as a percentage amount. A value of &#x60;1&#x60; corresponds to 1% of the fee. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


