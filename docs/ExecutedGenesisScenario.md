# ExecutedGenesisScenario


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sequence_number** | **int** | An index of the Scenario on the list of all Scenarios that were executed. Note: the stored sequence numbers do not necessarily have to be consecutive (e.g. in a case where some configured Scenario failed to execute or failed to write results to the database).  | 
**logical_name** | **str** |  | 
**committed_transactions** | [**[ExecutedScenarioTransaction]**](ExecutedScenarioTransaction.md) | Transactions successfully committed by the Scenario. | 
**addresses** | **{str: (str,)}** | Well-named addresses touched/created by the Scenario, keyed by their name.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


