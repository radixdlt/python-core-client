"""
    Radix Core API

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import re  # noqa: F401
import sys  # noqa: F401

from core_client.api_client import ApiClient, Endpoint as _Endpoint
from core_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from core_client.model.construction_build_request import ConstructionBuildRequest
from core_client.model.construction_build_response import ConstructionBuildResponse
from core_client.model.construction_derive_request import ConstructionDeriveRequest
from core_client.model.construction_derive_response import ConstructionDeriveResponse
from core_client.model.construction_finalize_request import ConstructionFinalizeRequest
from core_client.model.construction_finalize_response import ConstructionFinalizeResponse
from core_client.model.construction_hash_request import ConstructionHashRequest
from core_client.model.construction_hash_response import ConstructionHashResponse
from core_client.model.construction_parse_request import ConstructionParseRequest
from core_client.model.construction_parse_response import ConstructionParseResponse
from core_client.model.construction_submit_request import ConstructionSubmitRequest
from core_client.model.construction_submit_response import ConstructionSubmitResponse
from core_client.model.unexpected_error import UnexpectedError


class ConstructionApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __construction_build_post(
            self,
            construction_build_request,
            **kwargs
        ):
            """Build Transaction  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.construction_build_post(construction_build_request, async_req=True)
            >>> result = thread.get()

            Args:
                construction_build_request (ConstructionBuildRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ConstructionBuildResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['construction_build_request'] = \
                construction_build_request
            return self.call_with_http_info(**kwargs)

        self.construction_build_post = _Endpoint(
            settings={
                'response_type': (ConstructionBuildResponse,),
                'auth': [],
                'endpoint_path': '/construction/build',
                'operation_id': 'construction_build_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'construction_build_request',
                ],
                'required': [
                    'construction_build_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'construction_build_request':
                        (ConstructionBuildRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'construction_build_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__construction_build_post
        )

        def __construction_derive_post(
            self,
            construction_derive_request,
            **kwargs
        ):
            """Derive Entity Identifier  # noqa: E501

            Returns the entity identifier for an account, validator, or token given a public key  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.construction_derive_post(construction_derive_request, async_req=True)
            >>> result = thread.get()

            Args:
                construction_derive_request (ConstructionDeriveRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ConstructionDeriveResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['construction_derive_request'] = \
                construction_derive_request
            return self.call_with_http_info(**kwargs)

        self.construction_derive_post = _Endpoint(
            settings={
                'response_type': (ConstructionDeriveResponse,),
                'auth': [],
                'endpoint_path': '/construction/derive',
                'operation_id': 'construction_derive_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'construction_derive_request',
                ],
                'required': [
                    'construction_derive_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'construction_derive_request':
                        (ConstructionDeriveRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'construction_derive_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__construction_derive_post
        )

        def __construction_finalize_post(
            self,
            construction_finalize_request,
            **kwargs
        ):
            """Finalize Transaction  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.construction_finalize_post(construction_finalize_request, async_req=True)
            >>> result = thread.get()

            Args:
                construction_finalize_request (ConstructionFinalizeRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ConstructionFinalizeResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['construction_finalize_request'] = \
                construction_finalize_request
            return self.call_with_http_info(**kwargs)

        self.construction_finalize_post = _Endpoint(
            settings={
                'response_type': (ConstructionFinalizeResponse,),
                'auth': [],
                'endpoint_path': '/construction/finalize',
                'operation_id': 'construction_finalize_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'construction_finalize_request',
                ],
                'required': [
                    'construction_finalize_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'construction_finalize_request':
                        (ConstructionFinalizeRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'construction_finalize_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__construction_finalize_post
        )

        def __construction_hash_post(
            self,
            construction_hash_request,
            **kwargs
        ):
            """Get Transaction Hash  # noqa: E501

            Get the transaction identifier of a signed transaction  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.construction_hash_post(construction_hash_request, async_req=True)
            >>> result = thread.get()

            Args:
                construction_hash_request (ConstructionHashRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ConstructionHashResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['construction_hash_request'] = \
                construction_hash_request
            return self.call_with_http_info(**kwargs)

        self.construction_hash_post = _Endpoint(
            settings={
                'response_type': (ConstructionHashResponse,),
                'auth': [],
                'endpoint_path': '/construction/hash',
                'operation_id': 'construction_hash_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'construction_hash_request',
                ],
                'required': [
                    'construction_hash_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'construction_hash_request':
                        (ConstructionHashRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'construction_hash_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__construction_hash_post
        )

        def __construction_parse_post(
            self,
            construction_parse_request,
            **kwargs
        ):
            """Parse Transaction  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.construction_parse_post(construction_parse_request, async_req=True)
            >>> result = thread.get()

            Args:
                construction_parse_request (ConstructionParseRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ConstructionParseResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['construction_parse_request'] = \
                construction_parse_request
            return self.call_with_http_info(**kwargs)

        self.construction_parse_post = _Endpoint(
            settings={
                'response_type': (ConstructionParseResponse,),
                'auth': [],
                'endpoint_path': '/construction/parse',
                'operation_id': 'construction_parse_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'construction_parse_request',
                ],
                'required': [
                    'construction_parse_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'construction_parse_request':
                        (ConstructionParseRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'construction_parse_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__construction_parse_post
        )

        def __construction_submit_post(
            self,
            construction_submit_request,
            **kwargs
        ):
            """Submit Transaction  # noqa: E501

            Submit a transaction to the mempool  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.construction_submit_post(construction_submit_request, async_req=True)
            >>> result = thread.get()

            Args:
                construction_submit_request (ConstructionSubmitRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ConstructionSubmitResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['construction_submit_request'] = \
                construction_submit_request
            return self.call_with_http_info(**kwargs)

        self.construction_submit_post = _Endpoint(
            settings={
                'response_type': (ConstructionSubmitResponse,),
                'auth': [],
                'endpoint_path': '/construction/submit',
                'operation_id': 'construction_submit_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'construction_submit_request',
                ],
                'required': [
                    'construction_submit_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'construction_submit_request':
                        (ConstructionSubmitRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'construction_submit_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__construction_submit_post
        )
