# EncryptedTransactionMessageAllOf

A `PlaintextTransactionMessage` encrypted with \"Multi-party ECIES\" for a number of decryptors (public keys).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_hex** | **str** | The hex-encoded (128-bit) AES-GCM encrypted bytes of an SBOR-encoded &#x60;PlaintextTransactionMessage&#x60;. The bytes are serialized as the concatenation &#x60;Nonce/IV (12 bytes) || Cipher (variable length) || Tag/MAC (16 bytes)&#x60;:  | 
**curve_decryptor_sets** | [**[EncryptedMessageCurveDecryptorSet]**](EncryptedMessageCurveDecryptorSet.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


