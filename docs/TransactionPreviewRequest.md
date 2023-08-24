# TransactionPreviewRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | The logical name of the network | 
**manifest** | **str** | A text-representation of a transaction manifest | 
**start_epoch_inclusive** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch at which the transaction starts being valid | 
**end_epoch_exclusive** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch at which the transaction is no longer valid | 
**tip_percentage** | **int** | An integer between &#x60;0&#x60; and &#x60;255&#x60;, giving the validator tip as a percentage amount. A value of &#x60;1&#x60; corresponds to 1% of the fee. | 
**nonce** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, chosen to allow a unique intent to be created (to enable submitting an otherwise identical/duplicate intent).  | 
**signer_public_keys** | [**[PublicKey]**](PublicKey.md) | A list of public keys to be used as transaction signers | 
**flags** | [**TransactionPreviewRequestFlags**](TransactionPreviewRequestFlags.md) |  | 
**blobs_hex** | **[str]** | An array of hex-encoded blob data (optional) | [optional] 
**notary_public_key** | [**PublicKey**](PublicKey.md) |  | [optional] 
**notary_is_signatory** | **bool** | Whether the notary should count as a signatory (optional, default false) | [optional] 
**message** | [**TransactionMessage**](TransactionMessage.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


