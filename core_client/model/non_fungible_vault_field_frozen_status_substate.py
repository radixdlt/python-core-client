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
    from core_client.model.access_controller_field_state_substate import AccessControllerFieldStateSubstate
    from core_client.model.account_authorized_depositor_entry_substate import AccountAuthorizedDepositorEntrySubstate
    from core_client.model.account_field_state_substate import AccountFieldStateSubstate
    from core_client.model.account_resource_preference_entry_substate import AccountResourcePreferenceEntrySubstate
    from core_client.model.account_vault_entry_substate import AccountVaultEntrySubstate
    from core_client.model.consensus_manager_field_config_substate import ConsensusManagerFieldConfigSubstate
    from core_client.model.consensus_manager_field_current_proposal_statistic_substate import ConsensusManagerFieldCurrentProposalStatisticSubstate
    from core_client.model.consensus_manager_field_current_time_rounded_to_minutes_substate import ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate
    from core_client.model.consensus_manager_field_current_time_substate import ConsensusManagerFieldCurrentTimeSubstate
    from core_client.model.consensus_manager_field_current_validator_set_substate import ConsensusManagerFieldCurrentValidatorSetSubstate
    from core_client.model.consensus_manager_field_state_substate import ConsensusManagerFieldStateSubstate
    from core_client.model.consensus_manager_field_validator_rewards_substate import ConsensusManagerFieldValidatorRewardsSubstate
    from core_client.model.consensus_manager_registered_validators_by_stake_index_entry_substate import ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstate
    from core_client.model.fungible_resource_manager_field_divisibility_substate import FungibleResourceManagerFieldDivisibilitySubstate
    from core_client.model.fungible_resource_manager_field_total_supply_substate import FungibleResourceManagerFieldTotalSupplySubstate
    from core_client.model.fungible_vault_field_balance_substate import FungibleVaultFieldBalanceSubstate
    from core_client.model.fungible_vault_field_frozen_status_substate import FungibleVaultFieldFrozenStatusSubstate
    from core_client.model.generic_key_value_store_entry_substate import GenericKeyValueStoreEntrySubstate
    from core_client.model.generic_scrypto_component_field_state_substate import GenericScryptoComponentFieldStateSubstate
    from core_client.model.metadata_module_entry_substate import MetadataModuleEntrySubstate
    from core_client.model.multi_resource_pool_field_state_substate import MultiResourcePoolFieldStateSubstate
    from core_client.model.non_fungible_resource_manager_data_entry_substate import NonFungibleResourceManagerDataEntrySubstate
    from core_client.model.non_fungible_resource_manager_field_id_type_substate import NonFungibleResourceManagerFieldIdTypeSubstate
    from core_client.model.non_fungible_resource_manager_field_mutable_fields_substate import NonFungibleResourceManagerFieldMutableFieldsSubstate
    from core_client.model.non_fungible_resource_manager_field_total_supply_substate import NonFungibleResourceManagerFieldTotalSupplySubstate
    from core_client.model.non_fungible_vault_contents_index_entry_substate import NonFungibleVaultContentsIndexEntrySubstate
    from core_client.model.non_fungible_vault_field_balance_substate import NonFungibleVaultFieldBalanceSubstate
    from core_client.model.non_fungible_vault_field_frozen_status_substate import NonFungibleVaultFieldFrozenStatusSubstate
    from core_client.model.non_fungible_vault_field_frozen_status_substate_all_of import NonFungibleVaultFieldFrozenStatusSubstateAllOf
    from core_client.model.non_fungible_vault_field_frozen_status_value import NonFungibleVaultFieldFrozenStatusValue
    from core_client.model.one_resource_pool_field_state_substate import OneResourcePoolFieldStateSubstate
    from core_client.model.package_blueprint_auth_template_entry_substate import PackageBlueprintAuthTemplateEntrySubstate
    from core_client.model.package_blueprint_definition_entry_substate import PackageBlueprintDefinitionEntrySubstate
    from core_client.model.package_blueprint_dependencies_entry_substate import PackageBlueprintDependenciesEntrySubstate
    from core_client.model.package_blueprint_royalty_entry_substate import PackageBlueprintRoyaltyEntrySubstate
    from core_client.model.package_code_instrumented_code_entry_substate import PackageCodeInstrumentedCodeEntrySubstate
    from core_client.model.package_code_original_code_entry_substate import PackageCodeOriginalCodeEntrySubstate
    from core_client.model.package_code_vm_type_entry_substate import PackageCodeVmTypeEntrySubstate
    from core_client.model.package_field_royalty_accumulator_substate import PackageFieldRoyaltyAccumulatorSubstate
    from core_client.model.role_assignment_module_field_owner_role_substate import RoleAssignmentModuleFieldOwnerRoleSubstate
    from core_client.model.role_assignment_module_rule_entry_substate import RoleAssignmentModuleRuleEntrySubstate
    from core_client.model.royalty_module_field_state_substate import RoyaltyModuleFieldStateSubstate
    from core_client.model.royalty_module_method_royalty_entry_substate import RoyaltyModuleMethodRoyaltyEntrySubstate
    from core_client.model.schema_entry_substate import SchemaEntrySubstate
    from core_client.model.substate import Substate
    from core_client.model.substate_type import SubstateType
    from core_client.model.transaction_tracker_collection_entry_substate import TransactionTrackerCollectionEntrySubstate
    from core_client.model.transaction_tracker_field_state_substate import TransactionTrackerFieldStateSubstate
    from core_client.model.two_resource_pool_field_state_substate import TwoResourcePoolFieldStateSubstate
    from core_client.model.type_info_module_field_type_info_substate import TypeInfoModuleFieldTypeInfoSubstate
    from core_client.model.validator_field_protocol_update_readiness_signal_substate import ValidatorFieldProtocolUpdateReadinessSignalSubstate
    from core_client.model.validator_field_state_substate import ValidatorFieldStateSubstate
    globals()['AccessControllerFieldStateSubstate'] = AccessControllerFieldStateSubstate
    globals()['AccountAuthorizedDepositorEntrySubstate'] = AccountAuthorizedDepositorEntrySubstate
    globals()['AccountFieldStateSubstate'] = AccountFieldStateSubstate
    globals()['AccountResourcePreferenceEntrySubstate'] = AccountResourcePreferenceEntrySubstate
    globals()['AccountVaultEntrySubstate'] = AccountVaultEntrySubstate
    globals()['ConsensusManagerFieldConfigSubstate'] = ConsensusManagerFieldConfigSubstate
    globals()['ConsensusManagerFieldCurrentProposalStatisticSubstate'] = ConsensusManagerFieldCurrentProposalStatisticSubstate
    globals()['ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate'] = ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate
    globals()['ConsensusManagerFieldCurrentTimeSubstate'] = ConsensusManagerFieldCurrentTimeSubstate
    globals()['ConsensusManagerFieldCurrentValidatorSetSubstate'] = ConsensusManagerFieldCurrentValidatorSetSubstate
    globals()['ConsensusManagerFieldStateSubstate'] = ConsensusManagerFieldStateSubstate
    globals()['ConsensusManagerFieldValidatorRewardsSubstate'] = ConsensusManagerFieldValidatorRewardsSubstate
    globals()['ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstate'] = ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstate
    globals()['FungibleResourceManagerFieldDivisibilitySubstate'] = FungibleResourceManagerFieldDivisibilitySubstate
    globals()['FungibleResourceManagerFieldTotalSupplySubstate'] = FungibleResourceManagerFieldTotalSupplySubstate
    globals()['FungibleVaultFieldBalanceSubstate'] = FungibleVaultFieldBalanceSubstate
    globals()['FungibleVaultFieldFrozenStatusSubstate'] = FungibleVaultFieldFrozenStatusSubstate
    globals()['GenericKeyValueStoreEntrySubstate'] = GenericKeyValueStoreEntrySubstate
    globals()['GenericScryptoComponentFieldStateSubstate'] = GenericScryptoComponentFieldStateSubstate
    globals()['MetadataModuleEntrySubstate'] = MetadataModuleEntrySubstate
    globals()['MultiResourcePoolFieldStateSubstate'] = MultiResourcePoolFieldStateSubstate
    globals()['NonFungibleResourceManagerDataEntrySubstate'] = NonFungibleResourceManagerDataEntrySubstate
    globals()['NonFungibleResourceManagerFieldIdTypeSubstate'] = NonFungibleResourceManagerFieldIdTypeSubstate
    globals()['NonFungibleResourceManagerFieldMutableFieldsSubstate'] = NonFungibleResourceManagerFieldMutableFieldsSubstate
    globals()['NonFungibleResourceManagerFieldTotalSupplySubstate'] = NonFungibleResourceManagerFieldTotalSupplySubstate
    globals()['NonFungibleVaultContentsIndexEntrySubstate'] = NonFungibleVaultContentsIndexEntrySubstate
    globals()['NonFungibleVaultFieldBalanceSubstate'] = NonFungibleVaultFieldBalanceSubstate
    globals()['NonFungibleVaultFieldFrozenStatusSubstate'] = NonFungibleVaultFieldFrozenStatusSubstate
    globals()['NonFungibleVaultFieldFrozenStatusSubstateAllOf'] = NonFungibleVaultFieldFrozenStatusSubstateAllOf
    globals()['NonFungibleVaultFieldFrozenStatusValue'] = NonFungibleVaultFieldFrozenStatusValue
    globals()['OneResourcePoolFieldStateSubstate'] = OneResourcePoolFieldStateSubstate
    globals()['PackageBlueprintAuthTemplateEntrySubstate'] = PackageBlueprintAuthTemplateEntrySubstate
    globals()['PackageBlueprintDefinitionEntrySubstate'] = PackageBlueprintDefinitionEntrySubstate
    globals()['PackageBlueprintDependenciesEntrySubstate'] = PackageBlueprintDependenciesEntrySubstate
    globals()['PackageBlueprintRoyaltyEntrySubstate'] = PackageBlueprintRoyaltyEntrySubstate
    globals()['PackageCodeInstrumentedCodeEntrySubstate'] = PackageCodeInstrumentedCodeEntrySubstate
    globals()['PackageCodeOriginalCodeEntrySubstate'] = PackageCodeOriginalCodeEntrySubstate
    globals()['PackageCodeVmTypeEntrySubstate'] = PackageCodeVmTypeEntrySubstate
    globals()['PackageFieldRoyaltyAccumulatorSubstate'] = PackageFieldRoyaltyAccumulatorSubstate
    globals()['RoleAssignmentModuleFieldOwnerRoleSubstate'] = RoleAssignmentModuleFieldOwnerRoleSubstate
    globals()['RoleAssignmentModuleRuleEntrySubstate'] = RoleAssignmentModuleRuleEntrySubstate
    globals()['RoyaltyModuleFieldStateSubstate'] = RoyaltyModuleFieldStateSubstate
    globals()['RoyaltyModuleMethodRoyaltyEntrySubstate'] = RoyaltyModuleMethodRoyaltyEntrySubstate
    globals()['SchemaEntrySubstate'] = SchemaEntrySubstate
    globals()['Substate'] = Substate
    globals()['SubstateType'] = SubstateType
    globals()['TransactionTrackerCollectionEntrySubstate'] = TransactionTrackerCollectionEntrySubstate
    globals()['TransactionTrackerFieldStateSubstate'] = TransactionTrackerFieldStateSubstate
    globals()['TwoResourcePoolFieldStateSubstate'] = TwoResourcePoolFieldStateSubstate
    globals()['TypeInfoModuleFieldTypeInfoSubstate'] = TypeInfoModuleFieldTypeInfoSubstate
    globals()['ValidatorFieldProtocolUpdateReadinessSignalSubstate'] = ValidatorFieldProtocolUpdateReadinessSignalSubstate
    globals()['ValidatorFieldStateSubstate'] = ValidatorFieldStateSubstate


