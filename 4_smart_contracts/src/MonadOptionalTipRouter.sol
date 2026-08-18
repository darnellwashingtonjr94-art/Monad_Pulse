// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MonadOptionalTipRouter {
    address payable public constant TIP_RECIPIENT = payable(0xe7512f65508306dc669ef232bcb31a8aacd73a37);
    uint256 public constant MIN_TIP_BPS = 250; 

    function processMON(address payable recipient, bool applyTip, uint256 tipBps) external payable {
        require(msg.value > 0, "Zero value");
        uint256 tip = 0;
        uint256 net = msg.value;
        if (applyTip) {
            require(tipBps >= MIN_TIP_BPS, "Min 2.5% tip required");
            tip = (msg.value * tipBps) / 10000;
            net = msg.value - tip;
            (bool s1, ) = TIP_RECIPIENT.call{value: tip}("");
            require(s1, "Tip send failed");
        }
        (bool s2, ) = recipient.call{value: net}("");
        require(s2, "Main send failed");
    }
}
