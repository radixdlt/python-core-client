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
from core_client.model.key_list_request import KeyListRequest
from core_client.model.key_list_response import KeyListResponse
from core_client.model.key_sign_request import KeySignRequest
from core_client.model.key_sign_response import KeySignResponse
from core_client.model.unexpected_error import UnexpectedError
from core_client.model.update_vote_request import UpdateVoteRequest
from core_client.model.update_vote_response import UpdateVoteResponse


class KeyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __key_list_post(
            self,
            key_list_request,
            **kwargs
        ):
            """Get public keys  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.key_list_post(key_list_request, async_req=True)
            >>> result = thread.get()

            Args:
                key_list_request (KeyListRequest):

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
                KeyListResponse
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
            kwargs['key_list_request'] = \
                key_list_request
            return self.call_with_http_info(**kwargs)

        self.key_list_post = _Endpoint(
            settings={
                'response_type': (KeyListResponse,),
                'auth': [],
                'endpoint_path': '/key/list',
                'operation_id': 'key_list_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'key_list_request',
                ],
                'required': [
                    'key_list_request',
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
                    'key_list_request':
                        (KeyListRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'key_list_request': 'body',
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
            callable=__key_list_post
        )

        def __key_sign_post(
            self,
            key_sign_request,
            **kwargs
        ):
            """Sign transaction  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.key_sign_post(key_sign_request, async_req=True)
            >>> result = thread.get()

            Args:
                key_sign_request (KeySignRequest):

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
                KeySignResponse
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
            kwargs['key_sign_request'] = \
                key_sign_request
            return self.call_with_http_info(**kwargs)

        self.key_sign_post = _Endpoint(
            settings={
                'response_type': (KeySignResponse,),
                'auth': [],
                'endpoint_path': '/key/sign',
                'operation_id': 'key_sign_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'key_sign_request',
                ],
                'required': [
                    'key_sign_request',
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
                    'key_sign_request':
                        (KeySignRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'key_sign_request': 'body',
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
            callable=__key_sign_post
        )

        def __key_vote_post(
            self,
            update_vote_request,
            **kwargs
        ):
            """Vote for the candidate fork (if present)  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.key_vote_post(update_vote_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_vote_request (UpdateVoteRequest):

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
                UpdateVoteResponse
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
            kwargs['update_vote_request'] = \
                update_vote_request
            return self.call_with_http_info(**kwargs)

        self.key_vote_post = _Endpoint(
            settings={
                'response_type': (UpdateVoteResponse,),
                'auth': [],
                'endpoint_path': '/key/vote',
                'operation_id': 'key_vote_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_vote_request',
                ],
                'required': [
                    'update_vote_request',
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
                    'update_vote_request':
                        (UpdateVoteRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'update_vote_request': 'body',
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
            callable=__key_vote_post
        )

        def __key_withdraw_vote_post(
            self,
            update_vote_request,
            **kwargs
        ):
            """Withdraw the vote for the candidate fork  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.key_withdraw_vote_post(update_vote_request, async_req=True)
            >>> result = thread.get()

            Args:
                update_vote_request (UpdateVoteRequest):

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
                UpdateVoteResponse
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
            kwargs['update_vote_request'] = \
                update_vote_request
            return self.call_with_http_info(**kwargs)

        self.key_withdraw_vote_post = _Endpoint(
            settings={
                'response_type': (UpdateVoteResponse,),
                'auth': [],
                'endpoint_path': '/key/withdraw-vote',
                'operation_id': 'key_withdraw_vote_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'update_vote_request',
                ],
                'required': [
                    'update_vote_request',
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
                    'update_vote_request':
                        (UpdateVoteRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'update_vote_request': 'body',
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
            callable=__key_withdraw_vote_post
        )
