//SPDX-License-Identifier: MIT
pragma solidity =0.8.11;

import "@openzeppelin/contracts/token/ERC1155/presets/ERC1155PresetMinterPauser.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract RKLCollection is ERC1155PresetMinterPauser("ipfs://QmRPAQFr3d1ueXmKF4yfbTMHV3MRYaqKZ9Z3QQF5vytpyk/") {
  function setURI(string calldata newuri) external {
    require(hasRole(DEFAULT_ADMIN_ROLE, _msgSender()), "ERC1155PresetMinterPauser: must have admin role to set new uri");
    _setURI(newuri);
  }

  function uri(uint256 tokenId) override public view returns (string memory) {
    return string(abi.encodePacked(ERC1155.uri(tokenId), Strings.toString(tokenId)));
  }
}
