# core_client.KeyApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**key_list_post**](KeyApi.md#key_list_post) | **POST** /key/list | Get public keys
[**key_sign_post**](KeyApi.md#key_sign_post) | **POST** /key/sign | Sign transaction


# **key_list_post**
> KeyListResponse key_list_post(key_list_request)

Get public keys

### Example

```python
import time
import core_client
from core_client.api import key_api
from core_client.model.key_list_response import KeyListResponse
from core_client.model.key_list_request import KeyListRequest
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
    api_instance = key_api.KeyApi(api_client)
    key_list_request = KeyListRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
    ) # KeyListRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get public keys
        api_response = api_instance.key_list_post(key_list_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling KeyApi->key_list_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_list_request** | [**KeyListRequest**](KeyListRequest.md)|  |

### Return type

[**KeyListResponse**](KeyListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The node&#39;s public keys |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **key_sign_post**
> KeySignResponse key_sign_post(key_sign_request)

Sign transaction

### Example

```python
import time
import core_client
from core_client.api import key_api
from core_client.model.key_sign_response import KeySignResponse
from core_client.model.key_sign_request import KeySignRequest
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
    api_instance = key_api.KeyApi(api_client)
    key_sign_request = KeySignRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        unsigned_transaction="unsigned_transaction_example",
        public_key=PublicKey(
            hex="hex_example",
        ),
    ) # KeySignRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Sign transaction
        api_response = api_instance.key_sign_post(key_sign_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling KeyApi->key_sign_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_sign_request** | [**KeySignRequest**](KeySignRequest.md)|  |

### Return type

[**KeySignResponse**](KeySignResponse.md)

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

