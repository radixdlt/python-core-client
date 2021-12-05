from dataclasses import dataclass
import system_client as system_api
from system_client.api import default_api
import core_client as core_api
from core_client.api import entity_api
from core_client.api import construction_api
from core_client.api import network_api
from core_client.api import sign_api
from core_client.model.data import Data
from core_client.model.entity_request import EntityRequest
from core_client.model.sign_request import SignRequest
from core_client.model.sub_entity import SubEntity
from core_client.model.sub_entity_metadata import SubEntityMetadata
from core_client.model.prepared_validator_owner import PreparedValidatorOwner
from core_client.model.prepared_validator_registered import PreparedValidatorRegistered
from core_client.model.validator_allow_delegation import ValidatorAllowDelegation
from core_client.model.prepared_validator_fee import PreparedValidatorFee
from core_client.model.validator_metadata import ValidatorMetadata
from core_client.model.network_status_request import NetworkStatusRequest
from core_client.model.construction_build_request import ConstructionBuildRequest
from core_client.model.construction_submit_request import ConstructionSubmitRequest
from core_client.model.resource_amount import ResourceAmount
from core_client.model.stake_unit_resource_identifier import StakeUnitResourceIdentifier
from core_client.model.token_resource_identifier import TokenResourceIdentifier
from core_client.model.resource_identifier import ResourceIdentifier
from core_client.model.rri import RRI
from core_client.model.operation import Operation
from core_client.model.operation_group import OperationGroup
from core_client.model.big_integer import BigInteger
from core_client.model.entity_identifier import EntityIdentifier
from core_client.model.network_identifier import NetworkIdentifier

def get_health(api_client):
    api = default_api.DefaultApi(api_client)
    return api.system_health_get()

def get_version(api_client):
    api = default_api.DefaultApi(api_client)
    return api.system_version_get()

def get_metrics(api_client):
    api = default_api.DefaultApi(api_client)
    return api.system_metrics_get()

def get_peers(api_client):
    api = default_api.DefaultApi(api_client)
    return api.system_peers_get()

def get_address_book(api_client):
    api = default_api.DefaultApi(api_client)
    return api.system_addressbook_get()

def get_configuration(api_client):
    api = default_api.DefaultApi(api_client)
    return api.system_configuration_get()

def get_account_info(api_client):
    api = network_api.NetworkApi(api_client)
    network_identifier = api.network_configuration_post(dict()).network_identifier
    node_identifiers = get_node_identifiers(api_client)
    account_entity_identifier = node_identifiers.account_entity_identifier
    api = entity_api.EntityApi(api_client)
    account = api.entity_post(EntityRequest(
        network_identifier = network_identifier,
        entity_identifier = account_entity_identifier
    ))
    return {
        'account_identifier': account_entity_identifier,
        'balances': account.balances
    }

def get_validator_info(api_client):
    api = network_api.NetworkApi(api_client)
    network_identifier = api.network_configuration_post(dict()).network_identifier
    node_identifiers = get_node_identifiers(api_client)
    validator_entity_identifier = node_identifiers.validator_entity_identifier
    api = entity_api.EntityApi(api_client)
    validator_data_objects = api.entity_post(EntityRequest(
        network_identifier = network_identifier,
        entity_identifier = validator_entity_identifier
    )).data_objects

    validator_system_entity_identifier = EntityIdentifier(
        address = validator_entity_identifier.address,
        sub_entity = SubEntity(
            address = 'system'
        )
    )
    validator_system = api.entity_post(EntityRequest(
            network_identifier = network_identifier,
            entity_identifier = validator_system_entity_identifier
        ))
    validator_system_data_objects = validator_system.data_objects

    return {
        'balances': validator_system.balances,
        'data_objects': validator_data_objects + validator_system_data_objects
    }

def set_validator_metadata(name, url):
    return lambda node_identifiers : [
            OperationGroup([
                Operation(
                    type = "Data",
                    entity_identifier = node_identifiers.validator_entity_identifier,
                    data = Data(
                        action = 'CREATE',
                        data_object = ValidatorMetadata(
                            type = "ValidatorMetadata",
                            name = name,
                            url = url
                        )
                    )
                )
            ]),
        ]

def set_validator_registered(registered):
    return lambda node_identifiers : [
            OperationGroup([
                Operation(
                    type = "Data",
                    entity_identifier = node_identifiers.validator_entity_identifier,
                    data = Data(
                        action = 'CREATE',
                        data_object = PreparedValidatorRegistered(
                            type = "PreparedValidatorRegistered",
                            registered = registered
                        )
                    )
                )
            ])
        ]

def set_validator_fee(fee):
     return lambda node_identifiers : [
             OperationGroup([
                 Operation(
                     type = "Data",
                     entity_identifier = node_identifiers.validator_entity_identifier,
                     data = Data(
                         action = 'CREATE',
                         data_object = PreparedValidatorFee(
                             type = "PreparedValidatorFee",
                             fee = fee
                         )
                     )
                 )
             ]),
         ]

def set_validator_allow_delegation(allow_delegation):
     return lambda node_identifiers : [
             OperationGroup([
                 Operation(
                     type = "Data",
                     entity_identifier = node_identifiers.validator_entity_identifier,
                     data = Data(
                         action = 'CREATE',
                         data_object = ValidatorAllowDelegation(
                             type = "ValidatorAllowDelegation",
                             allow_delegation = allow_delegation
                         )
                     )
                 )
             ]),
         ]

