// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TipRouterEvents {
    event TipProcessed(address indexed sender, address indexed recipient, uint256 amount);

    function emitTipEvent(address sender, address recipient, uint256 amount) internal {
        emit TipProcessed(sender, recipient, amount);
    }
}
