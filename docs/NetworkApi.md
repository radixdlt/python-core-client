# core_client.NetworkApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_configuration_post**](NetworkApi.md#network_configuration_post) | **POST** /network/configuration | Get Network Configuration
[**network_status_post**](NetworkApi.md#network_status_post) | **POST** /network/status | Get Network Status


# **network_configuration_post**
> NetworkConfigurationResponse network_configuration_post(body)

Get Network Configuration

Returns the network configuration of the network the node is connected to.

### Example

```python
import time
import core_client
from core_client.api import network_api
from core_client.model.network_configuration_response import NetworkConfigurationResponse
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
    api_instance = network_api.NetworkApi(api_client)
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        # Get Network Configuration
        api_response = api_instance.network_configuration_post(body)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling NetworkApi->network_configuration_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

### Return type

[**NetworkConfigurationResponse**](NetworkConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Configuration |  -  |
**500** | An unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_status_post**
> NetworkStatusResponse network_status_post(network_status_request)

Get Network Status

Returns the current state and status of the node's copy of the ledger. If the node is syncing, the `current_state_X` responses may be behind the global ledger.

### Example

```python
import time
import core_client
from core_client.api import network_api
from core_client.model.network_status_response import NetworkStatusResponse
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.network_status_request import NetworkStatusRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = network_api.NetworkApi(api_client)
    network_status_request = NetworkStatusRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
    ) # NetworkStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Network Status
        api_response = api_instance.network_status_post(network_status_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling NetworkApi->network_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_status_request** | [**NetworkStatusRequest**](NetworkStatusRequest.md)|  |

### Return type

[**NetworkStatusResponse**](NetworkStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Status |  -  |
**500** | An Unexpected Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

