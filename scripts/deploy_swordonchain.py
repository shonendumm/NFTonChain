from scripts.helpful_scripts import get_account
from brownie import SwordOnChain



# {NFT_contract_address}/{tokenId}
opensea_url = "https://testnets.opensea.io/assets/{}/{}"



def main():
    deploy_and_create_sword()

def deploy_and_create_sword():
    account = get_account()
    sword = SwordOnChain.deploy({"from": account}, publish_source = True)
    tx = sword.createCollectible({"from": account})
    tx.wait(1)
    print(f"Congrats! You can view your NFT now at {opensea_url.format(sword.address, sword.tokenCounter() - 1)}")

    print("Please wait 20 minutes, and hit the refresh metadata button")
    return sword