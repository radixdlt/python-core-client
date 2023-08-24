# core_client.LTSApi

All URIs are relative to *http://localhost:3333/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lts_state_account_all_fungible_resource_balances_post**](LTSApi.md#lts_state_account_all_fungible_resource_balances_post) | **POST** /lts/state/account-all-fungible-resource-balances | Get All Account Balances
[**lts_state_account_fungible_resource_balance_post**](LTSApi.md#lts_state_account_fungible_resource_balance_post) | **POST** /lts/state/account-fungible-resource-balance | Get Single Account Balance
[**lts_stream_account_transaction_outcomes_post**](LTSApi.md#lts_stream_account_transaction_outcomes_post) | **POST** /lts/stream/account-transaction-outcomes | Get Account Transaction Outcomes
[**lts_stream_transaction_outcomes_post**](LTSApi.md#lts_stream_transaction_outcomes_post) | **POST** /lts/stream/transaction-outcomes | Get Transaction Outcomes
[**lts_transaction_construction_post**](LTSApi.md#lts_transaction_construction_post) | **POST** /lts/transaction/construction | Get Construction Metadata
[**lts_transaction_status_post**](LTSApi.md#lts_transaction_status_post) | **POST** /lts/transaction/status | Get Transaction Status
[**lts_transaction_submit_post**](LTSApi.md#lts_transaction_submit_post) | **POST** /lts/transaction/submit | Submit Transaction


# **lts_state_account_all_fungible_resource_balances_post**
> LtsStateAccountAllFungibleResourceBalancesResponse lts_state_account_all_fungible_resource_balances_post(lts_state_account_all_fungible_resource_balances_request)

Get All Account Balances

Returns balances for all resources associated with an account

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.lts_state_account_all_fungible_resource_balances_request import LtsStateAccountAllFungibleResourceBalancesRequest
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_state_account_all_fungible_resource_balances_response import LtsStateAccountAllFungibleResourceBalancesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_state_account_all_fungible_resource_balances_request = LtsStateAccountAllFungibleResourceBalancesRequest(
        network="{{network}}",
        account_address="account_address_example",
    ) # LtsStateAccountAllFungibleResourceBalancesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get All Account Balances
        api_response = api_instance.lts_state_account_all_fungible_resource_balances_post(lts_state_account_all_fungible_resource_balances_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_state_account_all_fungible_resource_balances_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_state_account_all_fungible_resource_balances_request** | [**LtsStateAccountAllFungibleResourceBalancesRequest**](LtsStateAccountAllFungibleResourceBalancesRequest.md)|  |

### Return type

[**LtsStateAccountAllFungibleResourceBalancesResponse**](LtsStateAccountAllFungibleResourceBalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account all resource balances response |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lts_state_account_fungible_resource_balance_post**
> LtsStateAccountFungibleResourceBalanceResponse lts_state_account_fungible_resource_balance_post(lts_state_account_fungible_resource_balance_request)

Get Single Account Balance

Returns balance of a single fungible resource in an account

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_state_account_fungible_resource_balance_request import LtsStateAccountFungibleResourceBalanceRequest
from core_client.model.lts_state_account_fungible_resource_balance_response import LtsStateAccountFungibleResourceBalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_state_account_fungible_resource_balance_request = LtsStateAccountFungibleResourceBalanceRequest(
        network="{{network}}",
        account_address="account_address_example",
        resource_address="resource_address_example",
    ) # LtsStateAccountFungibleResourceBalanceRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Single Account Balance
        api_response = api_instance.lts_state_account_fungible_resource_balance_post(lts_state_account_fungible_resource_balance_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_state_account_fungible_resource_balance_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_state_account_fungible_resource_balance_request** | [**LtsStateAccountFungibleResourceBalanceRequest**](LtsStateAccountFungibleResourceBalanceRequest.md)|  |

### Return type

[**LtsStateAccountFungibleResourceBalanceResponse**](LtsStateAccountFungibleResourceBalanceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Account resource balance response |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lts_stream_account_transaction_outcomes_post**
> LtsStreamAccountTransactionOutcomesResponse lts_stream_account_transaction_outcomes_post(lts_stream_account_transaction_outcomes_request)

Get Account Transaction Outcomes

Returns a list of committed transaction outcomes (containing balance changes) from a given state version, filtered to only transactions which involved the given account. 

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_stream_account_transaction_outcomes_request import LtsStreamAccountTransactionOutcomesRequest
from core_client.model.lts_stream_account_transaction_outcomes_response import LtsStreamAccountTransactionOutcomesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_stream_account_transaction_outcomes_request = LtsStreamAccountTransactionOutcomesRequest(
        network="{{network}}",
        account_address="account_address_example",
        from_state_version=StateVersion(1),
        limit=1,
    ) # LtsStreamAccountTransactionOutcomesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Account Transaction Outcomes
        api_response = api_instance.lts_stream_account_transaction_outcomes_post(lts_stream_account_transaction_outcomes_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_stream_account_transaction_outcomes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_stream_account_transaction_outcomes_request** | [**LtsStreamAccountTransactionOutcomesRequest**](LtsStreamAccountTransactionOutcomesRequest.md)|  |

### Return type

[**LtsStreamAccountTransactionOutcomesResponse**](LtsStreamAccountTransactionOutcomesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lts_stream_transaction_outcomes_post**
> LtsStreamTransactionOutcomesResponse lts_stream_transaction_outcomes_post(lts_stream_transaction_outcomes_request)

Get Transaction Outcomes

Returns a list of committed transaction outcomes (containing balance changes) from a given state version. 

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_stream_transaction_outcomes_request import LtsStreamTransactionOutcomesRequest
from core_client.model.lts_stream_transaction_outcomes_response import LtsStreamTransactionOutcomesResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_stream_transaction_outcomes_request = LtsStreamTransactionOutcomesRequest(
        network="{{network}}",
        from_state_version=StateVersion(1),
        limit=1,
    ) # LtsStreamTransactionOutcomesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Outcomes
        api_response = api_instance.lts_stream_transaction_outcomes_post(lts_stream_transaction_outcomes_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_stream_transaction_outcomes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_stream_transaction_outcomes_request** | [**LtsStreamTransactionOutcomesRequest**](LtsStreamTransactionOutcomesRequest.md)|  |

### Return type

[**LtsStreamTransactionOutcomesResponse**](LtsStreamTransactionOutcomesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lts_transaction_construction_post**
> LtsTransactionConstructionResponse lts_transaction_construction_post(lts_transaction_construction_request)

Get Construction Metadata

Returns information necessary to build a transaction

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_transaction_construction_response import LtsTransactionConstructionResponse
from core_client.model.lts_transaction_construction_request import LtsTransactionConstructionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_transaction_construction_request = LtsTransactionConstructionRequest(
        network="{{network}}",
    ) # LtsTransactionConstructionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Construction Metadata
        api_response = api_instance.lts_transaction_construction_post(lts_transaction_construction_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_transaction_construction_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_transaction_construction_request** | [**LtsTransactionConstructionRequest**](LtsTransactionConstructionRequest.md)|  |

### Return type

[**LtsTransactionConstructionResponse**](LtsTransactionConstructionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All info needed to build a transaction |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lts_transaction_status_post**
> LtsTransactionStatusResponse lts_transaction_status_post(lts_transaction_status_request)

Get Transaction Status

Shares the node's knowledge of any payloads associated with the given intent hash. Generally there will be a single payload for a given intent, but it's theoretically possible there may be multiple. This knowledge is summarised into a status for the intent. This summarised status in the response is likely sufficient for most clients. 

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.lts_transaction_status_response import LtsTransactionStatusResponse
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.lts_transaction_status_request import LtsTransactionStatusRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_transaction_status_request = LtsTransactionStatusRequest(
        network="{{network}}",
        intent_hash=IntentHash("intent_hash_example"),
    ) # LtsTransactionStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Status
        api_response = api_instance.lts_transaction_status_post(lts_transaction_status_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_transaction_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_transaction_status_request** | [**LtsTransactionStatusRequest**](LtsTransactionStatusRequest.md)|  |

### Return type

[**LtsTransactionStatusResponse**](LtsTransactionStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction status response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lts_transaction_submit_post**
> LtsTransactionSubmitResponse lts_transaction_submit_post(lts_transaction_submit_request)

Submit Transaction

Submits a notarized transaction to the network. Returns whether the transaction submission was already included in the node's mempool. 

### Example

```python
import time
import core_client
from core_client.api import lts_api
from core_client.model.lts_transaction_submit_response import LtsTransactionSubmitResponse
from core_client.model.transaction_submit_error_response import TransactionSubmitErrorResponse
from core_client.model.lts_transaction_submit_request import LtsTransactionSubmitRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lts_api.LTSApi(api_client)
    lts_transaction_submit_request = LtsTransactionSubmitRequest(
        network="{{network}}",
        notarized_transaction_hex="notarized_transaction_hex_example",
        force_recalculate=True,
    ) # LtsTransactionSubmitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Submit Transaction
        api_response = api_instance.lts_transaction_submit_post(lts_transaction_submit_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling LTSApi->lts_transaction_submit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lts_transaction_submit_request** | [**LtsTransactionSubmitRequest**](LtsTransactionSubmitRequest.md)|  |

### Return type

[**LtsTransactionSubmitResponse**](LtsTransactionSubmitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction Submit Response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

