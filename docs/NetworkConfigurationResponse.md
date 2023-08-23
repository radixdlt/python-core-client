# NetworkConfigurationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**NetworkConfigurationResponseVersion**](NetworkConfigurationResponseVersion.md) |  | 
**network** | **str** | The logical name of the network | 
**network_id** | [**NetworkIdentifierByte**](NetworkIdentifierByte.md) |  | 
**network_hrp_suffix** | **str** | The network suffix used for Bech32m HRPs used for addressing. | 
**address_types** | [**[AddressType]**](AddressType.md) |  | 
**well_known_addresses** | [**NetworkConfigurationResponseWellKnownAddresses**](NetworkConfigurationResponseWellKnownAddresses.md) |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


