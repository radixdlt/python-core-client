# core_client.SignApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sign_post**](SignApi.md#sign_post) | **POST** /sign | Sign a transaction with the node&#39;s key


# **sign_post**
> SignResponse sign_post(sign_request)

Sign a transaction with the node's key

### Example

```python
import time
import core_client
from core_client.api import sign_api
from core_client.model.sign_response import SignResponse
from core_client.model.sign_request import SignRequest
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
    api_instance = sign_api.SignApi(api_client)
    sign_request = SignRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        unsigned_transaction="unsigned_transaction_example",
        public_key=PublicKey(
            hex="hex_example",
        ),
    ) # SignRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sign a transaction with the node's key
        api_response = api_instance.sign_post(sign_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling SignApi->sign_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_request** | [**SignRequest**](SignRequest.md)|  |

### Return type

[**SignResponse**](SignResponse.md)

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

