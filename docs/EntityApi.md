# core_client.EntityApi

All URIs are relative to *http://localhost:3333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**entity_post**](EntityApi.md#entity_post) | **POST** /entity | Get Entity Information


# **entity_post**
> EntityResponse entity_post(entity_request)

Get Entity Information

Gets the balances and data objects at an entity at the current state of the ledger.

### Example

```python
import time
import core_client
from core_client.api import entity_api
from core_client.model.entity_response import EntityResponse
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.entity_request import EntityRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:3333
# See configuration.py for a list of all supported configuration parameters.
configuration = core_client.Configuration(
    host = "http://localhost:3333"
)


# Enter a context with an instance of the API client
with core_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = entity_api.EntityApi(api_client)
    entity_request = EntityRequest(
        network_identifier=NetworkIdentifier(
            network="network_example",
        ),
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
    ) # EntityRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Get Entity Information
        api_response = api_instance.entity_post(entity_request)
        pprint(api_response)
    except core_client.ApiException as e:
        print("Exception when calling EntityApi->entity_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_request** | [**EntityRequest**](EntityRequest.md)|  |

### Return type

[**EntityResponse**](EntityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Entity Balances and Data |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

