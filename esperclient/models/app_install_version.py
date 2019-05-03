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


class AppInstallVersion(object):
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
        'app_version_id': 'str',
        'version_code': 'str',
        'build_number': 'str',
        'hash_string': 'str'
    }

    attribute_map = {
        'app_version_id': 'app_version_id',
        'version_code': 'version_code',
        'build_number': 'build_number',
        'hash_string': 'hash_string'
    }

    def __init__(self, app_version_id=None, version_code=None, build_number=None, hash_string=None):
        """AppInstallVersion - a model defined in Swagger"""

        self._app_version_id = None
        self._version_code = None
        self._build_number = None
        self._hash_string = None
        self.discriminator = None

        if app_version_id is not None:
            self.app_version_id = app_version_id
        if version_code is not None:
            self.version_code = version_code
        if build_number is not None:
            self.build_number = build_number
        if hash_string is not None:
            self.hash_string = hash_string

    @property
    def app_version_id(self):
        """Gets the app_version_id of this AppInstallVersion.


        :return: The app_version_id of this AppInstallVersion.
        :rtype: str
        """
        return self._app_version_id

    @app_version_id.setter
    def app_version_id(self, app_version_id):
        """Sets the app_version_id of this AppInstallVersion.


        :param app_version_id: The app_version_id of this AppInstallVersion.
        :type: str
        """

        self._app_version_id = app_version_id

    @property
    def version_code(self):
        """Gets the version_code of this AppInstallVersion.


        :return: The version_code of this AppInstallVersion.
        :rtype: str
        """
        return self._version_code

    @version_code.setter
    def version_code(self, version_code):
        """Sets the version_code of this AppInstallVersion.


        :param version_code: The version_code of this AppInstallVersion.
        :type: str
        """

        self._version_code = version_code

    @property
    def build_number(self):
        """Gets the build_number of this AppInstallVersion.


        :return: The build_number of this AppInstallVersion.
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """Sets the build_number of this AppInstallVersion.


        :param build_number: The build_number of this AppInstallVersion.
        :type: str
        """

        self._build_number = build_number

    @property
    def hash_string(self):
        """Gets the hash_string of this AppInstallVersion.


        :return: The hash_string of this AppInstallVersion.
        :rtype: str
        """
        return self._hash_string

    @hash_string.setter
    def hash_string(self, hash_string):
        """Sets the hash_string of this AppInstallVersion.


        :param hash_string: The hash_string of this AppInstallVersion.
        :type: str
        """

        self._hash_string = hash_string

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
        if issubclass(AppInstallVersion, dict):
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
        if not isinstance(other, AppInstallVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
