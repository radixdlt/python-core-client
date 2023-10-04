# core_client.MempoolApi

All URIs are relative to *http://localhost:3333/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mempool_list_post**](MempoolApi.md#mempool_list_post) | **POST** /mempool/list | Get Mempool List
[**mempool_transaction_post**](MempoolApi.md#mempool_transaction_post) | **POST** /mempool/transaction | Get Mempool Transaction


# **mempool_list_post**
> MempoolListResponse mempool_list_post(mempool_list_request)

Get Mempool List

Returns the hashes of all the transactions currently in the mempool

### Example

```python
import time
import core_client
from core_client.api import mempool_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.mempool_list_response import MempoolListResponse
from core_client.model.mempool_list_request import MempoolListRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mempool_api.MempoolApi(api_client)
    mempool_list_request = MempoolListRequest(
        network="{{network}}",
    ) # MempoolListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Mempool List
        api_response = api_instance.mempool_list_post(mempool_list_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling MempoolApi->mempool_list_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mempool_list_request** | [**MempoolListRequest**](MempoolListRequest.md)|  |

### Return type

[**MempoolListResponse**](MempoolListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mempool List Response |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mempool_transaction_post**
> MempoolTransactionResponse mempool_transaction_post(mempool_transaction_request)

Get Mempool Transaction

Returns the payload of a transaction currently in the mempool

### Example

```python
import time
import core_client
from core_client.api import mempool_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.mempool_transaction_request import MempoolTransactionRequest
from core_client.model.mempool_transaction_response import MempoolTransactionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mempool_api.MempoolApi(api_client)
    mempool_transaction_request = MempoolTransactionRequest(
        network="{{network}}",
        payload_hashes=[
            "payload_hashes_example",
        ],
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
**200** | Mempool Transaction Response |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

