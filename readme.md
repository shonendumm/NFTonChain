

### Deploy contract
brownie run scripts/deploy_NFTonChain.py --network rinkeby

#### Example of minted NFT
https://testnets.opensea.io/assets/0x9C5b4F4a8746B0E4379F252c019D8FeF15B2ff20/0


### How to store image data in tokenURI on chain?

1. Pass the svg file via brownie (python) during minting of coin.
2. Encode svg together with NFT metadata using Base64 library.

### Reference
Learnt from https://www.youtube.com/watch?v=QVWs9e4RFSA&t=4s&ab_channel=ArturChmaro
Artur Chmaro's code: https://gist.github.com/Chmarusso/045ee79fa9a1fae55928a613044c9067 