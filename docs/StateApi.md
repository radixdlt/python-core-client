# core_client.StateApi

All URIs are relative to *http://localhost:3333/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**state_access_controller_post**](StateApi.md#state_access_controller_post) | **POST** /state/access-controller | Get Access Controller Details
[**state_account_post**](StateApi.md#state_account_post) | **POST** /state/account | Get Account Details
[**state_component_post**](StateApi.md#state_component_post) | **POST** /state/component | Get Component Details
[**state_consensus_manager_post**](StateApi.md#state_consensus_manager_post) | **POST** /state/consensus-manager | Get Consensus Manager Details
[**state_non_fungible_post**](StateApi.md#state_non_fungible_post) | **POST** /state/non-fungible | Get Non-Fungible Details
[**state_package_post**](StateApi.md#state_package_post) | **POST** /state/package | Get Package Details
[**state_resource_post**](StateApi.md#state_resource_post) | **POST** /state/resource | Get Resource Details
[**state_validator_post**](StateApi.md#state_validator_post) | **POST** /state/validator | Get Validator Details


# **state_access_controller_post**
> StateAccessControllerResponse state_access_controller_post(state_access_controller_request)

Get Access Controller Details

Reads the access controller's substate/s from the top of the current ledger. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_access_controller_request import StateAccessControllerRequest
from core_client.model.state_access_controller_response import StateAccessControllerResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_access_controller_request = StateAccessControllerRequest(
        network="{{network}}",
        controller_address="controller_address_example",
    ) # StateAccessControllerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Access Controller Details
        api_response = api_instance.state_access_controller_post(state_access_controller_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_access_controller_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_access_controller_request** | [**StateAccessControllerRequest**](StateAccessControllerRequest.md)|  |

### Return type

[**StateAccessControllerResponse**](StateAccessControllerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_account_post**
> StateAccountResponse state_account_post(state_account_request)

Get Account Details

Reads the account's substate/s from the top of the current ledger. Also returns all vaults under the account. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.state_account_request import StateAccountRequest
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_account_response import StateAccountResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_account_request = StateAccountRequest(
        network="{{network}}",
        account_address="account_address_example",
    ) # StateAccountRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Account Details
        api_response = api_instance.state_account_post(state_account_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_account_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_account_request** | [**StateAccountRequest**](StateAccountRequest.md)|  |

### Return type

[**StateAccountResponse**](StateAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_component_post**
> StateComponentResponse state_component_post(state_component_request)

Get Component Details

Reads the component's substate/s from the top of the current ledger. Also recursively extracts vault balance totals from the component's entity subtree. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_component_response import StateComponentResponse
from core_client.model.state_component_request import StateComponentRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_component_request = StateComponentRequest(
        network="{{network}}",
        component_address="component_address_example",
    ) # StateComponentRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Component Details
        api_response = api_instance.state_component_post(state_component_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_component_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_component_request** | [**StateComponentRequest**](StateComponentRequest.md)|  |

### Return type

[**StateComponentResponse**](StateComponentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_consensus_manager_post**
> StateConsensusManagerResponse state_consensus_manager_post(state_consensus_manager_request)

Get Consensus Manager Details

Reads the consensus manager's substate/s from the top of the current ledger. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_consensus_manager_request import StateConsensusManagerRequest
from core_client.model.state_consensus_manager_response import StateConsensusManagerResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_consensus_manager_request = StateConsensusManagerRequest(
        network="{{network}}",
    ) # StateConsensusManagerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Consensus Manager Details
        api_response = api_instance.state_consensus_manager_post(state_consensus_manager_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_consensus_manager_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_consensus_manager_request** | [**StateConsensusManagerRequest**](StateConsensusManagerRequest.md)|  |

### Return type

[**StateConsensusManagerResponse**](StateConsensusManagerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_non_fungible_post**
> StateNonFungibleResponse state_non_fungible_post(state_non_fungible_request)

Get Non-Fungible Details

Reads the data associated with a single Non-Fungible Unit under a Non-Fungible Resource. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_non_fungible_response import StateNonFungibleResponse
from core_client.model.state_non_fungible_request import StateNonFungibleRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_non_fungible_request = StateNonFungibleRequest(
        network="{{network}}",
        resource_address="resource_address_example",
        non_fungible_id="non_fungible_id_example",
    ) # StateNonFungibleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Non-Fungible Details
        api_response = api_instance.state_non_fungible_post(state_non_fungible_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_non_fungible_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_non_fungible_request** | [**StateNonFungibleRequest**](StateNonFungibleRequest.md)|  |

### Return type

[**StateNonFungibleResponse**](StateNonFungibleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_package_post**
> StatePackageResponse state_package_post(state_package_request)

Get Package Details

Reads the package's substate/s from the top of the current ledger. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.state_package_response import StatePackageResponse
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_package_request import StatePackageRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_package_request = StatePackageRequest(
        network="{{network}}",
        package_address="package_address_example",
    ) # StatePackageRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Package Details
        api_response = api_instance.state_package_post(state_package_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_package_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_package_request** | [**StatePackageRequest**](StatePackageRequest.md)|  |

### Return type

[**StatePackageResponse**](StatePackageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_resource_post**
> StateResourceResponse state_resource_post(state_resource_request)

Get Resource Details

Reads the resource manager's substate/s from the top of the current ledger. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_resource_response import StateResourceResponse
from core_client.model.state_resource_request import StateResourceRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_resource_request = StateResourceRequest(
        network="{{network}}",
        resource_address="resource_address_example",
    ) # StateResourceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Resource Details
        api_response = api_instance.state_resource_post(state_resource_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_resource_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_resource_request** | [**StateResourceRequest**](StateResourceRequest.md)|  |

### Return type

[**StateResourceResponse**](StateResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **state_validator_post**
> StateValidatorResponse state_validator_post(state_validator_request)

Get Validator Details

Reads the validator's substate/s from the top of the current ledger. 

### Example

```python
import time
import core_client
from core_client.api import state_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.state_validator_response import StateValidatorResponse
from core_client.model.state_validator_request import StateValidatorRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = state_api.StateApi(api_client)
    state_validator_request = StateValidatorRequest(
        network="{{network}}",
        validator_address="validator_address_example",
    ) # StateValidatorRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Validator Details
        api_response = api_instance.state_validator_post(state_validator_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling StateApi->state_validator_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state_validator_request** | [**StateValidatorRequest**](StateValidatorRequest.md)|  |

### Return type

[**StateValidatorResponse**](StateValidatorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current state response |  -  |
**400** | Client error |  -  |
**404** | Not found error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

