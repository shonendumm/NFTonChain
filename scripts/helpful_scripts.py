from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENV = ["hardhat", "development", "ganache", "mainnet-fork"]

def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts[id]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENV:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])