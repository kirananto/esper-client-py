# coding: utf-8

"""
    Esper SDK

    This is a read only Esper SDK.  You can find out more about Esper at [https://shoonya.io](https://shoonya.io).  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: developer@shoonya.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class EmmDevice(object):
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
        'id': 'int',
        'google_device_id': 'str',
        'management_type': 'str',
        'device': 'str',
        'google_user': 'int',
        'policy': 'int',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'is_active': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'google_device_id': 'google_device_id',
        'management_type': 'managementType',
        'device': 'device',
        'google_user': 'google_user',
        'policy': 'policy',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'is_active': 'is_active'
    }

    def __init__(self, id=None, google_device_id=None, management_type=None, device=None, google_user=None, policy=None, created_on=None, updated_on=None, is_active=True):  # noqa: E501
        """EmmDevice - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._google_device_id = None
        self._management_type = None
        self._device = None
        self._google_user = None
        self._policy = None
        self._created_on = None
        self._updated_on = None
        self._is_active = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if google_device_id is not None:
            self.google_device_id = google_device_id
        if management_type is not None:
            self.management_type = management_type
        if device is not None:
            self.device = device
        if google_user is not None:
            self.google_user = google_user
        if policy is not None:
            self.policy = policy
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if is_active is not None:
            self.is_active = is_active

    @property
    def id(self):
        """Gets the id of this EmmDevice.  # noqa: E501


        :return: The id of this EmmDevice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EmmDevice.


        :param id: The id of this EmmDevice.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def google_device_id(self):
        """Gets the google_device_id of this EmmDevice.  # noqa: E501


        :return: The google_device_id of this EmmDevice.  # noqa: E501
        :rtype: str
        """
        return self._google_device_id

    @google_device_id.setter
    def google_device_id(self, google_device_id):
        """Sets the google_device_id of this EmmDevice.


        :param google_device_id: The google_device_id of this EmmDevice.  # noqa: E501
        :type: str
        """

        self._google_device_id = google_device_id

    @property
    def management_type(self):
        """Gets the management_type of this EmmDevice.  # noqa: E501


        :return: The management_type of this EmmDevice.  # noqa: E501
        :rtype: str
        """
        return self._management_type

    @management_type.setter
    def management_type(self, management_type):
        """Sets the management_type of this EmmDevice.


        :param management_type: The management_type of this EmmDevice.  # noqa: E501
        :type: str
        """

        self._management_type = management_type

    @property
    def device(self):
        """Gets the device of this EmmDevice.  # noqa: E501


        :return: The device of this EmmDevice.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this EmmDevice.


        :param device: The device of this EmmDevice.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def google_user(self):
        """Gets the google_user of this EmmDevice.  # noqa: E501


        :return: The google_user of this EmmDevice.  # noqa: E501
        :rtype: int
        """
        return self._google_user

    @google_user.setter
    def google_user(self, google_user):
        """Sets the google_user of this EmmDevice.


        :param google_user: The google_user of this EmmDevice.  # noqa: E501
        :type: int
        """

        self._google_user = google_user

    @property
    def policy(self):
        """Gets the policy of this EmmDevice.  # noqa: E501


        :return: The policy of this EmmDevice.  # noqa: E501
        :rtype: int
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this EmmDevice.


        :param policy: The policy of this EmmDevice.  # noqa: E501
        :type: int
        """

        self._policy = policy

    @property
    def created_on(self):
        """Gets the created_on of this EmmDevice.  # noqa: E501


        :return: The created_on of this EmmDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this EmmDevice.


        :param created_on: The created_on of this EmmDevice.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this EmmDevice.  # noqa: E501


        :return: The updated_on of this EmmDevice.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this EmmDevice.


        :param updated_on: The updated_on of this EmmDevice.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def is_active(self):
        """Gets the is_active of this EmmDevice.  # noqa: E501


        :return: The is_active of this EmmDevice.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this EmmDevice.


        :param is_active: The is_active of this EmmDevice.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(EmmDevice, dict):
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
        if not isinstance(other, EmmDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other