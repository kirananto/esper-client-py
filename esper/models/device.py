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
from esper.models.emm_device import EmmDevice  # noqa: F401,E501


class Device(object):
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
        'device_name': 'str',
        'policy_name': 'str',
        'status': 'int',
        'state': 'int',
        'current_command': 'str',
        'suid': 'str',
        'fcm_id': 'str',
        'enterprise': 'str',
        'policy': 'str',
        'user': 'str',
        'groups': 'list[str]',
        'api_level': 'int',
        'template_name': 'str',
        'mqtt_id': 'str',
        'software_info': 'object',
        'hardware_info': 'object',
        'displays': 'object',
        'network_info': 'object',
        'memory_info': 'object',
        'audio_constraints': 'object',
        'provisioned_on': 'datetime',
        'created_on': 'datetime',
        'updated_on': 'datetime',
        'emm_device': 'EmmDevice',
        'is_gms': 'bool',
        'is_active': 'bool'
    }

    attribute_map = {
        'url': 'url',
        'device_name': 'device_name',
        'policy_name': 'policy_name',
        'status': 'status',
        'state': 'state',
        'current_command': 'current_command',
        'suid': 'suid',
        'fcm_id': 'fcm_id',
        'enterprise': 'enterprise',
        'policy': 'policy',
        'user': 'user',
        'groups': 'groups',
        'api_level': 'api_level',
        'template_name': 'template_name',
        'mqtt_id': 'mqtt_id',
        'software_info': 'softwareInfo',
        'hardware_info': 'hardwareInfo',
        'displays': 'displays',
        'network_info': 'networkInfo',
        'memory_info': 'memoryInfo',
        'audio_constraints': 'audioConstraints',
        'provisioned_on': 'provisioned_on',
        'created_on': 'created_on',
        'updated_on': 'updated_on',
        'emm_device': 'emm_device',
        'is_gms': 'is_gms',
        'is_active': 'is_active'
    }

    def __init__(self, url=None, device_name=None, policy_name=None, status=None, state=None, current_command=None, suid=None, fcm_id=None, enterprise=None, policy=None, user=None, groups=None, api_level=None, template_name=None, mqtt_id=None, software_info=None, hardware_info=None, displays=None, network_info=None, memory_info=None, audio_constraints=None, provisioned_on=None, created_on=None, updated_on=None, emm_device=None, is_gms=True, is_active=True):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._device_name = None
        self._policy_name = None
        self._status = None
        self._state = None
        self._current_command = None
        self._suid = None
        self._fcm_id = None
        self._enterprise = None
        self._policy = None
        self._user = None
        self._groups = None
        self._api_level = None
        self._template_name = None
        self._mqtt_id = None
        self._software_info = None
        self._hardware_info = None
        self._displays = None
        self._network_info = None
        self._memory_info = None
        self._audio_constraints = None
        self._provisioned_on = None
        self._created_on = None
        self._updated_on = None
        self._emm_device = None
        self._is_gms = None
        self._is_active = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if device_name is not None:
            self.device_name = device_name
        if policy_name is not None:
            self.policy_name = policy_name
        if status is not None:
            self.status = status
        if state is not None:
            self.state = state
        if current_command is not None:
            self.current_command = current_command
        if suid is not None:
            self.suid = suid
        if fcm_id is not None:
            self.fcm_id = fcm_id
        if enterprise is not None:
            self.enterprise = enterprise
        if policy is not None:
            self.policy = policy
        if user is not None:
            self.user = user
        if groups is not None:
            self.groups = groups
        if api_level is not None:
            self.api_level = api_level
        if template_name is not None:
            self.template_name = template_name
        if mqtt_id is not None:
            self.mqtt_id = mqtt_id
        if software_info is not None:
            self.software_info = software_info
        if hardware_info is not None:
            self.hardware_info = hardware_info
        if displays is not None:
            self.displays = displays
        if network_info is not None:
            self.network_info = network_info
        if memory_info is not None:
            self.memory_info = memory_info
        if audio_constraints is not None:
            self.audio_constraints = audio_constraints
        if provisioned_on is not None:
            self.provisioned_on = provisioned_on
        if created_on is not None:
            self.created_on = created_on
        if updated_on is not None:
            self.updated_on = updated_on
        if emm_device is not None:
            self.emm_device = emm_device
        if is_gms is not None:
            self.is_gms = is_gms
        if is_active is not None:
            self.is_active = is_active

    @property
    def url(self):
        """Gets the url of this Device.  # noqa: E501


        :return: The url of this Device.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Device.


        :param url: The url of this Device.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def device_name(self):
        """Gets the device_name of this Device.  # noqa: E501


        :return: The device_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this Device.


        :param device_name: The device_name of this Device.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def policy_name(self):
        """Gets the policy_name of this Device.  # noqa: E501


        :return: The policy_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this Device.


        :param policy_name: The policy_name of this Device.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def status(self):
        """Gets the status of this Device.  # noqa: E501

        Current status of device  # noqa: E501

        :return: The status of this Device.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Device.

        Current status of device  # noqa: E501

        :param status: The status of this Device.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def state(self):
        """Gets the state of this Device.  # noqa: E501

        Current state of device  # noqa: E501

        :return: The state of this Device.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Device.

        Current state of device  # noqa: E501

        :param state: The state of this Device.  # noqa: E501
        :type: int
        """

        self._state = state

    @property
    def current_command(self):
        """Gets the current_command of this Device.  # noqa: E501

        Current command associated with device  # noqa: E501

        :return: The current_command of this Device.  # noqa: E501
        :rtype: str
        """
        return self._current_command

    @current_command.setter
    def current_command(self, current_command):
        """Sets the current_command of this Device.

        Current command associated with device  # noqa: E501

        :param current_command: The current_command of this Device.  # noqa: E501
        :type: str
        """

        self._current_command = current_command

    @property
    def suid(self):
        """Gets the suid of this Device.  # noqa: E501

        Device generated unique id  # noqa: E501

        :return: The suid of this Device.  # noqa: E501
        :rtype: str
        """
        return self._suid

    @suid.setter
    def suid(self, suid):
        """Sets the suid of this Device.

        Device generated unique id  # noqa: E501

        :param suid: The suid of this Device.  # noqa: E501
        :type: str
        """

        self._suid = suid

    @property
    def fcm_id(self):
        """Gets the fcm_id of this Device.  # noqa: E501


        :return: The fcm_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._fcm_id

    @fcm_id.setter
    def fcm_id(self, fcm_id):
        """Sets the fcm_id of this Device.


        :param fcm_id: The fcm_id of this Device.  # noqa: E501
        :type: str
        """

        self._fcm_id = fcm_id

    @property
    def enterprise(self):
        """Gets the enterprise of this Device.  # noqa: E501


        :return: The enterprise of this Device.  # noqa: E501
        :rtype: str
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this Device.


        :param enterprise: The enterprise of this Device.  # noqa: E501
        :type: str
        """

        self._enterprise = enterprise

    @property
    def policy(self):
        """Gets the policy of this Device.  # noqa: E501


        :return: The policy of this Device.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this Device.


        :param policy: The policy of this Device.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def user(self):
        """Gets the user of this Device.  # noqa: E501


        :return: The user of this Device.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Device.


        :param user: The user of this Device.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def groups(self):
        """Gets the groups of this Device.  # noqa: E501


        :return: The groups of this Device.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Device.


        :param groups: The groups of this Device.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def api_level(self):
        """Gets the api_level of this Device.  # noqa: E501


        :return: The api_level of this Device.  # noqa: E501
        :rtype: int
        """
        return self._api_level

    @api_level.setter
    def api_level(self, api_level):
        """Sets the api_level of this Device.


        :param api_level: The api_level of this Device.  # noqa: E501
        :type: int
        """

        self._api_level = api_level

    @property
    def template_name(self):
        """Gets the template_name of this Device.  # noqa: E501


        :return: The template_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Device.


        :param template_name: The template_name of this Device.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def mqtt_id(self):
        """Gets the mqtt_id of this Device.  # noqa: E501


        :return: The mqtt_id of this Device.  # noqa: E501
        :rtype: str
        """
        return self._mqtt_id

    @mqtt_id.setter
    def mqtt_id(self, mqtt_id):
        """Sets the mqtt_id of this Device.


        :param mqtt_id: The mqtt_id of this Device.  # noqa: E501
        :type: str
        """

        self._mqtt_id = mqtt_id

    @property
    def software_info(self):
        """Gets the software_info of this Device.  # noqa: E501


        :return: The software_info of this Device.  # noqa: E501
        :rtype: object
        """
        return self._software_info

    @software_info.setter
    def software_info(self, software_info):
        """Sets the software_info of this Device.


        :param software_info: The software_info of this Device.  # noqa: E501
        :type: object
        """

        self._software_info = software_info

    @property
    def hardware_info(self):
        """Gets the hardware_info of this Device.  # noqa: E501


        :return: The hardware_info of this Device.  # noqa: E501
        :rtype: object
        """
        return self._hardware_info

    @hardware_info.setter
    def hardware_info(self, hardware_info):
        """Sets the hardware_info of this Device.


        :param hardware_info: The hardware_info of this Device.  # noqa: E501
        :type: object
        """

        self._hardware_info = hardware_info

    @property
    def displays(self):
        """Gets the displays of this Device.  # noqa: E501


        :return: The displays of this Device.  # noqa: E501
        :rtype: object
        """
        return self._displays

    @displays.setter
    def displays(self, displays):
        """Sets the displays of this Device.


        :param displays: The displays of this Device.  # noqa: E501
        :type: object
        """

        self._displays = displays

    @property
    def network_info(self):
        """Gets the network_info of this Device.  # noqa: E501


        :return: The network_info of this Device.  # noqa: E501
        :rtype: object
        """
        return self._network_info

    @network_info.setter
    def network_info(self, network_info):
        """Sets the network_info of this Device.


        :param network_info: The network_info of this Device.  # noqa: E501
        :type: object
        """

        self._network_info = network_info

    @property
    def memory_info(self):
        """Gets the memory_info of this Device.  # noqa: E501


        :return: The memory_info of this Device.  # noqa: E501
        :rtype: object
        """
        return self._memory_info

    @memory_info.setter
    def memory_info(self, memory_info):
        """Sets the memory_info of this Device.


        :param memory_info: The memory_info of this Device.  # noqa: E501
        :type: object
        """

        self._memory_info = memory_info

    @property
    def audio_constraints(self):
        """Gets the audio_constraints of this Device.  # noqa: E501


        :return: The audio_constraints of this Device.  # noqa: E501
        :rtype: object
        """
        return self._audio_constraints

    @audio_constraints.setter
    def audio_constraints(self, audio_constraints):
        """Sets the audio_constraints of this Device.


        :param audio_constraints: The audio_constraints of this Device.  # noqa: E501
        :type: object
        """

        self._audio_constraints = audio_constraints

    @property
    def provisioned_on(self):
        """Gets the provisioned_on of this Device.  # noqa: E501


        :return: The provisioned_on of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._provisioned_on

    @provisioned_on.setter
    def provisioned_on(self, provisioned_on):
        """Sets the provisioned_on of this Device.


        :param provisioned_on: The provisioned_on of this Device.  # noqa: E501
        :type: datetime
        """

        self._provisioned_on = provisioned_on

    @property
    def created_on(self):
        """Gets the created_on of this Device.  # noqa: E501


        :return: The created_on of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Device.


        :param created_on: The created_on of this Device.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def updated_on(self):
        """Gets the updated_on of this Device.  # noqa: E501


        :return: The updated_on of this Device.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this Device.


        :param updated_on: The updated_on of this Device.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def emm_device(self):
        """Gets the emm_device of this Device.  # noqa: E501


        :return: The emm_device of this Device.  # noqa: E501
        :rtype: EmmDevice
        """
        return self._emm_device

    @emm_device.setter
    def emm_device(self, emm_device):
        """Sets the emm_device of this Device.


        :param emm_device: The emm_device of this Device.  # noqa: E501
        :type: EmmDevice
        """

        self._emm_device = emm_device

    @property
    def is_gms(self):
        """Gets the is_gms of this Device.  # noqa: E501


        :return: The is_gms of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._is_gms

    @is_gms.setter
    def is_gms(self, is_gms):
        """Sets the is_gms of this Device.


        :param is_gms: The is_gms of this Device.  # noqa: E501
        :type: bool
        """

        self._is_gms = is_gms

    @property
    def is_active(self):
        """Gets the is_active of this Device.  # noqa: E501


        :return: The is_active of this Device.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Device.


        :param is_active: The is_active of this Device.  # noqa: E501
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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other