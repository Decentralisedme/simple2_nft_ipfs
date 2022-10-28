from brownie import config, network, accounts

LOCAL_BLOCKCHAIN_ENV = ["mainnet-fork-dev", "mainnet-fork", "development"]
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"
CYCLE_MAPPING = {0: "NIGHT"}


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load.id
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    if network.show_active() in config["networks"]:
        account = accounts.add(config["wallets"]["from_key"])
        return account
    return None


def get_cycle(cycle_number):
    return CYCLE_MAPPING[cycle_number]
