# coding: utf-8

"""
    Esper SDK

    This is a read only Esper SDK.  You can find out more about Esper at [https://shoonya.io](https://shoonya.io).  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: developer@shoonya.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from esper.api_client import ApiClient


class DeviceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_devices(self, enterprise_id, **kwargs):  # noqa: E501
        """Find devices in an enterprise  # noqa: E501

        Returns a list of devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_devices(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :return: DeviceListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_devices_with_http_info(enterprise_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_devices_with_http_info(enterprise_id, **kwargs)  # noqa: E501
            return data

    def get_all_devices_with_http_info(self, enterprise_id, **kwargs):  # noqa: E501
        """Find devices in an enterprise  # noqa: E501

        Returns a list of devices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_devices_with_http_info(enterprise_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str enterprise_id: ID of the enterprise (required)
        :return: DeviceListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enterprise_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_devices" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enterprise_id' is set
        if ('enterprise_id' not in params or
                params['enterprise_id'] is None):
            raise ValueError("Missing the required parameter `enterprise_id` when calling `get_all_devices`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'enterprise_id' in params:
            path_params['enterprise_id'] = params['enterprise_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/enterprise/{enterprise_id}/device/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
