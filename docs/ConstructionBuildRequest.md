# ConstructionBuildRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_identifier** | [**NetworkIdentifier**](NetworkIdentifier.md) |  | 
**operation_groups** | [**[OperationGroup]**](OperationGroup.md) | Operation groups which describe the intent of the request. | 
**fee_payer** | [**EntityIdentifier**](EntityIdentifier.md) |  | 
**message** | **str** | An optional message payload encoded in hex with the Radix message encoding scheme. | [optional] 
**disable_resource_allocate_and_destroy** | **bool** | Disallow minting and burning of tokens (except for fees). Useful for verification of transactions without needing to fetch additional substate data, such as when verifying transactions in an offline environment. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


