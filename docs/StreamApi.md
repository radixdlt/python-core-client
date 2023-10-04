# core_client.StreamApi

All URIs are relative to *http://localhost:3333/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_transactions_post**](StreamApi.md#stream_transactions_post) | **POST** /stream/transactions | Get Committed Transactions


# **stream_transactions_post**
> StreamTransactionsResponse stream_transactions_post(stream_transactions_request)

Get Committed Transactions

Returns the list of committed transactions. 

### Example

```python
import time
import core_client
from core_client.api import stream_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.stream_transactions_request import StreamTransactionsRequest
from core_client.model.stream_transactions_response import StreamTransactionsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stream_api.StreamApi(api_client)
    stream_transactions_request = StreamTransactionsRequest(
        network="{{network}}",
        from_state_version=StateVersion(1),
        limit=1,
        sbor_format_options=SborFormatOptions(
            raw=True,
            programmatic_json=True,
        ),
        transaction_format_options=TransactionFormatOptions(
            manifest=True,
            blobs=True,
            message=True,
            raw_system_transaction=True,
            raw_notarized_transaction=True,
            raw_ledger_transaction=True,
        ),
        substate_format_options=SubstateFormatOptions(
            raw=True,
            hash=True,
            typed=True,
            previous=True,
        ),
        include_proofs=True,
    ) # StreamTransactionsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Committed Transactions
        api_response = api_instance.stream_transactions_post(stream_transactions_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StreamApi->stream_transactions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream_transactions_request** | [**StreamTransactionsRequest**](StreamTransactionsRequest.md)|  |

### Return type

[**StreamTransactionsResponse**](StreamTransactionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Committed transactions response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

