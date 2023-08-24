# EncryptedMessageCurveDecryptorSet

A decryptor set for a particular ECDSA curve type. The (128-bit) AES-GCM symmetric key is encrypted separately for each decryptor public key via (256-bit) AES-KeyWrap. AES-KeyWrap uses a key derived via a KDF (Key Derivation Function) using a shared secret. For each decryptor public key, we create a shared curve point `G` via static Diffie-Helman between the decryptor public key, and a per-transaction ephemeral public key for that curve type. We then use that shared secret with a key derivation function to create the (256-bit) KEK (Key Encrypting Key): `KEK = HKDF(hash: Blake2b, secret: x co-ord of G, salt: [], length: 256 bits)`. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dh_ephemeral_public_key** | [**PublicKey**](PublicKey.md) |  | 
**decryptors** | [**[EncryptedMessageDecryptor]**](EncryptedMessageDecryptor.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


