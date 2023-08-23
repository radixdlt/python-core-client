# core_client.StatusApi

All URIs are relative to *http://localhost:3333/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_network_configuration_post**](StatusApi.md#status_network_configuration_post) | **POST** /status/network-configuration | Get Network Configuration
[**status_network_status_post**](StatusApi.md#status_network_status_post) | **POST** /status/network-status | Get Network Status
[**status_scenarios_post**](StatusApi.md#status_scenarios_post) | **POST** /status/scenarios | Get Scenarios&#39; results.


# **status_network_configuration_post**
> NetworkConfigurationResponse status_network_configuration_post()

Get Network Configuration

Returns the network configuration of the network the node is connected to.

### Example

```python
import time
import core_client
from core_client.api import status_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.network_configuration_response import NetworkConfigurationResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Network Configuration
        api_response = api_instance.status_network_configuration_post()
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StatusApi->status_network_configuration_post: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkConfigurationResponse**](NetworkConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Configuration |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_network_status_post**
> NetworkStatusResponse status_network_status_post(network_status_request)

Get Network Status

Returns the current state and status of the node's copy of the ledger.

### Example

```python
import time
import core_client
from core_client.api import status_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.network_status_response import NetworkStatusResponse
from core_client.model.network_status_request import NetworkStatusRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)
    network_status_request = NetworkStatusRequest(
        network="{{network}}",
    ) # NetworkStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Network Status
        api_response = api_instance.status_network_status_post(network_status_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StatusApi->status_network_status_post: %s\n" % e)
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
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_scenarios_post**
> ScenariosResponse status_scenarios_post(scenarios_request)

Get Scenarios' results.

Get results of test-oriented \"Genesis Scenarios\" executed on this Network.

### Example

```python
import time
import core_client
from core_client.api import status_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.scenarios_response import ScenariosResponse
from core_client.model.scenarios_request import ScenariosRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = status_api.StatusApi(api_client)
    scenarios_request = ScenariosRequest(
        network="{{network}}",
    ) # ScenariosRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Scenarios' results.
        api_response = api_instance.status_scenarios_post(scenarios_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StatusApi->status_scenarios_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scenarios_request** | [**ScenariosRequest**](ScenariosRequest.md)|  |

### Return type

[**ScenariosResponse**](ScenariosResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scenarios&#39; results |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

