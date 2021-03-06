# coding: utf-8

"""
Esper Manage API

OpenAPI spec version: 1.0.0
Contact: developer@esper.io
---------------------------------------------------------

Copyright 2019 Shoonya Enterprises Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""



import pprint
import re

import six

from esperclient.models.device_app_permission import DeviceAppPermission


class DeviceApp(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'permissions': 'list[DeviceAppPermission]',
        'app_name': 'str',
        'package_name': 'str',
        'whitelisted': 'bool',
        'product_id': 'str',
        'version_code': 'str',
        'version_name': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool',
        'device': 'str'
    }

    attribute_map = {
        'id': 'id',
        'permissions': 'permissions',
        'app_name': 'app_name',
        'package_name': 'package_name',
        'whitelisted': 'whitelisted',
        'product_id': 'product_id',
        'version_code': 'version_code',
        'version_name': 'version_name',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active',
        'device': 'device'
    }

    def __init__(self, id=None, permissions=None, app_name=None, package_name=None, whitelisted=None, product_id=None, version_code=None, version_name=None, created_on=None, updated_on=None, is_active=None, device=None):
        """DeviceApp - a model defined in Swagger"""

        self._id = None
        self._permissions = None
        self._app_name = None
        self._package_name = None
        self._whitelisted = None
        self._product_id = None
        self._version_code = None
        self._version_name = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self._device = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if permissions is not None:
            self.permissions = permissions
        self.app_name = app_name
        self.package_name = package_name
        if whitelisted is not None:
            self.whitelisted = whitelisted
        if product_id is not None:
            self.product_id = product_id
        if version_code is not None:
            self.version_code = version_code
        if version_name is not None:
            self.version_name = version_name
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active
        self.device = device

    @property
    def id(self):
        """Gets the id of this DeviceApp.


        :return: The id of this DeviceApp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceApp.


        :param id: The id of this DeviceApp.
        :type: str
        """

        self._id = id

    @property
    def permissions(self):
        """Gets the permissions of this DeviceApp.


        :return: The permissions of this DeviceApp.
        :rtype: list[DeviceAppPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this DeviceApp.


        :param permissions: The permissions of this DeviceApp.
        :type: list[DeviceAppPermission]
        """

        self._permissions = permissions

    @property
    def app_name(self):
        """Gets the app_name of this DeviceApp.


        :return: The app_name of this DeviceApp.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this DeviceApp.


        :param app_name: The app_name of this DeviceApp.
        :type: str
        """
        if app_name is None:
            raise ValueError("Invalid value for `app_name`, must not be `None`")
        if app_name is not None and len(app_name) < 1:
            raise ValueError("Invalid value for `app_name`, length must be greater than or equal to `1`")

        self._app_name = app_name

    @property
    def package_name(self):
        """Gets the package_name of this DeviceApp.


        :return: The package_name of this DeviceApp.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this DeviceApp.


        :param package_name: The package_name of this DeviceApp.
        :type: str
        """
        if package_name is None:
            raise ValueError("Invalid value for `package_name`, must not be `None`")
        if package_name is not None and len(package_name) > 255:
            raise ValueError("Invalid value for `package_name`, length must be less than or equal to `255`")
        if package_name is not None and len(package_name) < 1:
            raise ValueError("Invalid value for `package_name`, length must be greater than or equal to `1`")

        self._package_name = package_name

    @property
    def whitelisted(self):
        """Gets the whitelisted of this DeviceApp.


        :return: The whitelisted of this DeviceApp.
        :rtype: bool
        """
        return self._whitelisted

    @whitelisted.setter
    def whitelisted(self, whitelisted):
        """Sets the whitelisted of this DeviceApp.


        :param whitelisted: The whitelisted of this DeviceApp.
        :type: bool
        """

        self._whitelisted = whitelisted

    @property
    def product_id(self):
        """Gets the product_id of this DeviceApp.


        :return: The product_id of this DeviceApp.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this DeviceApp.


        :param product_id: The product_id of this DeviceApp.
        :type: str
        """
        if product_id is not None and len(product_id) > 255:
            raise ValueError("Invalid value for `product_id`, length must be less than or equal to `255`")
        if product_id is not None and len(product_id) < 1:
            raise ValueError("Invalid value for `product_id`, length must be greater than or equal to `1`")

        self._product_id = product_id

    @property
    def version_code(self):
        """Gets the version_code of this DeviceApp.


        :return: The version_code of this DeviceApp.
        :rtype: str
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        """Sets the version_code of this DeviceApp.


        :param version_code: The version_code of this DeviceApp.
        :type: str
        """
        if version_code is not None and len(version_code) > 128:
            raise ValueError("Invalid value for `version_code`, length must be less than or equal to `128`")
        if version_code is not None and len(version_code) < 1:
            raise ValueError("Invalid value for `version_code`, length must be greater than or equal to `1`")

        self._version_code = version_code

    @property
    def version_name(self):
        """Gets the version_name of this DeviceApp.


        :return: The version_name of this DeviceApp.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        """Sets the version_name of this DeviceApp.


        :param version_name: The version_name of this DeviceApp.
        :type: str
        """
        if version_name is not None and len(version_name) > 128:
            raise ValueError("Invalid value for `version_name`, length must be less than or equal to `128`")
        if version_name is not None and len(version_name) < 1:
            raise ValueError("Invalid value for `version_name`, length must be greater than or equal to `1`")

        self._version_name = version_name

    @property
    def created_on(self):
        """Gets the created_on of this DeviceApp.


        :return: The created_on of this DeviceApp.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeviceApp.


        :param created_on: The created_on of this DeviceApp.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this DeviceApp.


        :return: The updated_on of this DeviceApp.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this DeviceApp.


        :param updated_on: The updated_on of this DeviceApp.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this DeviceApp.


        :return: The is_active of this DeviceApp.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this DeviceApp.


        :param is_active: The is_active of this DeviceApp.
        :type: bool
        """

        self._is_active = is_active

    @property
    def device(self):
        """Gets the device of this DeviceApp.


        :return: The device of this DeviceApp.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this DeviceApp.


        :param device: The device of this DeviceApp.
        :type: str
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")

        self._device = device

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DeviceApp, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeviceApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
