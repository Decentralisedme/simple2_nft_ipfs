from brownie import SimpleCollectable2, config, network
from scripts.helpful_scripts import get_account


def deploy_and_create():
    account = get_account()
    simp_collectable = SimpleCollectable2.deploy({"from": account})
    # simp_collectable = SimpleCollectanble2.deploy(
    #     {"from", account},
    #     publish_source=config["networks"][network.show_active()].get("verify"),
    # )
    txn_creating = simp_collectable.createCollectable({"from": account})
    txn_creating.wait(1)
    print("New token has ben created")
    return simp_collectable, txn_creating


def main():
    deploy_and_create()
