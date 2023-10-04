# core_client.TransactionApi

All URIs are relative to *http://localhost:3333/core*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_call_preview_post**](TransactionApi.md#transaction_call_preview_post) | **POST** /transaction/call-preview | Scrypto Call Preview
[**transaction_parse_post**](TransactionApi.md#transaction_parse_post) | **POST** /transaction/parse | Parse Transaction Payload
[**transaction_preview_post**](TransactionApi.md#transaction_preview_post) | **POST** /transaction/preview | Transaction Preview
[**transaction_receipt_post**](TransactionApi.md#transaction_receipt_post) | **POST** /transaction/receipt | Get Transaction Receipt
[**transaction_status_post**](TransactionApi.md#transaction_status_post) | **POST** /transaction/status | Get Transaction Status
[**transaction_submit_post**](TransactionApi.md#transaction_submit_post) | **POST** /transaction/submit | Transaction Submit


# **transaction_call_preview_post**
> TransactionCallPreviewResponse transaction_call_preview_post(transaction_call_preview_request)

Scrypto Call Preview

Preview a scrypto function or method call against the latest network state. Returns the result of the scrypto function or method call. 

### Example

```python
import time
import core_client
from core_client.api import transaction_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.transaction_call_preview_request import TransactionCallPreviewRequest
from core_client.model.transaction_call_preview_response import TransactionCallPreviewResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    transaction_call_preview_request = TransactionCallPreviewRequest(
        network="{{network}}",
        target=TargetIdentifier(),
        arguments=[
            "arguments_example",
        ],
    ) # TransactionCallPreviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Scrypto Call Preview
        api_response = api_instance.transaction_call_preview_post(transaction_call_preview_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionApi->transaction_call_preview_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_call_preview_request** | [**TransactionCallPreviewRequest**](TransactionCallPreviewRequest.md)|  |

### Return type

[**TransactionCallPreviewResponse**](TransactionCallPreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of the scrypto function call |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_parse_post**
> TransactionParseResponse transaction_parse_post(transaction_parse_request)

Parse Transaction Payload

Extracts the contents and hashes of various types of transaction payloads, or sub-payloads.

### Example

```python
import time
import core_client
from core_client.api import transaction_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.transaction_parse_response import TransactionParseResponse
from core_client.model.transaction_parse_request import TransactionParseRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    transaction_parse_request = TransactionParseRequest(
        network="{{network}}",
        payload_hex="payload_hex_example",
        parse_mode="Any",
        validation_mode="None",
        response_mode="Basic",
        transaction_format_options=TransactionFormatOptions(
            manifest=True,
            blobs=True,
            message=True,
            raw_system_transaction=True,
            raw_notarized_transaction=True,
            raw_ledger_transaction=True,
        ),
    ) # TransactionParseRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Parse Transaction Payload
        api_response = api_instance.transaction_parse_post(transaction_parse_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionApi->transaction_parse_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_parse_request** | [**TransactionParseRequest**](TransactionParseRequest.md)|  |

### Return type

[**TransactionParseResponse**](TransactionParseResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction Parse Response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_preview_post**
> TransactionPreviewResponse transaction_preview_post(transaction_preview_request)

Transaction Preview

Preview a transaction against the latest network state, and returns the preview receipt. 

### Example

```python
import time
import core_client
from core_client.api import transaction_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.transaction_preview_request import TransactionPreviewRequest
from core_client.model.transaction_preview_response import TransactionPreviewResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    transaction_preview_request = TransactionPreviewRequest(
        network="{{network}}",
        manifest="manifest_example",
        blobs_hex=[
            "blobs_hex_example",
        ],
        start_epoch_inclusive=0,
        end_epoch_exclusive=0,
        notary_public_key=PublicKey(),
        notary_is_signatory=True,
        tip_percentage=0,
        nonce=0,
        signer_public_keys=[
            PublicKey(),
        ],
        message=TransactionMessage(),
        flags=TransactionPreviewRequestFlags(
            use_free_credit=True,
            assume_all_signature_proofs=True,
            skip_epoch_check=True,
        ),
    ) # TransactionPreviewRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Transaction Preview
        api_response = api_instance.transaction_preview_post(transaction_preview_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionApi->transaction_preview_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_preview_request** | [**TransactionPreviewRequest**](TransactionPreviewRequest.md)|  |

### Return type

[**TransactionPreviewResponse**](TransactionPreviewResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction preview response |  -  |
**400** | Client error |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_receipt_post**
> TransactionReceiptResponse transaction_receipt_post(transaction_receipt_request)

Get Transaction Receipt

Gets the transaction receipt for a committed transaction. 

### Example

```python
import time
import core_client
from core_client.api import transaction_api
from core_client.model.transaction_receipt_response import TransactionReceiptResponse
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.transaction_receipt_request import TransactionReceiptRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    transaction_receipt_request = TransactionReceiptRequest(
        network="{{network}}",
        intent_hash="intent_hash_example",
    ) # TransactionReceiptRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Receipt
        api_response = api_instance.transaction_receipt_post(transaction_receipt_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionApi->transaction_receipt_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_receipt_request** | [**TransactionReceiptRequest**](TransactionReceiptRequest.md)|  |

### Return type

[**TransactionReceiptResponse**](TransactionReceiptResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Committed transaction found response |  -  |
**400** | Client error |  -  |
**404** | Committed transaction not found response |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transaction_status_post**
> TransactionStatusResponse transaction_status_post(transaction_status_request)

Get Transaction Status

Shares the node's knowledge of any payloads associated with the given intent hash. Generally there will be a single payload for a given intent, but it's theoretically possible there may be multiple. This knowledge is summarised into a status for the intent. This summarised status in the response is likely sufficient for most clients. 

### Example

```python
import time
import core_client
from core_client.api import transaction_api
from core_client.model.basic_error_response import BasicErrorResponse
from core_client.model.transaction_status_request import TransactionStatusRequest
from core_client.model.transaction_status_response import TransactionStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    transaction_status_request = TransactionStatusRequest(
        network="{{network}}",
        intent_hash="intent_hash_example",
    ) # TransactionStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Status
        api_response = api_instance.transaction_status_post(transaction_status_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionApi->transaction_status_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_status_request** | [**TransactionStatusRequest**](TransactionStatusRequest.md)|  |

### Return type

[**TransactionStatusResponse**](TransactionStatusResponse.md)

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

# **transaction_submit_post**
> TransactionSubmitResponse transaction_submit_post(transaction_submit_request)

Transaction Submit

Submits a notarized transaction to the network. Returns whether the transaction submission was already included in the node's mempool. 

### Example

```python
import time
import core_client
from core_client.api import transaction_api
from core_client.model.transaction_submit_request import TransactionSubmitRequest
from core_client.model.transaction_submit_error_response import TransactionSubmitErrorResponse
from core_client.model.transaction_submit_response import TransactionSubmitResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333/core
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333/core"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = transaction_api.TransactionApi(api_client)
    transaction_submit_request = TransactionSubmitRequest(
        network="{{network}}",
        notarized_transaction_hex="notarized_transaction_hex_example",
        force_recalculate=True,
    ) # TransactionSubmitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Transaction Submit
        api_response = api_instance.transaction_submit_post(transaction_submit_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling TransactionApi->transaction_submit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_submit_request** | [**TransactionSubmitRequest**](TransactionSubmitRequest.md)|  |

### Return type

[**TransactionSubmitResponse**](TransactionSubmitResponse.md)

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

