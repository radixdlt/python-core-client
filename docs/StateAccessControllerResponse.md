# StateAccessControllerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at_ledger_state** | [**LedgerStateSummary**](LedgerStateSummary.md) |  | 
**state** | [**Substate**](Substate.md) |  | 
**owner_role** | [**Substate**](Substate.md) |  | 
**vaults** | [**[VaultBalance]**](VaultBalance.md) | Any vaults owned directly or indirectly by the component | 
**descendent_nodes** | [**[StateComponentDescendentNode]**](StateComponentDescendentNode.md) | Any descendent nodes owned directly or indirectly by the component | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