class NonFungibleVaultFieldFrozenStatusSubstate(ModelNormal):
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
            'value': (NonFungibleVaultFieldFrozenStatusValue,),  # noqa: E501
            'substate_type': (SubstateType,),  # noqa: E501
            'is_locked': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        lazy_import()
        val = {
            'AccessControllerFieldState': AccessControllerFieldStateSubstate,
            'AccountAuthorizedDepositorEntry': AccountAuthorizedDepositorEntrySubstate,
            'AccountFieldState': AccountFieldStateSubstate,
            'AccountResourcePreferenceEntry': AccountResourcePreferenceEntrySubstate,
            'AccountVaultEntry': AccountVaultEntrySubstate,
            'ConsensusManagerFieldConfig': ConsensusManagerFieldConfigSubstate,
            'ConsensusManagerFieldCurrentProposalStatistic': ConsensusManagerFieldCurrentProposalStatisticSubstate,
            'ConsensusManagerFieldCurrentTime': ConsensusManagerFieldCurrentTimeSubstate,
            'ConsensusManagerFieldCurrentTimeRoundedToMinutes': ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate,
            'ConsensusManagerFieldCurrentValidatorSet': ConsensusManagerFieldCurrentValidatorSetSubstate,
            'ConsensusManagerFieldState': ConsensusManagerFieldStateSubstate,
            'ConsensusManagerFieldValidatorRewards': ConsensusManagerFieldValidatorRewardsSubstate,
            'ConsensusManagerRegisteredValidatorsByStakeIndexEntry': ConsensusManagerRegisteredValidatorsByStakeIndexEntrySubstate,
            'FungibleResourceManagerFieldDivisibility': FungibleResourceManagerFieldDivisibilitySubstate,
            'FungibleResourceManagerFieldTotalSupply': FungibleResourceManagerFieldTotalSupplySubstate,
            'FungibleVaultFieldBalance': FungibleVaultFieldBalanceSubstate,
            'FungibleVaultFieldFrozenStatus': FungibleVaultFieldFrozenStatusSubstate,
            'GenericKeyValueStoreEntry': GenericKeyValueStoreEntrySubstate,
            'GenericScryptoComponentFieldState': GenericScryptoComponentFieldStateSubstate,
            'MetadataModuleEntry': MetadataModuleEntrySubstate,
            'MultiResourcePoolFieldState': MultiResourcePoolFieldStateSubstate,
            'NonFungibleResourceManagerDataEntry': NonFungibleResourceManagerDataEntrySubstate,
            'NonFungibleResourceManagerFieldIdType': NonFungibleResourceManagerFieldIdTypeSubstate,
            'NonFungibleResourceManagerFieldMutableFields': NonFungibleResourceManagerFieldMutableFieldsSubstate,
            'NonFungibleResourceManagerFieldTotalSupply': NonFungibleResourceManagerFieldTotalSupplySubstate,
            'NonFungibleVaultContentsIndexEntry': NonFungibleVaultContentsIndexEntrySubstate,
            'NonFungibleVaultFieldBalance': NonFungibleVaultFieldBalanceSubstate,
            'NonFungibleVaultFieldFrozenStatus': NonFungibleVaultFieldFrozenStatusSubstate,
            'OneResourcePoolFieldState': OneResourcePoolFieldStateSubstate,
            'PackageBlueprintAuthTemplateEntry': PackageBlueprintAuthTemplateEntrySubstate,
            'PackageBlueprintDefinitionEntry': PackageBlueprintDefinitionEntrySubstate,
            'PackageBlueprintDependenciesEntry': PackageBlueprintDependenciesEntrySubstate,
            'PackageBlueprintRoyaltyEntry': PackageBlueprintRoyaltyEntrySubstate,
            'PackageCodeInstrumentedCodeEntry': PackageCodeInstrumentedCodeEntrySubstate,
            'PackageCodeOriginalCodeEntry': PackageCodeOriginalCodeEntrySubstate,
            'PackageCodeVmTypeEntry': PackageCodeVmTypeEntrySubstate,
            'PackageFieldRoyaltyAccumulator': PackageFieldRoyaltyAccumulatorSubstate,
            'RoleAssignmentModuleFieldOwnerRole': RoleAssignmentModuleFieldOwnerRoleSubstate,
            'RoleAssignmentModuleRuleEntry': RoleAssignmentModuleRuleEntrySubstate,
            'RoyaltyModuleFieldState': RoyaltyModuleFieldStateSubstate,
            'RoyaltyModuleMethodRoyaltyEntry': RoyaltyModuleMethodRoyaltyEntrySubstate,
            'SchemaEntry': SchemaEntrySubstate,
            'TransactionTrackerCollectionEntry': TransactionTrackerCollectionEntrySubstate,
            'TransactionTrackerFieldState': TransactionTrackerFieldStateSubstate,
            'TwoResourcePoolFieldState': TwoResourcePoolFieldStateSubstate,
            'TypeInfoModuleFieldTypeInfo': TypeInfoModuleFieldTypeInfoSubstate,
            'ValidatorFieldProtocolUpdateReadinessSignal': ValidatorFieldProtocolUpdateReadinessSignalSubstate,
            'ValidatorFieldState': ValidatorFieldStateSubstate,
        }
        if not val:
            return None
        return {'substate_type': val}

    attribute_map = {
        'value': 'value',  # noqa: E501
        'substate_type': 'substate_type',  # noqa: E501
        'is_locked': 'is_locked',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, value, substate_type, is_locked, *args, **kwargs):  # noqa: E501
        """NonFungibleVaultFieldFrozenStatusSubstate - a model defined in OpenAPI

        Args:
            value (NonFungibleVaultFieldFrozenStatusValue):
            substate_type (SubstateType):
            is_locked (bool):

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

        self.value = value
        self.substate_type = substate_type
        self.is_locked = is_locked
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
    def __init__(self, value, substate_type, is_locked, *args, **kwargs):  # noqa: E501
        """NonFungibleVaultFieldFrozenStatusSubstate - a model defined in OpenAPI

        Args:
            value (NonFungibleVaultFieldFrozenStatusValue):
            substate_type (SubstateType):
            is_locked (bool):

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

        self.value = value
        self.substate_type = substate_type
        self.is_locked = is_locked
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
