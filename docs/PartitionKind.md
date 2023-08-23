# PartitionKind

The type of the partition: - Field   - Has key: TupleKey(u8) also known as an offset   - No iteration exposed to engine   - Is versioned / locked substate-by-substate - KeyValue (\"ConcurrentMap\")   - Has key: MapKey(Vec<u8>)   - No iteration exposed to engine   - Is versioned / locked substate-by-substate - Index   - Has key: MapKey(Vec<u8>)   - Iteration exposed to engine via the MapKey's database key (ie hash of the key)   - Is versioned / locked in its entirety - SortedIndex   - Has key: SortedU16Key(U16, Vec<u8>)   - Iteration exposed to engine via the user-controlled U16 prefix and then the MapKey's database key (ie hash of the key)   - Is versioned / locked in its entirety 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The type of the partition: - Field   - Has key: TupleKey(u8) also known as an offset   - No iteration exposed to engine   - Is versioned / locked substate-by-substate - KeyValue (\&quot;ConcurrentMap\&quot;)   - Has key: MapKey(Vec&lt;u8&gt;)   - No iteration exposed to engine   - Is versioned / locked substate-by-substate - Index   - Has key: MapKey(Vec&lt;u8&gt;)   - Iteration exposed to engine via the MapKey&#39;s database key (ie hash of the key)   - Is versioned / locked in its entirety - SortedIndex   - Has key: SortedU16Key(U16, Vec&lt;u8&gt;)   - Iteration exposed to engine via the user-controlled U16 prefix and then the MapKey&#39;s database key (ie hash of the key)   - Is versioned / locked in its entirety  |  must be one of ["Field", "KeyValue", "Index", "SortedIndex", ]
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


