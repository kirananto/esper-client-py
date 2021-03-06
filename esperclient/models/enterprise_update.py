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

from esperclient.models.enterprise_detail import EnterpriseDetail


class EnterpriseUpdate(object):
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
        'name': 'str',
        'display_name': 'str',
        'short_code': 'str',
        'details': 'EnterpriseDetail'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'short_code': 'short_code',
        'details': 'details'
    }

    def __init__(self, name=None, display_name=None, short_code=None, details=None):
        """EnterpriseUpdate - a model defined in Swagger"""

        self._name = None
        self._display_name = None
        self._short_code = None
        self._details = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if short_code is not None:
            self.short_code = short_code
        if details is not None:
            self.details = details

    @property
    def name(self):
        """Gets the name of this EnterpriseUpdate.


        :return: The name of this EnterpriseUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnterpriseUpdate.


        :param name: The name of this EnterpriseUpdate.
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this EnterpriseUpdate.


        :return: The display_name of this EnterpriseUpdate.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this EnterpriseUpdate.


        :param display_name: The display_name of this EnterpriseUpdate.
        :type: str
        """
        if display_name is not None and len(display_name) > 50:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `50`")
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")

        self._display_name = display_name

    @property
    def short_code(self):
        """Gets the short_code of this EnterpriseUpdate.


        :return: The short_code of this EnterpriseUpdate.
        :rtype: str
        """
        return self._short_code

    @short_code.setter
    def short_code(self, short_code):
        """Sets the short_code of this EnterpriseUpdate.


        :param short_code: The short_code of this EnterpriseUpdate.
        :type: str
        """
        if short_code is not None and len(short_code) > 10:
            raise ValueError("Invalid value for `short_code`, length must be less than or equal to `10`")
        if short_code is not None and len(short_code) < 1:
            raise ValueError("Invalid value for `short_code`, length must be greater than or equal to `1`")

        self._short_code = short_code

    @property
    def details(self):
        """Gets the details of this EnterpriseUpdate.


        :return: The details of this EnterpriseUpdate.
        :rtype: EnterpriseDetail
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this EnterpriseUpdate.


        :param details: The details of this EnterpriseUpdate.
        :type: EnterpriseDetail
        """

        self._details = details

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
        if issubclass(EnterpriseUpdate, dict):
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
        if not isinstance(other, EnterpriseUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
