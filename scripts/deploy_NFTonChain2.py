from scripts.helpful_scripts import get_account
from brownie import NFTonChain2
import json


# {NFT_contract_address}/{tokenId}
opensea_url = "https://testnets.opensea.io/assets/{}/{}"



def get_file():
    svg = open("img/cryptopunks00.svg") 
    loaded_svg = svg.read()
    print(loaded_svg)
    print(type(loaded_svg))
    return loaded_svg

def get_metadata():
    with open("./metadata/etherOrcsDecoded.json", "r") as jsonfile:
        jsonObject = json.load(jsonfile)
        metadata = json.dumps(jsonObject)
    return metadata


def main():
    metadata = get_metadata()
    deploy_and_create_nft(metadata)

def deploy_and_create_nft(loaded_svg):
    account = get_account()
    nftContract = NFTonChain2.deploy({"from": account}, publish_source = True)
    tx = nftContract.createCollectible(loaded_svg, {"from": account})
    tx.wait(1)
    print(f"Congrats! You can view your NFT now at {opensea_url.format(nftContract.address, nftContract.tokenCounter() - 1)}")

    print("Please wait 20 minutes, and hit the refresh metadata button")
    return nftContract