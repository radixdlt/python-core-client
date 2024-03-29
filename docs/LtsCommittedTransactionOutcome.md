# LtsCommittedTransactionOutcome

For the given transaction, contains the status, total fee summary and individual entity resource balance changes. The balance changes accounts for the fee payments as well. Current implementation does not take into account recalls, but this will change in a future update. For failed transactions, current implementation does not return any balance changes (not even the fee payments). This will also change in a future update. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_version** | [**StateVersion**](StateVersion.md) |  | 
**proposer_timestamp_ms** | **int** | An integer between &#x60;0&#x60; and &#x60;10^14&#x60;, marking the proposer timestamp in ms. | 
**accumulator_hash** | **str** | The hex-encoded transaction accumulator hash. This hash captures the order of all transactions on ledger. This hash is &#x60;ACC_{N+1} &#x3D; combine(ACC_N, LEDGER_HASH_{N}))&#x60; (where &#x60;combine()&#x60; is an arbitrary deterministic function we use).  | 
**status** | [**LtsCommittedTransactionStatus**](LtsCommittedTransactionStatus.md) |  | 
**fungible_entity_balance_changes** | [**[LtsEntityFungibleBalanceChanges]**](LtsEntityFungibleBalanceChanges.md) | A list of all fungible balance updates which occurred in this transaction, aggregated by the global entity (such as account) which owns the vaults which were updated.  | 
**non_fungible_entity_balance_changes** | [**[LtsEntityNonFungibleBalanceChanges]**](LtsEntityNonFungibleBalanceChanges.md) | Non fungible changes per entity and resource  | 
**resultant_account_fungible_balances** | [**[LtsResultantAccountFungibleBalances]**](LtsResultantAccountFungibleBalances.md) | A list of the resultant fungible account balances for any balances which changed in this transaction. Only balances for accounts are returned, not any other kind of entity.  | 
**total_fee** | **str** | The string-encoded decimal representing the total amount of XRD payed as fee (execution, validator tip and royalties). A decimal is formed of some signed integer &#x60;m&#x60; of attos (&#x60;10^(-18)&#x60;) units, where &#x60;-2^(192 - 1) &lt;&#x3D; m &lt; 2^(192 - 1)&#x60;.  | 
**user_transaction_identifiers** | [**TransactionIdentifiers**](TransactionIdentifiers.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


