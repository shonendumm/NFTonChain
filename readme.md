

### Deploy contract
brownie run scripts/deploy_NFTonChain.py --network rinkeby

#### Example of minted sword
https://testnets.opensea.io/assets/0x16F2418Fe011575a5B8f14A2DCeE83A2CF0035d5/0


### How to store image data in tokenURI on chain?

1. Pass the svg file via brownie (python) during minting of coin.
2. Encode svg together with NFT metadata using Base64 library.

### Reference
Learnt from https://www.youtube.com/watch?v=QVWs9e4RFSA&t=4s&ab_channel=ArturChmaro
Artur Chmaro's code: https://gist.github.com/Chmarusso/045ee79fa9a1fae55928a613044c9067 