def set_validator_owner(owner):
      return lambda node_identifiers : [
              OperationGroup([
                  Operation(
                      type = "Data",
                      entity_identifier = node_identifiers.validator_entity_identifier,
                      data = Data(
                          action = 'CREATE',
                          data_object = PreparedValidatorOwner(
                              type = "PreparedValidatorOwner",
                              owner = EntityIdentifier(address = owner)
                          )
                      )
                  )
              ]),
          ]

def transfer_tokens(rri, amount, receiver):
    return lambda node_identifiers : [
            OperationGroup([
                Operation(
                    type = "Resource",
                    entity_identifier = node_identifiers.account_entity_identifier,
                    amount = ResourceAmount(
                        BigInteger('-' + amount),
                        TokenResourceIdentifier(type = "Token", rri = RRI(rri))
                    )
                ),
                Operation(
                    type = "Resource",
                    entity_identifier = EntityIdentifier(address = receiver),
                    amount = ResourceAmount(
                        BigInteger(amount),
                        TokenResourceIdentifier(type = "Token", rri = RRI(rri))
                    )
                )
            ])
        ]

def stake_tokens(rri, amount, validator):
     return lambda node_identifiers : [
             OperationGroup([
                 Operation(
                     type = "Resource",
                     entity_identifier = node_identifiers.account_entity_identifier,
                     amount = ResourceAmount(
                         BigInteger('-' + amount),
                         TokenResourceIdentifier(type = "Token", rri = RRI(rri))
                     )
                 ),
                 Operation(
                     type = "Resource",
                     entity_identifier = EntityIdentifier(
                        address = node_identifiers.account_entity_identifier.address,
                        sub_entity = SubEntity(
                            address = 'prepared_stake',
                            metadata = SubEntityMetadata(
                                validator_address = validator
                            )
                        )
                     ),
                     amount = ResourceAmount(
                         BigInteger(amount),
                         TokenResourceIdentifier(type = "Token", rri = RRI(rri))
                     )
                 )
             ])
         ]

def unstake_stake_units(amount, validator):
     return lambda node_identifiers : [
             OperationGroup([
                  Operation(
                      type = "Resource",
                      entity_identifier = node_identifiers.account_entity_identifier,
                      amount = ResourceAmount(
                          BigInteger('-' + amount),
                          StakeUnitResourceIdentifier(type = "StakeUnit", validator_address = validator)
                      )
                  ),
                  Operation(
                      type = "Resource",
                      entity_identifier = EntityIdentifier(
                         address = node_identifiers.account_entity_identifier.address,
                         sub_entity = SubEntity(
                             address = 'prepared_unstake'
                         )
                      ),
                      amount = ResourceAmount(
                          BigInteger(amount),
                          StakeUnitResourceIdentifier(type = "StakeUnit", validator_address = validator)
                      )
                  )
              ])
          ]


def submit_action(api_client, actions):
    api = network_api.NetworkApi(api_client)
    network_identifier = api.network_configuration_post(dict()).network_identifier
    node_identifiers = get_node_identifiers(api_client)
    public_key = node_identifiers.public_key
    account_entity_identifier = node_identifiers.account_entity_identifier
    api = construction_api.ConstructionApi(api_client)

    # flatmap
    operation_groups = []
    for action in actions:
        for operation_group in action(node_identifiers):
            operation_groups.append(operation_group)

    build = api.construction_build_post(ConstructionBuildRequest(
        network_identifier = network_identifier,
        fee_payer = account_entity_identifier,
        operation_groups = operation_groups
    ))
    unsigned_transaction = build.unsigned_transaction

    api = sign_api.SignApi(api_client)
    response = api.sign_post(SignRequest(
        network_identifier = network_identifier,
        public_key = public_key,
        unsigned_transaction = unsigned_transaction
    ))

    api = construction_api.ConstructionApi(api_client)
    response = api.construction_submit_post(ConstructionSubmitRequest(
        network_identifier = network_identifier,
        signed_transaction = response.signed_transaction
    ))
    return response

def get_node_identifiers(api_client):
    api = network_api.NetworkApi(api_client)
    network_identifier = api.network_configuration_post(dict()).network_identifier
    status = api.network_status_post(NetworkStatusRequest(network_identifier = network_identifier))
    return status.node_identifiers

if __name__ == "__main__":
    system_config = system_api.Configuration("http://localhost:3333")
    with system_api.ApiClient(system_config) as api_client:
        print(get_health(api_client))
        # print(get_version(api_client))
        # print(get_configuration(api_client))

    config = core_api.Configuration("http://localhost:3333")
    with core_api.ApiClient(config) as api_client:
        print(get_node_identifiers(api_client))
        actions = [
            set_validator_metadata('Validator', 'https://www.google.com'),
            set_validator_registered(True)
            # set_validator_owner('ddx1qspll7tm6464am4yypzn59p42g6a8qhkguhc269p3vhs27s5vq5h24sfvvdfj')
            # set_validator_allow_delegation(True)
            # set_validator_fee(500) # 5%
            # transfer_tokens('xrd_dr1qyrs8qwl', '1000', 'ddx1qspll7tm6464am4yypzn59p42g6a8qhkguhc269p3vhs27s5vq5h24sfvvdfj')
            # stake_tokens('xrd_dr1qyrs8qwl', '90000000000000000000', 'dv1q0llj774w40wafpqg5apgd2jxhfc9aj897zk3gvt9uzh59rq9964vjryzf9')
            # unstake_stake_units('100000000000000000', 'dv1q0llj774w40wafpqg5apgd2jxhfc9aj897zk3gvt9uzh59rq9964vjryzf9')
        ]
        print(submit_action(api_client, actions))
