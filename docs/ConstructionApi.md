# core_client.ConstructionApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**construction_build_post**](ConstructionApi.md#construction_build_post) | **POST** /construction/build | Build Transaction
[**construction_derive_post**](ConstructionApi.md#construction_derive_post) | **POST** /construction/derive | Derive Entity Identifier
[**construction_finalize_post**](ConstructionApi.md#construction_finalize_post) | **POST** /construction/finalize | Finalize Transaction
[**construction_hash_post**](ConstructionApi.md#construction_hash_post) | **POST** /construction/hash | Get Transaction Hash
[**construction_parse_post**](ConstructionApi.md#construction_parse_post) | **POST** /construction/parse | Parse Transaction
[**construction_submit_post**](ConstructionApi.md#construction_submit_post) | **POST** /construction/submit | Submit Transaction


# **construction_build_post**
> ConstructionBuildResponse construction_build_post(construction_build_request)

Build Transaction

### Example

```python
import time
import core_client
from core_client.api import construction_api
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.construction_build_response import ConstructionBuildResponse
from core_client.model.construction_build_request import ConstructionBuildRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = construction_api.ConstructionApi(api_client)
    construction_build_request = ConstructionBuildRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        operation_groups=[
            OperationGroup(
                operations=[
                    Operation(
                        type="type_example",
                        entity_identifier=EntityIdentifier(
                            address="address_example",
                            sub_entity=SubEntity(
                                address="address_example",
                                metadata=SubEntityMetadata(
                                    validator_address="validator_address_example",
                                    epoch_unlock=1,
                                ),
                            ),
                        ),
                        substate=Substate(
                            substate_operation="BOOTUP",
                            substate_identifier=SubstateIdentifier(
                                identifier="identifier_example",
                            ),
                        ),
                        amount=ResourceAmount(
                            value=BigInteger("-80728"),
                            resource_identifier=ResourceIdentifier(
                                type="type_example",
                            ),
                        ),
                        data=Data(
                            action="CREATE",
                            data_object=DataObject(
                                type="type_example",
                            ),
                        ),
                        metadata={},
                    ),
                ],
                metadata={},
            ),
        ],
        fee_payer=EntityIdentifier(
            address="address_example",
            sub_entity=SubEntity(
                address="address_example",
                metadata=SubEntityMetadata(
                    validator_address="validator_address_example",
                    epoch_unlock=1,
                ),
            ),
        ),
        message="message_example",
        disable_resource_allocate_and_destroy=True,
    ) # ConstructionBuildRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Build Transaction
        api_response = api_instance.construction_build_post(construction_build_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_build_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construction_build_request** | [**ConstructionBuildRequest**](ConstructionBuildRequest.md)|  |

### Return type

[**ConstructionBuildResponse**](ConstructionBuildResponse.md)

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

# **construction_derive_post**
> ConstructionDeriveResponse construction_derive_post(construction_derive_request)

Derive Entity Identifier

Returns the entity identifier for an account, validator, or token given a public key

### Example

```python
import time
import core_client
from core_client.api import construction_api
from core_client.model.construction_derive_request import ConstructionDeriveRequest
from core_client.model.construction_derive_response import ConstructionDeriveResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = construction_api.ConstructionApi(api_client)
    construction_derive_request = ConstructionDeriveRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        public_key=PublicKey(
            hex="hex_example",
        ),
        metadata=ConstructionDeriveRequestMetadata(
            type="type_example",
        ),
    ) # ConstructionDeriveRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Derive Entity Identifier
        api_response = api_instance.construction_derive_post(construction_derive_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_derive_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construction_derive_request** | [**ConstructionDeriveRequest**](ConstructionDeriveRequest.md)|  |

### Return type

[**ConstructionDeriveResponse**](ConstructionDeriveResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity Identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **construction_finalize_post**
> ConstructionFinalizeResponse construction_finalize_post(construction_finalize_request)

Finalize Transaction

### Example

```python
import time
import core_client
from core_client.api import construction_api
from core_client.model.construction_finalize_request import ConstructionFinalizeRequest
from core_client.model.construction_finalize_response import ConstructionFinalizeResponse
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
    api_instance = construction_api.ConstructionApi(api_client)
    construction_finalize_request = ConstructionFinalizeRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        unsigned_transaction="unsigned_transaction_example",
        signature=Signature(
            public_key=PublicKey(
                hex="hex_example",
            ),
            bytes="bytes_example",
        ),
    ) # ConstructionFinalizeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Finalize Transaction
        api_response = api_instance.construction_finalize_post(construction_finalize_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_finalize_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construction_finalize_request** | [**ConstructionFinalizeRequest**](ConstructionFinalizeRequest.md)|  |

### Return type

[**ConstructionFinalizeResponse**](ConstructionFinalizeResponse.md)

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

# **construction_hash_post**
> ConstructionHashResponse construction_hash_post(construction_hash_request)

Get Transaction Hash

Get the transaction identifier of a signed transaction

### Example

```python
import time
import core_client
from core_client.api import construction_api
from core_client.model.construction_hash_request import ConstructionHashRequest
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.construction_hash_response import ConstructionHashResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = construction_api.ConstructionApi(api_client)
    construction_hash_request = ConstructionHashRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        signed_transaction="signed_transaction_example",
    ) # ConstructionHashRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Transaction Hash
        api_response = api_instance.construction_hash_post(construction_hash_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_hash_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construction_hash_request** | [**ConstructionHashRequest**](ConstructionHashRequest.md)|  |

### Return type

[**ConstructionHashResponse**](ConstructionHashResponse.md)

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

# **construction_parse_post**
> ConstructionParseResponse construction_parse_post(construction_parse_request)

Parse Transaction

### Example

```python
import time
import core_client
from core_client.api import construction_api
from core_client.model.construction_parse_request import ConstructionParseRequest
from core_client.model.construction_parse_response import ConstructionParseResponse
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
    api_instance = construction_api.ConstructionApi(api_client)
    construction_parse_request = ConstructionParseRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        transaction="transaction_example",
        signed=True,
    ) # ConstructionParseRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Parse Transaction
        api_response = api_instance.construction_parse_post(construction_parse_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_parse_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construction_parse_request** | [**ConstructionParseRequest**](ConstructionParseRequest.md)|  |

### Return type

[**ConstructionParseResponse**](ConstructionParseResponse.md)

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

# **construction_submit_post**
> ConstructionSubmitResponse construction_submit_post(construction_submit_request)

Submit Transaction

Submit a transaction to the mempool

### Example

```python
import time
import core_client
from core_client.api import construction_api
from core_client.model.construction_submit_response import ConstructionSubmitResponse
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.construction_submit_request import ConstructionSubmitRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = construction_api.ConstructionApi(api_client)
    construction_submit_request = ConstructionSubmitRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
        signed_transaction="signed_transaction_example",
    ) # ConstructionSubmitRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Submit Transaction
        api_response = api_instance.construction_submit_post(construction_submit_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling ConstructionApi->construction_submit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **construction_submit_request** | [**ConstructionSubmitRequest**](ConstructionSubmitRequest.md)|  |

### Return type

[**ConstructionSubmitResponse**](ConstructionSubmitResponse.md)

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

