# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class VoltageMap(object):
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
        'experiment': 'str',
        'detector': 'str',
        'voltages': 'list[VoltageMapVoltages]',
        'created_by': 'str',
        'comments': 'str',
        '_date': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'experiment': 'experiment',
        'detector': 'detector',
        'voltages': 'voltages',
        'created_by': 'created_by',
        'comments': 'comments',
        '_date': 'date',
        'id': '_id'
    }

    def __init__(self, name=None, experiment=None, detector=None, voltages=None, created_by=None, comments=None, _date=None, id=None):  # noqa: E501
        """VoltageMap - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._experiment = None
        self._detector = None
        self._voltages = None
        self._created_by = None
        self._comments = None
        self.__date = None
        self._id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if experiment is not None:
            self.experiment = experiment
        if detector is not None:
            self.detector = detector
        if voltages is not None:
            self.voltages = voltages
        if created_by is not None:
            self.created_by = created_by
        if comments is not None:
            self.comments = comments
        if _date is not None:
            self._date = _date
        if id is not None:
            self.id = id

    @property
    def name(self):
        """Gets the name of this VoltageMap.  # noqa: E501


        :return: The name of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VoltageMap.


        :param name: The name of this VoltageMap.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def experiment(self):
        """Gets the experiment of this VoltageMap.  # noqa: E501


        :return: The experiment of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this VoltageMap.


        :param experiment: The experiment of this VoltageMap.  # noqa: E501
        :type: str
        """
        allowed_values = ["xenon1t", "xenonnt", "unknown"]  # noqa: E501
        if experiment not in allowed_values:
            raise ValueError(
                "Invalid value for `experiment` ({0}), must be one of {1}"  # noqa: E501
                .format(experiment, allowed_values)
            )

        self._experiment = experiment

    @property
    def detector(self):
        """Gets the detector of this VoltageMap.  # noqa: E501


        :return: The detector of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self._detector

    @detector.setter
    def detector(self, detector):
        """Sets the detector of this VoltageMap.


        :param detector: The detector of this VoltageMap.  # noqa: E501
        :type: str
        """
        allowed_values = ["tpc", "nveto", "muveto", "unknown"]  # noqa: E501
        if detector not in allowed_values:
            raise ValueError(
                "Invalid value for `detector` ({0}), must be one of {1}"  # noqa: E501
                .format(detector, allowed_values)
            )

        self._detector = detector

    @property
    def voltages(self):
        """Gets the voltages of this VoltageMap.  # noqa: E501


        :return: The voltages of this VoltageMap.  # noqa: E501
        :rtype: list[VoltageMapVoltages]
        """
        return self._voltages

    @voltages.setter
    def voltages(self, voltages):
        """Sets the voltages of this VoltageMap.


        :param voltages: The voltages of this VoltageMap.  # noqa: E501
        :type: list[VoltageMapVoltages]
        """

        self._voltages = voltages

    @property
    def created_by(self):
        """Gets the created_by of this VoltageMap.  # noqa: E501


        :return: The created_by of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this VoltageMap.


        :param created_by: The created_by of this VoltageMap.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def comments(self):
        """Gets the comments of this VoltageMap.  # noqa: E501


        :return: The comments of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this VoltageMap.


        :param comments: The comments of this VoltageMap.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def _date(self):
        """Gets the _date of this VoltageMap.  # noqa: E501


        :return: The _date of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this VoltageMap.


        :param _date: The _date of this VoltageMap.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def id(self):
        """Gets the id of this VoltageMap.  # noqa: E501


        :return: The id of this VoltageMap.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VoltageMap.


        :param id: The id of this VoltageMap.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if issubclass(VoltageMap, dict):
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
        if not isinstance(other, VoltageMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
