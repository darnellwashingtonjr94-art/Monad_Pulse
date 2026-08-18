// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TipRouterStorage {
    mapping(address => uint256) public totalTipsContributed;

    function recordTip(address contributor, uint256 amount) internal {
        totalTipsContributed[contributor] += amount;
    }
}
