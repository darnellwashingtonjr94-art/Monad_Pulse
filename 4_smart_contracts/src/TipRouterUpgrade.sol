// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TipRouterUpgrade {
    address payable public constant TIP_RECIPIENT = payable(0xe7512f65508306dc669ef232bcb31a8aacd73a37);
    
    event ContractUpgraded(address indexed newImplementation);

    function triggerUpgradeNotice() external {
        emit ContractUpgraded(msg.sender);
    }
}
