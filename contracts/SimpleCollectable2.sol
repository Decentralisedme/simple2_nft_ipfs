// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectable2 is ERC721 {
    uint256 public tokenCounter;
    // NEW
    enum Cycle {
        RIDE
    }
    mapping(uint256 => Cycle) public tokenIdToCycle;

    constructor() public ERC721("Virtual_Cycle", "BICI") {
        tokenCounter = 0;
    }

    function createCollectable() public returns (uint256) {
        // NEW
        Cycle cycle = Cycle(0);
        uint256 newTokenId = tokenCounter;
        // NEW
        tokenIdToCycle[newTokenId] = cycle;
        _safeMint(msg.sender, newTokenId);
        tokenCounter = tokenCounter + 1;
        return tokenCounter;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        // 3 tokens URI
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: caller is not owner nor Approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}
