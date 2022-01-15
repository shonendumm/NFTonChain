// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "./Base64.sol";

contract NFTonChain is ERC721 {
    uint256 public tokenCounter;
    // we map and store each token's SVG so that we can retrieve them later when tokenURI is called
    mapping(uint256 => string) public tokenIdtoSVG;

    constructor() ERC721("NFT on Chain", "NOC") {
        // initialize tokenCounter to 0, for token id
        tokenCounter = 0;
    }

    function createCollectible(string memory input) public returns(string memory) {
        // use tokenCounter as an id for each created token
        // use _safeMint inherited from ERC721 contract to mint a token
        
        tokenIdtoSVG[tokenCounter] = input;
        _safeMint(msg.sender, tokenCounter);
        string memory createdTokenURI = tokenURI(tokenCounter);
        tokenCounter = tokenCounter + 1;

        return createdTokenURI;
    }

    function getImageSVG(uint256 _tokenId) public view returns (string memory) {
        return tokenIdtoSVG[_tokenId];
    }


    function tokenURI(uint256 tokenId) override(ERC721) public view returns (string memory) {
        string memory svg = getImageSVG(tokenId);
        string memory json = Base64.encode(
            bytes(string(
                abi.encodePacked(
                    '{"name": ', '"Example NFT",',
                    '"image_data": "',svg,'"}' 
                )
            ))
        );
        return string(abi.encodePacked('data:application/json;base64,', json));

    }


}