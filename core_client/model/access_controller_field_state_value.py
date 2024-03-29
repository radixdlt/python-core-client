"""
    Radix Core API - Babylon

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import re  # noqa: F401
import sys  # noqa: F401

from core_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from core_client.exceptions import ApiAttributeError


def lazy_import():
    from core_client.model.entity_reference import EntityReference
    from core_client.model.primary_role_recovery_attempt import PrimaryRoleRecoveryAttempt
    from core_client.model.recovery_role_recovery_attempt import RecoveryRoleRecoveryAttempt
    globals()['EntityReference'] = EntityReference
    globals()['PrimaryRoleRecoveryAttempt'] = PrimaryRoleRecoveryAttempt
    globals()['RecoveryRoleRecoveryAttempt'] = RecoveryRoleRecoveryAttempt


class AccessControllerFieldStateValue(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('timed_recovery_delay_minutes',): {
            'inclusive_maximum': 4294967295,
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'controlled_vault': (EntityReference,),  # noqa: E501
            'recovery_badge_resource_address': (str,),  # noqa: E501
            'is_primary_role_locked': (bool,),  # noqa: E501
            'has_primary_role_badge_withdraw_attempt': (bool,),  # noqa: E501
            'has_recovery_role_badge_withdraw_attempt': (bool,),  # noqa: E501
            'timed_recovery_delay_minutes': (int,),  # noqa: E501
            'primary_role_recovery_attempt': (PrimaryRoleRecoveryAttempt,),  # noqa: E501
            'recovery_role_recovery_attempt': (RecoveryRoleRecoveryAttempt,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'controlled_vault': 'controlled_vault',  # noqa: E501
        'recovery_badge_resource_address': 'recovery_badge_resource_address',  # noqa: E501
        'is_primary_role_locked': 'is_primary_role_locked',  # noqa: E501
        'has_primary_role_badge_withdraw_attempt': 'has_primary_role_badge_withdraw_attempt',  # noqa: E501
        'has_recovery_role_badge_withdraw_attempt': 'has_recovery_role_badge_withdraw_attempt',  # noqa: E501
        'timed_recovery_delay_minutes': 'timed_recovery_delay_minutes',  # noqa: E501
        'primary_role_recovery_attempt': 'primary_role_recovery_attempt',  # noqa: E501
        'recovery_role_recovery_attempt': 'recovery_role_recovery_attempt',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, controlled_vault, recovery_badge_resource_address, is_primary_role_locked, has_primary_role_badge_withdraw_attempt, has_recovery_role_badge_withdraw_attempt, *args, **kwargs):  # noqa: E501
        """AccessControllerFieldStateValue - a model defined in OpenAPI

        Args:
            controlled_vault (EntityReference):
            recovery_badge_resource_address (str): The Bech32m-encoded human readable version of the resource address
            is_primary_role_locked (bool): Whether the primary role is currently locked.
            has_primary_role_badge_withdraw_attempt (bool): Whether the primary role badge withdraw is currently being attempted.
            has_recovery_role_badge_withdraw_attempt (bool): Whether the recovery role badge withdraw is currently being attempted.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            timed_recovery_delay_minutes (int): An integer between `0` and `2^32 - 1`, specifying the amount of time (in minutes) that it takes for timed recovery to be done. When not present, then timed recovery can not be performed through this access controller. . [optional]  # noqa: E501
            primary_role_recovery_attempt (PrimaryRoleRecoveryAttempt): [optional]  # noqa: E501
            recovery_role_recovery_attempt (RecoveryRoleRecoveryAttempt): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.controlled_vault = controlled_vault
        self.recovery_badge_resource_address = recovery_badge_resource_address
        self.is_primary_role_locked = is_primary_role_locked
        self.has_primary_role_badge_withdraw_attempt = has_primary_role_badge_withdraw_attempt
        self.has_recovery_role_badge_withdraw_attempt = has_recovery_role_badge_withdraw_attempt
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, controlled_vault, recovery_badge_resource_address, is_primary_role_locked, has_primary_role_badge_withdraw_attempt, has_recovery_role_badge_withdraw_attempt, *args, **kwargs):  # noqa: E501
        """AccessControllerFieldStateValue - a model defined in OpenAPI

        Args:
            controlled_vault (EntityReference):
            recovery_badge_resource_address (str): The Bech32m-encoded human readable version of the resource address
            is_primary_role_locked (bool): Whether the primary role is currently locked.
            has_primary_role_badge_withdraw_attempt (bool): Whether the primary role badge withdraw is currently being attempted.
            has_recovery_role_badge_withdraw_attempt (bool): Whether the recovery role badge withdraw is currently being attempted.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            timed_recovery_delay_minutes (int): An integer between `0` and `2^32 - 1`, specifying the amount of time (in minutes) that it takes for timed recovery to be done. When not present, then timed recovery can not be performed through this access controller. . [optional]  # noqa: E501
            primary_role_recovery_attempt (PrimaryRoleRecoveryAttempt): [optional]  # noqa: E501
            recovery_role_recovery_attempt (RecoveryRoleRecoveryAttempt): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.controlled_vault = controlled_vault
        self.recovery_badge_resource_address = recovery_badge_resource_address
        self.is_primary_role_locked = is_primary_role_locked
        self.has_primary_role_badge_withdraw_attempt = has_primary_role_badge_withdraw_attempt
        self.has_recovery_role_badge_withdraw_attempt = has_recovery_role_badge_withdraw_attempt
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
