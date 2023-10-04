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



class NetworkConfigurationResponseWellKnownAddresses(ModelNormal):
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
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'xrd': (str,),  # noqa: E501
            'secp256k1_signature_virtual_badge': (str,),  # noqa: E501
            'ed25519_signature_virtual_badge': (str,),  # noqa: E501
            'package_of_direct_caller_virtual_badge': (str,),  # noqa: E501
            'global_caller_virtual_badge': (str,),  # noqa: E501
            'system_transaction_badge': (str,),  # noqa: E501
            'package_owner_badge': (str,),  # noqa: E501
            'validator_owner_badge': (str,),  # noqa: E501
            'account_owner_badge': (str,),  # noqa: E501
            'identity_owner_badge': (str,),  # noqa: E501
            'package_package': (str,),  # noqa: E501
            'resource_package': (str,),  # noqa: E501
            'account_package': (str,),  # noqa: E501
            'identity_package': (str,),  # noqa: E501
            'consensus_manager_package': (str,),  # noqa: E501
            'access_controller_package': (str,),  # noqa: E501
            'transaction_processor_package': (str,),  # noqa: E501
            'metadata_module_package': (str,),  # noqa: E501
            'royalty_module_package': (str,),  # noqa: E501
            'role_assignment_module_package': (str,),  # noqa: E501
            'genesis_helper_package': (str,),  # noqa: E501
            'faucet_package': (str,),  # noqa: E501
            'pool_package': (str,),  # noqa: E501
            'consensus_manager': (str,),  # noqa: E501
            'genesis_helper': (str,),  # noqa: E501
            'faucet': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'xrd': 'xrd',  # noqa: E501
        'secp256k1_signature_virtual_badge': 'secp256k1_signature_virtual_badge',  # noqa: E501
        'ed25519_signature_virtual_badge': 'ed25519_signature_virtual_badge',  # noqa: E501
        'package_of_direct_caller_virtual_badge': 'package_of_direct_caller_virtual_badge',  # noqa: E501
        'global_caller_virtual_badge': 'global_caller_virtual_badge',  # noqa: E501
        'system_transaction_badge': 'system_transaction_badge',  # noqa: E501
        'package_owner_badge': 'package_owner_badge',  # noqa: E501
        'validator_owner_badge': 'validator_owner_badge',  # noqa: E501
        'account_owner_badge': 'account_owner_badge',  # noqa: E501
        'identity_owner_badge': 'identity_owner_badge',  # noqa: E501
        'package_package': 'package_package',  # noqa: E501
        'resource_package': 'resource_package',  # noqa: E501
        'account_package': 'account_package',  # noqa: E501
        'identity_package': 'identity_package',  # noqa: E501
        'consensus_manager_package': 'consensus_manager_package',  # noqa: E501
        'access_controller_package': 'access_controller_package',  # noqa: E501
        'transaction_processor_package': 'transaction_processor_package',  # noqa: E501
        'metadata_module_package': 'metadata_module_package',  # noqa: E501
        'royalty_module_package': 'royalty_module_package',  # noqa: E501
        'role_assignment_module_package': 'role_assignment_module_package',  # noqa: E501
        'genesis_helper_package': 'genesis_helper_package',  # noqa: E501
        'faucet_package': 'faucet_package',  # noqa: E501
        'pool_package': 'pool_package',  # noqa: E501
        'consensus_manager': 'consensus_manager',  # noqa: E501
        'genesis_helper': 'genesis_helper',  # noqa: E501
        'faucet': 'faucet',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, xrd, secp256k1_signature_virtual_badge, ed25519_signature_virtual_badge, package_of_direct_caller_virtual_badge, global_caller_virtual_badge, system_transaction_badge, package_owner_badge, validator_owner_badge, account_owner_badge, identity_owner_badge, package_package, resource_package, account_package, identity_package, consensus_manager_package, access_controller_package, transaction_processor_package, metadata_module_package, royalty_module_package, role_assignment_module_package, genesis_helper_package, faucet_package, pool_package, consensus_manager, genesis_helper, faucet, *args, **kwargs):  # noqa: E501
        """NetworkConfigurationResponseWellKnownAddresses - a model defined in OpenAPI

        Args:
            xrd (str):
            secp256k1_signature_virtual_badge (str):
            ed25519_signature_virtual_badge (str):
            package_of_direct_caller_virtual_badge (str):
            global_caller_virtual_badge (str):
            system_transaction_badge (str):
            package_owner_badge (str):
            validator_owner_badge (str):
            account_owner_badge (str):
            identity_owner_badge (str):
            package_package (str):
            resource_package (str):
            account_package (str):
            identity_package (str):
            consensus_manager_package (str):
            access_controller_package (str):
            transaction_processor_package (str):
            metadata_module_package (str):
            royalty_module_package (str):
            role_assignment_module_package (str):
            genesis_helper_package (str):
            faucet_package (str):
            pool_package (str):
            consensus_manager (str):
            genesis_helper (str):
            faucet (str):

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

        self.xrd = xrd
        self.secp256k1_signature_virtual_badge = secp256k1_signature_virtual_badge
        self.ed25519_signature_virtual_badge = ed25519_signature_virtual_badge
        self.package_of_direct_caller_virtual_badge = package_of_direct_caller_virtual_badge
        self.global_caller_virtual_badge = global_caller_virtual_badge
        self.system_transaction_badge = system_transaction_badge
        self.package_owner_badge = package_owner_badge
        self.validator_owner_badge = validator_owner_badge
        self.account_owner_badge = account_owner_badge
        self.identity_owner_badge = identity_owner_badge
        self.package_package = package_package
        self.resource_package = resource_package
        self.account_package = account_package
        self.identity_package = identity_package
        self.consensus_manager_package = consensus_manager_package
        self.access_controller_package = access_controller_package
        self.transaction_processor_package = transaction_processor_package
        self.metadata_module_package = metadata_module_package
        self.royalty_module_package = royalty_module_package
        self.role_assignment_module_package = role_assignment_module_package
        self.genesis_helper_package = genesis_helper_package
        self.faucet_package = faucet_package
        self.pool_package = pool_package
        self.consensus_manager = consensus_manager
        self.genesis_helper = genesis_helper
        self.faucet = faucet
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
    def __init__(self, xrd, secp256k1_signature_virtual_badge, ed25519_signature_virtual_badge, package_of_direct_caller_virtual_badge, global_caller_virtual_badge, system_transaction_badge, package_owner_badge, validator_owner_badge, account_owner_badge, identity_owner_badge, package_package, resource_package, account_package, identity_package, consensus_manager_package, access_controller_package, transaction_processor_package, metadata_module_package, royalty_module_package, role_assignment_module_package, genesis_helper_package, faucet_package, pool_package, consensus_manager, genesis_helper, faucet, *args, **kwargs):  # noqa: E501
        """NetworkConfigurationResponseWellKnownAddresses - a model defined in OpenAPI

        Args:
            xrd (str):
            secp256k1_signature_virtual_badge (str):
            ed25519_signature_virtual_badge (str):
            package_of_direct_caller_virtual_badge (str):
            global_caller_virtual_badge (str):
            system_transaction_badge (str):
            package_owner_badge (str):
            validator_owner_badge (str):
            account_owner_badge (str):
            identity_owner_badge (str):
            package_package (str):
            resource_package (str):
            account_package (str):
            identity_package (str):
            consensus_manager_package (str):
            access_controller_package (str):
            transaction_processor_package (str):
            metadata_module_package (str):
            royalty_module_package (str):
            role_assignment_module_package (str):
            genesis_helper_package (str):
            faucet_package (str):
            pool_package (str):
            consensus_manager (str):
            genesis_helper (str):
            faucet (str):

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

        self.xrd = xrd
        self.secp256k1_signature_virtual_badge = secp256k1_signature_virtual_badge
        self.ed25519_signature_virtual_badge = ed25519_signature_virtual_badge
        self.package_of_direct_caller_virtual_badge = package_of_direct_caller_virtual_badge
        self.global_caller_virtual_badge = global_caller_virtual_badge
        self.system_transaction_badge = system_transaction_badge
        self.package_owner_badge = package_owner_badge
        self.validator_owner_badge = validator_owner_badge
        self.account_owner_badge = account_owner_badge
        self.identity_owner_badge = identity_owner_badge
        self.package_package = package_package
        self.resource_package = resource_package
        self.account_package = account_package
        self.identity_package = identity_package
        self.consensus_manager_package = consensus_manager_package
        self.access_controller_package = access_controller_package
        self.transaction_processor_package = transaction_processor_package
        self.metadata_module_package = metadata_module_package
        self.royalty_module_package = royalty_module_package
        self.role_assignment_module_package = role_assignment_module_package
        self.genesis_helper_package = genesis_helper_package
        self.faucet_package = faucet_package
        self.pool_package = pool_package
        self.consensus_manager = consensus_manager
        self.genesis_helper = genesis_helper
        self.faucet = faucet
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