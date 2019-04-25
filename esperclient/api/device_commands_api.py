# coding: utf-8

"""
    Esper Manage API

    # Introduction Esper Manage APIs for Cloud are a set of REST-based APIs that help you programmatically control and monitor your enterprise's dedicated Esper endpoint. Using these APIs, one can orchestrate & manage devices that have been provisioned against your endpoint. Furthermore, this API allows you to manage android applications that get installed on such devices. To read more about the various capabilities of Esper endpoints and Esper managed devices, please visit [esper.io](https://esper.io). This guide describes all the available APIs in detail, along with code samples for you to quickly ramp up to using them.  You can find out more about Esper at [https://esper.io](https://esper.io)  We've done our best to keep this document up to date, but if you find any issues, please reach out to us at developer@esper.io.  # SDK    You are welcome to use your favorite HTTP/REST library for your programming language in order to use these APIs, or you can use our official SDK (currently available in [python](https://github.com/esper-io/esper-client-py)) to do so.   # Authentication Client needs to send authentication details to access APIs. Following authentication schemes are supported:  #### Basic Authentication Client can use username and password to authenticate. These are your developer account credentials. For example, the client sends HTTP requests with the Authorization header that contains the word `Basic` followed by a space and a base64-encoded string `username:password`. ##### Base64 encoding Bash  ``` echo 'username:password' | base64 ```  Powershell  ``` [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes(\"username:password\")) ```  **Example request** ```bash curl -X GET \\   https://DOMAIN.shoonyacloud.com/api/enterprise/<enterprise_id>/device/ \\   -H 'Authorization: Basic cl0ZWFkbWluOnNpdG1pbjEyMyQ=' \\   -H 'Content-Type: application/json' \\ ``` You can read more about basic authentication scheme  [here](https://swagger.io/docs/specification/authentication/basic-authentication/)  # Errors The API uses standard HTTP status codes to indicate success or failure. All error responses will have a JSON body in the following format  ``` {   \"errors\": [],   \"message\": \"error message\",   \"status\": 400 } ``` * `errors` -  List of error details * `message` - Error description * `status` - HTTP status code   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: developer@esper.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from esperclient.api_client import ApiClient


class DeviceCommandsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_device_command(self, command_id, **kwargs):  # noqa: E501
        """Get command information  # noqa: E501

        Returns DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_command(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: A UUID string identifying this device command. (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_device_command_with_http_info(command_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_device_command_with_http_info(command_id, **kwargs)  # noqa: E501
            return data

    def get_device_command_with_http_info(self, command_id, **kwargs):  # noqa: E501
        """Get command information  # noqa: E501

        Returns DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_device_command_with_http_info(command_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str command_id: A UUID string identifying this device command. (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_device_command" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params or
                params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `get_device_command`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v0/device-command/{command_id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceCommand',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def install_device_app(self, data, **kwargs):  # noqa: E501
        """Install an app on device  # noqa: E501

        Creates DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.install_device_app(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceCommandRequest data: (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.install_device_app_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.install_device_app_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def install_device_app_with_http_info(self, data, **kwargs):  # noqa: E501
        """Install an app on device  # noqa: E501

        Creates DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.install_device_app_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceCommandRequest data: (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method install_device_app" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `install_device_app`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/v0/device-command/install/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceCommand',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lock_device(self, data, **kwargs):  # noqa: E501
        """Lock a device  # noqa: E501

        Creates DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lock_device(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceCommandRequest data: (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lock_device_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.lock_device_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def lock_device_with_http_info(self, data, **kwargs):  # noqa: E501
        """Lock a device  # noqa: E501

        Creates DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lock_device_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceCommandRequest data: (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lock_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `lock_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/v0/device-command/lock/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceCommand',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reboot_device(self, data, **kwargs):  # noqa: E501
        """Reboot a device  # noqa: E501

        Creates DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reboot_device(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceCommandRequest data: (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.reboot_device_with_http_info(data, **kwargs)  # noqa: E501
        else:
            (data) = self.reboot_device_with_http_info(data, **kwargs)  # noqa: E501
            return data

    def reboot_device_with_http_info(self, data, **kwargs):  # noqa: E501
        """Reboot a device  # noqa: E501

        Creates DeviceCommand instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reboot_device_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeviceCommandRequest data: (required)
        :return: DeviceCommand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reboot_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in params or
                params['data'] is None):
            raise ValueError("Missing the required parameter `data` when calling `reboot_device`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basic_security']  # noqa: E501

        return self.api_client.call_api(
            '/v0/device-command/reboot/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeviceCommand',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
