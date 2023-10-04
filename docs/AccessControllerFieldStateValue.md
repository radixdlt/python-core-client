# AccessControllerFieldStateValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlled_vault** | [**EntityReference**](EntityReference.md) |  | 
**recovery_badge_resource_address** | **str** | The Bech32m-encoded human readable version of the resource address | 
**is_primary_role_locked** | **bool** | Whether the primary role is currently locked. | 
**has_primary_role_badge_withdraw_attempt** | **bool** | Whether the primary role badge withdraw is currently being attempted. | 
**has_recovery_role_badge_withdraw_attempt** | **bool** | Whether the recovery role badge withdraw is currently being attempted. | 
**timed_recovery_delay_minutes** | **int** | An integer between &#x60;0&#x60; and &#x60;2^32 - 1&#x60;, specifying the amount of time (in minutes) that it takes for timed recovery to be done. When not present, then timed recovery can not be performed through this access controller.  | [optional] 
**primary_role_recovery_attempt** | [**PrimaryRoleRecoveryAttempt**](PrimaryRoleRecoveryAttempt.md) |  | [optional] 
**recovery_role_recovery_attempt** | [**RecoveryRoleRecoveryAttempt**](RecoveryRoleRecoveryAttempt.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


