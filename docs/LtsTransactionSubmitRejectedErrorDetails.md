# LtsTransactionSubmitRejectedErrorDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | An explanation of the error | 
**is_fresh** | **bool** | Whether (true) this rejected status has just been calculated fresh, or (false) the status is from the pending transaction result cache.  | 
**is_payload_rejection_permanent** | **bool** | Whether the rejection of this payload is known to be permanent.  | 
**is_intent_rejection_permanent** | **bool** | Whether the rejection of this intent is known to be permanent - this is a stronger statement than the payload rejection being permanent, as it implies any payloads containing the intent will also be permanently rejected.  | 
**is_rejected_because_intent_already_committed** | **bool** | Whether the cached rejection of this intent is due to the intent already having been committed. If so, see the /transaction/receipt endpoint for further information.  | 
**type** | [**LtsTransactionSubmitErrorDetailsType**](LtsTransactionSubmitErrorDetailsType.md) |  | 
**retry_from_timestamp** | [**Instant**](Instant.md) |  | [optional] 
**retry_from_epoch** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch after which the node will consider recalculating the validity of the transaction. Only present if the rejection is temporary due to a header specifying a \&quot;from epoch\&quot; in the future.  | [optional] 
**invalid_from_epoch** | **int** | An integer between &#x60;0&#x60; and &#x60;10^10&#x60;, marking the epoch from which the transaction will no longer be valid, and be permanently rejected. Only present if the rejection isn&#39;t permanent.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


