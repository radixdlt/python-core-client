# BlueprintDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | [**BlueprintInterface**](BlueprintInterface.md) |  | 
**function_exports** | [**{str: (PackageExport,)}**](PackageExport.md) | A map from the function name to its export | 
**hook_exports** | [**[HookExport]**](HookExport.md) | A map from certain object lifecycle hooks to a callback \&quot;package export\&quot;. There is at most one callback registered for each &#x60;ObjectHook&#x60;.  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


