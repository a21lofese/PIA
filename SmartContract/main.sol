// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.0;

contract Messenger {
    address owner;
    string[] messages;

    constructor() {
        owner = msg.sender;
    }

    function add(string calldata newMsg) public {
        require(msg.sender == owner, "Error, solo el propietario puede!");
        messages.push(newMsg);
    }

    function count() public view returns (uint256) {
        return messages.length;
    }

    function getMessages(uint256 index) public view returns (string memory) {
        return messages[index];
    }
}
