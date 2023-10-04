# TimestampedValidatorSignature


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validator_key** | [**EcdsaSecp256k1PublicKey**](EcdsaSecp256k1PublicKey.md) |  | 
**validator_address** | **str** | The Bech32m-encoded human readable version of the component address | 
**timestamp_ms** | **int** | An integer between &#x60;0&#x60; and &#x60;10^14&#x60;, marking the unix timestamp in ms. | 
**signature** | [**EcdsaSecp256k1Signature**](EcdsaSecp256k1Signature.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


