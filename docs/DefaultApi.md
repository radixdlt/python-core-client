# system_client.DefaultApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prometheus_metrics_get**](DefaultApi.md#prometheus_metrics_get) | **GET** /prometheus/metrics | Get Prometheus Metrics
[**system_addressbook_get**](DefaultApi.md#system_addressbook_get) | **GET** /system/addressbook | Get Address Book
[**system_configuration_get**](DefaultApi.md#system_configuration_get) | **GET** /system/configuration | Get Configuration
[**system_health_get**](DefaultApi.md#system_health_get) | **GET** /system/health | Get Health
[**system_metrics_get**](DefaultApi.md#system_metrics_get) | **GET** /system/metrics | Get Metrics
[**system_peers_get**](DefaultApi.md#system_peers_get) | **GET** /system/peers | Get Peers
[**system_version_get**](DefaultApi.md#system_version_get) | **GET** /system/version | Get Version


# **prometheus_metrics_get**
> str prometheus_metrics_get()

Get Prometheus Metrics

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Prometheus Metrics
        api_response = api_instance.prometheus_metrics_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->prometheus_metrics_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Prometheus Metrics |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_addressbook_get**
> SystemAddressBookResponse system_addressbook_get()

Get Address Book

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.system_address_book_response import SystemAddressBookResponse
from system_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Address Book
        api_response = api_instance.system_addressbook_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->system_addressbook_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemAddressBookResponse**](SystemAddressBookResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Address Book |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_configuration_get**
> SystemConfigurationResponse system_configuration_get()

Get Configuration

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.system_configuration_response import SystemConfigurationResponse
from system_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Configuration
        api_response = api_instance.system_configuration_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->system_configuration_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemConfigurationResponse**](SystemConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System Configuration |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_health_get**
> HealthResponse system_health_get()

Get Health

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.error import Error
from system_client.model.health_response import HealthResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Health
        api_response = api_instance.system_health_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->system_health_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**HealthResponse**](HealthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_metrics_get**
> SystemMetricsResponse system_metrics_get()

Get Metrics

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.error import Error
from system_client.model.system_metrics_response import SystemMetricsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Metrics
        api_response = api_instance.system_metrics_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->system_metrics_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemMetricsResponse**](SystemMetricsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | System Metrics |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_peers_get**
> SystemPeersResponse system_peers_get()

Get Peers

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.system_peers_response import SystemPeersResponse
from system_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Peers
        api_response = api_instance.system_peers_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->system_peers_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemPeersResponse**](SystemPeersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Peers |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_version_get**
> VersionResponse system_version_get()

Get Version

### Example

```python
import time
import system_client
from system_client.api import default_api
from system_client.model.error import Error
from system_client.model.version_response import VersionResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = system_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with system_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Version
        api_response = api_instance.system_version_get()
        pprint(api_response)
    except system_client.ApiException as e:
        print("Exception when calling DefaultApi->system_version_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Version |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

