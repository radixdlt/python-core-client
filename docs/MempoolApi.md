# core_client.MempoolApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mempool_post**](MempoolApi.md#mempool_post) | **POST** /mempool | Get Mempool Transactions
[**mempool_transaction_post**](MempoolApi.md#mempool_transaction_post) | **POST** /mempool/transaction | Get Mempool Transaction


# **mempool_post**
> MempoolResponse mempool_post(mempool_request)

Get Mempool Transactions

Gets the transaction identifiers in the mempool

### Example

```python
import time
import core_client
from core_client.api import mempool_api
from core_client.model.mempool_response import MempoolResponse
from core_client.model.mempool_request import MempoolRequest
from core_client.model.unexpected_error import UnexpectedError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mempool_api.MempoolApi(api_client)
    mempool_request = MempoolRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
    ) # MempoolRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Mempool Transactions
        api_response = api_instance.mempool_post(mempool_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling MempoolApi->mempool_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mempool_request** | [**MempoolRequest**](MempoolRequest.md)|  |

### Return type

[**MempoolResponse**](MempoolResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mempool Transaction Identifiers |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mempool_transaction_post**
> MempoolTransactionResponse mempool_transaction_post(mempool_transaction_request)

Get Mempool Transaction

Gets the transaction from the mempool

### Example

```python
import time
import core_client
from core_client.api import mempool_api
from core_client.model.mempool_transaction_request import MempoolTransactionRequest
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.mempool_transaction_response import MempoolTransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mempool_api.MempoolApi(api_client)
    mempool_transaction_request = MempoolTransactionRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        transaction_identifier=TransactionIdentifier(
            hash=TransactionIdentifierHash("bf325375e030fccba00917317c574773100bf03b5fc61486286e564b23e9566b"),
        ),
    ) # MempoolTransactionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Mempool Transaction
        api_response = api_instance.mempool_transaction_post(mempool_transaction_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling MempoolApi->mempool_transaction_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mempool_transaction_request** | [**MempoolTransactionRequest**](MempoolTransactionRequest.md)|  |

### Return type

[**MempoolTransactionResponse**](MempoolTransactionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mempool Transaction Identifiers |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

