# core_client.EngineApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**engine_configuration_post**](EngineApi.md#engine_configuration_post) | **POST** /engine/configuration | Get Engine Configuration
[**engine_forks_voting_results_post**](EngineApi.md#engine_forks_voting_results_post) | **POST** /engine/forks-voting-results | Get forks voting results for the given epoch
[**engine_status_post**](EngineApi.md#engine_status_post) | **POST** /engine/status | Get Engine Current Status


# **engine_configuration_post**
> EngineConfigurationResponse engine_configuration_post(engine_configuration_request)

Get Engine Configuration

### Example

```python
import time
import core_client
from core_client.api import engine_api
from core_client.model.engine_configuration_response import EngineConfigurationResponse
from core_client.model.engine_configuration_request import EngineConfigurationRequest
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
    api_instance = engine_api.EngineApi(api_client)
    engine_configuration_request = EngineConfigurationRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
    ) # EngineConfigurationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Engine Configuration
        api_response = api_instance.engine_configuration_post(engine_configuration_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling EngineApi->engine_configuration_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_configuration_request** | [**EngineConfigurationRequest**](EngineConfigurationRequest.md)|  |

### Return type

[**EngineConfigurationResponse**](EngineConfigurationResponse.md)

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

# **engine_forks_voting_results_post**
> ForksVotingResultsResponse engine_forks_voting_results_post(forks_voting_results_request)

Get forks voting results for the given epoch

### Example

```python
import time
import core_client
from core_client.api import engine_api
from core_client.model.forks_voting_results_request import ForksVotingResultsRequest
from core_client.model.forks_voting_results_response import ForksVotingResultsResponse
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
    api_instance = engine_api.EngineApi(api_client)
    forks_voting_results_request = ForksVotingResultsRequest(
        epoch=1,
    ) # ForksVotingResultsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get forks voting results for the given epoch
        api_response = api_instance.engine_forks_voting_results_post(forks_voting_results_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling EngineApi->engine_forks_voting_results_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forks_voting_results_request** | [**ForksVotingResultsRequest**](ForksVotingResultsRequest.md)|  |

### Return type

[**ForksVotingResultsResponse**](ForksVotingResultsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Forks voting results for the given epoch |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **engine_status_post**
> EngineStatusResponse engine_status_post(engine_status_request)

Get Engine Current Status

### Example

```python
import time
import core_client
from core_client.api import engine_api
from core_client.model.engine_status_request import EngineStatusRequest
from core_client.model.engine_status_response import EngineStatusResponse
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
    api_instance = engine_api.EngineApi(api_client)
    engine_status_request = EngineStatusRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
    ) # EngineStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Engine Current Status
        api_response = api_instance.engine_status_post(engine_status_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling EngineApi->engine_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **engine_status_request** | [**EngineStatusRequest**](EngineStatusRequest.md)|  |

### Return type

[**EngineStatusResponse**](EngineStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Engine Status |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

