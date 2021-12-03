# core_client.TransactionsApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactions_post**](TransactionsApi.md#transactions_post) | **POST** /transactions | Get Committed Transactions


# **transactions_post**
> CommittedTransactionsResponse transactions_post(committed_transactions_request)

Get Committed Transactions

Returns an ordered sublist of committed transactions. This endpoint is designed for lite clients to sync with the state of the ledger.  The example response demonstrates a transfer transaction.  There is a more detailed worked example of reading this endpoint in the examples section. 

### Example

```python
import time
import core_client
from core_client.api import transactions_api
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.committed_transactions_response import CommittedTransactionsResponse
from core_client.model.committed_transactions_request import CommittedTransactionsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transactions_api.TransactionsApi(api_client)
    committed_transactions_request = CommittedTransactionsRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        state_identifier=PartialStateIdentifier(
            state_version=1,
            transaction_accumulator="transaction_accumulator_example",
        ),
        limit=1,
    ) # CommittedTransactionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Committed Transactions
        api_response = api_instance.transactions_post(committed_transactions_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionsApi->transactions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **committed_transactions_request** | [**CommittedTransactionsRequest**](CommittedTransactionsRequest.md)|  |

### Return type

[**CommittedTransactionsResponse**](CommittedTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sublist of Committed Transactions |  -  |
**500** | An Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

