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


class EnterprisePolicy(object):
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
        'url': 'str',
        'device_count': 'int',
        'is_default': 'bool',
        'is_template': 'bool',
        'uuid': 'str',
        'name': 'str',
        'description': 'str',
        'google_policy_id': 'str',
        'policy': 'str',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool',
        'enterprise': 'str'
    }

    attribute_map = {
        'url': 'url',
        'device_count': 'device_count',
        'is_default': 'is_default',
        'is_template': 'is_template',
        'uuid': 'uuid',
        'name': 'name',
        'description': 'description',
        'google_policy_id': 'google_policy_id',
        'policy': 'policy',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active',
        'enterprise': 'enterprise'
    }

    def __init__(self, url=None, device_count=None, is_default=None, is_template=False, uuid=None, name=None, description=None, google_policy_id=None, policy=None, created_on=None, updated_on=None, is_active=None, enterprise=None):
        """EnterprisePolicy - a model defined in Swagger"""

        self._url = None
        self._device_count = None
        self._is_default = None
        self._is_template = None
        self._uuid = None
        self._name = None
        self._description = None
        self._google_policy_id = None
        self._policy = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self._enterprise = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if device_count is not None:
            self.device_count = device_count
        if is_default is not None:
            self.is_default = is_default
        if is_template is not None:
            self.is_template = is_template
        if uuid is not None:
            self.uuid = uuid
        self.name = name
        if description is not None:
            self.description = description
        if google_policy_id is not None:
            self.google_policy_id = google_policy_id
        self.policy = policy
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active
        self.enterprise = enterprise

    @property
    def url(self):
        """Gets the url of this EnterprisePolicy.


        :return: The url of this EnterprisePolicy.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EnterprisePolicy.


        :param url: The url of this EnterprisePolicy.
        :type: str
        """

        self._url = url

    @property
    def device_count(self):
        """Gets the device_count of this EnterprisePolicy.


        :return: The device_count of this EnterprisePolicy.
        :rtype: int
        """
        return self._device_count

    @device_count.setter
    def device_count(self, device_count):
        """Sets the device_count of this EnterprisePolicy.


        :param device_count: The device_count of this EnterprisePolicy.
        :type: int
        """

        self._device_count = device_count

    @property
    def is_default(self):
        """Gets the is_default of this EnterprisePolicy.


        :return: The is_default of this EnterprisePolicy.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this EnterprisePolicy.


        :param is_default: The is_default of this EnterprisePolicy.
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_template(self):
        """Gets the is_template of this EnterprisePolicy.


        :return: The is_template of this EnterprisePolicy.
        :rtype: bool
        """
        return self._is_template

    @is_template.setter
    def is_template(self, is_template):
        """Sets the is_template of this EnterprisePolicy.


        :param is_template: The is_template of this EnterprisePolicy.
        :type: bool
        """

        self._is_template = is_template

    @property
    def uuid(self):
        """Gets the uuid of this EnterprisePolicy.


        :return: The uuid of this EnterprisePolicy.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this EnterprisePolicy.


        :param uuid: The uuid of this EnterprisePolicy.
        :type: str
        """

        self._uuid = uuid

    @property
    def name(self):
        """Gets the name of this EnterprisePolicy.


        :return: The name of this EnterprisePolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnterprisePolicy.


        :param name: The name of this EnterprisePolicy.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def description(self):
        """Gets the description of this EnterprisePolicy.


        :return: The description of this EnterprisePolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EnterprisePolicy.


        :param description: The description of this EnterprisePolicy.
        :type: str
        """

        self._description = description

    @property
    def google_policy_id(self):
        """Gets the google_policy_id of this EnterprisePolicy.


        :return: The google_policy_id of this EnterprisePolicy.
        :rtype: str
        """
        return self._google_policy_id

    @google_policy_id.setter
    def google_policy_id(self, google_policy_id):
        """Sets the google_policy_id of this EnterprisePolicy.


        :param google_policy_id: The google_policy_id of this EnterprisePolicy.
        :type: str
        """
        if google_policy_id is not None and len(google_policy_id) > 255:
            raise ValueError("Invalid value for `google_policy_id`, length must be less than or equal to `255`")
        if google_policy_id is not None and len(google_policy_id) < 1:
            raise ValueError("Invalid value for `google_policy_id`, length must be greater than or equal to `1`")

        self._google_policy_id = google_policy_id

    @property
    def policy(self):
        """Gets the policy of this EnterprisePolicy.

        Policy JSON string

        :return: The policy of this EnterprisePolicy.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this EnterprisePolicy.

        Policy JSON string

        :param policy: The policy of this EnterprisePolicy.
        :type: str
        """
        if policy is None:
            raise ValueError("Invalid value for `policy`, must not be `None`")

        self._policy = policy

    @property
    def created_on(self):
        """Gets the created_on of this EnterprisePolicy.


        :return: The created_on of this EnterprisePolicy.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this EnterprisePolicy.


        :param created_on: The created_on of this EnterprisePolicy.
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this EnterprisePolicy.


        :return: The updated_on of this EnterprisePolicy.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this EnterprisePolicy.


        :param updated_on: The updated_on of this EnterprisePolicy.
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this EnterprisePolicy.


        :return: The is_active of this EnterprisePolicy.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this EnterprisePolicy.


        :param is_active: The is_active of this EnterprisePolicy.
        :type: bool
        """

        self._is_active = is_active

    @property
    def enterprise(self):
        """Gets the enterprise of this EnterprisePolicy.


        :return: The enterprise of this EnterprisePolicy.
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this EnterprisePolicy.


        :param enterprise: The enterprise of this EnterprisePolicy.
        :type: str
        """
        if enterprise is None:
            raise ValueError("Invalid value for `enterprise`, must not be `None`")

        self._enterprise = enterprise

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
        if issubclass(EnterprisePolicy, dict):
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
        if not isinstance(other, EnterprisePolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
