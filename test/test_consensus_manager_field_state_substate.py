"""
    Babylon Core API - RCnet V2

    Generated by https://openapi-generator.tech with customisation from https://github.com/radixdlt/python-core-client/
"""


import sys
import unittest

import core_client
from core_client.model.access_controller_field_state_substate import AccessControllerFieldStateSubstate
from core_client.model.access_rules_module_field_owner_role_substate import AccessRulesModuleFieldOwnerRoleSubstate
from core_client.model.access_rules_module_rule_entry_substate import AccessRulesModuleRuleEntrySubstate
from core_client.model.account_deposit_rule_index_entry_substate import AccountDepositRuleIndexEntrySubstate
from core_client.model.account_field_state_substate import AccountFieldStateSubstate
from core_client.model.account_vault_index_entry_substate import AccountVaultIndexEntrySubstate
from core_client.model.consensus_manager_field_config_substate import ConsensusManagerFieldConfigSubstate
from core_client.model.consensus_manager_field_current_proposal_statistic_substate import ConsensusManagerFieldCurrentProposalStatisticSubstate
from core_client.model.consensus_manager_field_current_time_rounded_to_minutes_substate import ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate
from core_client.model.consensus_manager_field_current_time_substate import ConsensusManagerFieldCurrentTimeSubstate
from core_client.model.consensus_manager_field_current_validator_set_substate import ConsensusManagerFieldCurrentValidatorSetSubstate
from core_client.model.consensus_manager_field_state_substate import ConsensusManagerFieldStateSubstate
from core_client.model.consensus_manager_field_state_substate_all_of import ConsensusManagerFieldStateSubstateAllOf
from core_client.model.consensus_manager_field_state_value import ConsensusManagerFieldStateValue
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
from core_client.model.one_resource_pool_field_state_substate import OneResourcePoolFieldStateSubstate
from core_client.model.package_blueprint_auth_template_entry_substate import PackageBlueprintAuthTemplateEntrySubstate
from core_client.model.package_blueprint_definition_entry_substate import PackageBlueprintDefinitionEntrySubstate
from core_client.model.package_blueprint_dependencies_entry_substate import PackageBlueprintDependenciesEntrySubstate
from core_client.model.package_blueprint_royalty_entry_substate import PackageBlueprintRoyaltyEntrySubstate
from core_client.model.package_code_instrumented_code_entry_substate import PackageCodeInstrumentedCodeEntrySubstate
from core_client.model.package_code_original_code_entry_substate import PackageCodeOriginalCodeEntrySubstate
from core_client.model.package_code_vm_type_entry_substate import PackageCodeVmTypeEntrySubstate
from core_client.model.package_field_royalty_accumulator_substate import PackageFieldRoyaltyAccumulatorSubstate
from core_client.model.package_schema_entry_substate import PackageSchemaEntrySubstate
from core_client.model.royalty_module_field_state_substate import RoyaltyModuleFieldStateSubstate
from core_client.model.royalty_module_method_royalty_entry_substate import RoyaltyModuleMethodRoyaltyEntrySubstate
from core_client.model.substate import Substate
from core_client.model.substate_type import SubstateType
from core_client.model.transaction_tracker_collection_entry_substate import TransactionTrackerCollectionEntrySubstate
from core_client.model.transaction_tracker_field_state_substate import TransactionTrackerFieldStateSubstate
from core_client.model.two_resource_pool_field_state_substate import TwoResourcePoolFieldStateSubstate
from core_client.model.type_info_module_field_type_info_substate import TypeInfoModuleFieldTypeInfoSubstate
from core_client.model.validator_field_protocol_update_readiness_signal_substate import ValidatorFieldProtocolUpdateReadinessSignalSubstate
from core_client.model.validator_field_state_substate import ValidatorFieldStateSubstate
globals()['AccessControllerFieldStateSubstate'] = AccessControllerFieldStateSubstate
globals()['AccessRulesModuleFieldOwnerRoleSubstate'] = AccessRulesModuleFieldOwnerRoleSubstate
globals()['AccessRulesModuleRuleEntrySubstate'] = AccessRulesModuleRuleEntrySubstate
globals()['AccountDepositRuleIndexEntrySubstate'] = AccountDepositRuleIndexEntrySubstate
globals()['AccountFieldStateSubstate'] = AccountFieldStateSubstate
globals()['AccountVaultIndexEntrySubstate'] = AccountVaultIndexEntrySubstate
globals()['ConsensusManagerFieldConfigSubstate'] = ConsensusManagerFieldConfigSubstate
globals()['ConsensusManagerFieldCurrentProposalStatisticSubstate'] = ConsensusManagerFieldCurrentProposalStatisticSubstate
globals()['ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate'] = ConsensusManagerFieldCurrentTimeRoundedToMinutesSubstate
globals()['ConsensusManagerFieldCurrentTimeSubstate'] = ConsensusManagerFieldCurrentTimeSubstate
globals()['ConsensusManagerFieldCurrentValidatorSetSubstate'] = ConsensusManagerFieldCurrentValidatorSetSubstate
globals()['ConsensusManagerFieldStateSubstate'] = ConsensusManagerFieldStateSubstate
globals()['ConsensusManagerFieldStateSubstateAllOf'] = ConsensusManagerFieldStateSubstateAllOf
globals()['ConsensusManagerFieldStateValue'] = ConsensusManagerFieldStateValue
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
globals()['OneResourcePoolFieldStateSubstate'] = OneResourcePoolFieldStateSubstate
globals()['PackageBlueprintAuthTemplateEntrySubstate'] = PackageBlueprintAuthTemplateEntrySubstate
globals()['PackageBlueprintDefinitionEntrySubstate'] = PackageBlueprintDefinitionEntrySubstate
globals()['PackageBlueprintDependenciesEntrySubstate'] = PackageBlueprintDependenciesEntrySubstate
globals()['PackageBlueprintRoyaltyEntrySubstate'] = PackageBlueprintRoyaltyEntrySubstate
globals()['PackageCodeInstrumentedCodeEntrySubstate'] = PackageCodeInstrumentedCodeEntrySubstate
globals()['PackageCodeOriginalCodeEntrySubstate'] = PackageCodeOriginalCodeEntrySubstate
globals()['PackageCodeVmTypeEntrySubstate'] = PackageCodeVmTypeEntrySubstate
globals()['PackageFieldRoyaltyAccumulatorSubstate'] = PackageFieldRoyaltyAccumulatorSubstate
globals()['PackageSchemaEntrySubstate'] = PackageSchemaEntrySubstate
globals()['RoyaltyModuleFieldStateSubstate'] = RoyaltyModuleFieldStateSubstate
globals()['RoyaltyModuleMethodRoyaltyEntrySubstate'] = RoyaltyModuleMethodRoyaltyEntrySubstate
globals()['Substate'] = Substate
globals()['SubstateType'] = SubstateType
globals()['TransactionTrackerCollectionEntrySubstate'] = TransactionTrackerCollectionEntrySubstate
globals()['TransactionTrackerFieldStateSubstate'] = TransactionTrackerFieldStateSubstate
globals()['TwoResourcePoolFieldStateSubstate'] = TwoResourcePoolFieldStateSubstate
globals()['TypeInfoModuleFieldTypeInfoSubstate'] = TypeInfoModuleFieldTypeInfoSubstate
globals()['ValidatorFieldProtocolUpdateReadinessSignalSubstate'] = ValidatorFieldProtocolUpdateReadinessSignalSubstate
globals()['ValidatorFieldStateSubstate'] = ValidatorFieldStateSubstate
from core_client.model.consensus_manager_field_state_substate import ConsensusManagerFieldStateSubstate


class TestConsensusManagerFieldStateSubstate(unittest.TestCase):
    """ConsensusManagerFieldStateSubstate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConsensusManagerFieldStateSubstate(self):
        """Test ConsensusManagerFieldStateSubstate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConsensusManagerFieldStateSubstate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()