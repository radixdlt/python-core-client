# core_client.NodeApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**node_identifiers_post**](NodeApi.md#node_identifiers_post) | **POST** /node/identifiers | Get the node&#39;s identifiers
[**node_sign_post**](NodeApi.md#node_sign_post) | **POST** /node/sign | Sign a transaction with the node&#39;s key


# **node_identifiers_post**
> NodeIdentifiersResponse node_identifiers_post(node_identifiers_request)

Get the node's identifiers

### Example

```python
import time
import core_client
from core_client.api import node_api
from core_client.model.node_identifiers_request import NodeIdentifiersRequest
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.node_identifiers_response import NodeIdentifiersResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = node_api.NodeApi(api_client)
    node_identifiers_request = NodeIdentifiersRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
    ) # NodeIdentifiersRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get the node's identifiers
        api_response = api_instance.node_identifiers_post(node_identifiers_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling NodeApi->node_identifiers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_identifiers_request** | [**NodeIdentifiersRequest**](NodeIdentifiersRequest.md)|  |

### Return type

[**NodeIdentifiersResponse**](NodeIdentifiersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An unsigned transaction |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **node_sign_post**
> NodeSignResponse node_sign_post(node_sign_request)

Sign a transaction with the node's key

### Example

```python
import time
import core_client
from core_client.api import node_api
from core_client.model.node_sign_response import NodeSignResponse
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.node_sign_request import NodeSignRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = node_api.NodeApi(api_client)
    node_sign_request = NodeSignRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        unsigned_transaction="unsigned_transaction_example",
        public_key=PublicKey(
            hex="hex_example",
        ),
    ) # NodeSignRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sign a transaction with the node's key
        api_response = api_instance.node_sign_post(node_sign_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling NodeApi->node_sign_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_sign_request** | [**NodeSignRequest**](NodeSignRequest.md)|  |

### Return type

[**NodeSignResponse**](NodeSignResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An unsigned transaction |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

