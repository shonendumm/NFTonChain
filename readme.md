

### Deploy contract
brownie run scripts/swordonchain2.py --network rinkeby

#### Example of minted sword
https://testnets.opensea.io/assets/0x1bd0EEAD20A0c927994e40A09E1CD5d160a3087e/0 


### How to store image data in tokenURI on chain?

1. Pass the svg file via brownie (python) during minting of coin.
2. Encode svg together with NFT metadata using Base64 library.

