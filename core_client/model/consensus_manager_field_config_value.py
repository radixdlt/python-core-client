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
    from core_client.model.epoch_change_condition import EpochChangeCondition
    globals()['EpochChangeCondition'] = EpochChangeCondition


class ConsensusManagerFieldConfigValue(ModelNormal):
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
        ('max_validators',): {
            'inclusive_maximum': 10000000000,
            'inclusive_minimum': 0,
        },
        ('num_unstake_epochs',): {
            'inclusive_maximum': 10000000000,
            'inclusive_minimum': 0,
        },
        ('num_owner_stake_units_unlock_epochs',): {
            'inclusive_maximum': 10000000000,
            'inclusive_minimum': 0,
        },
        ('num_fee_increase_delay_epochs',): {
            'inclusive_maximum': 10000000000,
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
            'max_validators': (int,),  # noqa: E501
            'epoch_change_condition': (EpochChangeCondition,),  # noqa: E501
            'num_unstake_epochs': (int,),  # noqa: E501
            'total_emission_xrd_per_epoch': (str,),  # noqa: E501
            'min_validator_reliability': (str,),  # noqa: E501
            'num_owner_stake_units_unlock_epochs': (int,),  # noqa: E501
            'num_fee_increase_delay_epochs': (int,),  # noqa: E501
            'validator_creation_usd_equivalent_cost': (str,),  # noqa: E501
            'validator_creation_xrd_cost': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'max_validators': 'max_validators',  # noqa: E501
        'epoch_change_condition': 'epoch_change_condition',  # noqa: E501
        'num_unstake_epochs': 'num_unstake_epochs',  # noqa: E501
        'total_emission_xrd_per_epoch': 'total_emission_xrd_per_epoch',  # noqa: E501
        'min_validator_reliability': 'min_validator_reliability',  # noqa: E501
        'num_owner_stake_units_unlock_epochs': 'num_owner_stake_units_unlock_epochs',  # noqa: E501
        'num_fee_increase_delay_epochs': 'num_fee_increase_delay_epochs',  # noqa: E501
        'validator_creation_usd_equivalent_cost': 'validator_creation_usd_equivalent_cost',  # noqa: E501
        'validator_creation_xrd_cost': 'validator_creation_xrd_cost',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, max_validators, epoch_change_condition, num_unstake_epochs, total_emission_xrd_per_epoch, min_validator_reliability, num_owner_stake_units_unlock_epochs, num_fee_increase_delay_epochs, validator_creation_usd_equivalent_cost, validator_creation_xrd_cost, *args, **kwargs):  # noqa: E501
        """ConsensusManagerFieldConfigValue - a model defined in OpenAPI

        Args:
            max_validators (int): An integer between `0` and `10^10`, specifying the maximum number of validators in the active validator set. 
            epoch_change_condition (EpochChangeCondition):
            num_unstake_epochs (int): An integer between `0` and `10^10`, specifying the minimum number of epochs before an unstaker can withdraw their XRD. 
            total_emission_xrd_per_epoch (str): A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 
            min_validator_reliability (str): A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 
            num_owner_stake_units_unlock_epochs (int): An integer between `0` and `10^10`, specifying the minimum number of epochs before an owner can take their stake units after attempting to withdraw them. 
            num_fee_increase_delay_epochs (int): An integer between `0` and `10^10`, specifying the minimum number of epochs before a fee increase takes effect. 
            validator_creation_usd_equivalent_cost (str): The defining decimal cost of a validator in USD. This is turned into an XRD cost through the current protocol-based USD/XRD multiplier. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 
            validator_creation_xrd_cost (str): The decimal amount of XRD required to be passed in a bucket to create a validator. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 

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

        self.max_validators = max_validators
        self.epoch_change_condition = epoch_change_condition
        self.num_unstake_epochs = num_unstake_epochs
        self.total_emission_xrd_per_epoch = total_emission_xrd_per_epoch
        self.min_validator_reliability = min_validator_reliability
        self.num_owner_stake_units_unlock_epochs = num_owner_stake_units_unlock_epochs
        self.num_fee_increase_delay_epochs = num_fee_increase_delay_epochs
        self.validator_creation_usd_equivalent_cost = validator_creation_usd_equivalent_cost
        self.validator_creation_xrd_cost = validator_creation_xrd_cost
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
    def __init__(self, max_validators, epoch_change_condition, num_unstake_epochs, total_emission_xrd_per_epoch, min_validator_reliability, num_owner_stake_units_unlock_epochs, num_fee_increase_delay_epochs, validator_creation_usd_equivalent_cost, validator_creation_xrd_cost, *args, **kwargs):  # noqa: E501
        """ConsensusManagerFieldConfigValue - a model defined in OpenAPI

        Args:
            max_validators (int): An integer between `0` and `10^10`, specifying the maximum number of validators in the active validator set. 
            epoch_change_condition (EpochChangeCondition):
            num_unstake_epochs (int): An integer between `0` and `10^10`, specifying the minimum number of epochs before an unstaker can withdraw their XRD. 
            total_emission_xrd_per_epoch (str): A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 
            min_validator_reliability (str): A string-encoded fixed-precision decimal to 18 decimal places. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 
            num_owner_stake_units_unlock_epochs (int): An integer between `0` and `10^10`, specifying the minimum number of epochs before an owner can take their stake units after attempting to withdraw them. 
            num_fee_increase_delay_epochs (int): An integer between `0` and `10^10`, specifying the minimum number of epochs before a fee increase takes effect. 
            validator_creation_usd_equivalent_cost (str): The defining decimal cost of a validator in USD. This is turned into an XRD cost through the current protocol-based USD/XRD multiplier. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 
            validator_creation_xrd_cost (str): The decimal amount of XRD required to be passed in a bucket to create a validator. A decimal is formed of some signed integer `m` of attos (`10^(-18)`) units, where `-2^(192 - 1) <= m < 2^(192 - 1)`. 

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

        self.max_validators = max_validators
        self.epoch_change_condition = epoch_change_condition
        self.num_unstake_epochs = num_unstake_epochs
        self.total_emission_xrd_per_epoch = total_emission_xrd_per_epoch
        self.min_validator_reliability = min_validator_reliability
        self.num_owner_stake_units_unlock_epochs = num_owner_stake_units_unlock_epochs
        self.num_fee_increase_delay_epochs = num_fee_increase_delay_epochs
        self.validator_creation_usd_equivalent_cost = validator_creation_usd_equivalent_cost
        self.validator_creation_xrd_cost = validator_creation_xrd_cost
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
