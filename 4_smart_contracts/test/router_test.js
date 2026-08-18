const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("MonadOptionalTipRouter", function () {
  it("Should route funds and enforce 2.5% minimum tip", async function () {
    const [owner, recipient] = await ethers.getSigners();
    const Router = await ethers.getContractFactory("MonadOptionalTipRouter");
    const router = await Router.deploy();
    
    const sendVal = ethers.parseEther("1.0");
    await expect(
      router.processMON(recipient.address, true, 200, { value: sendVal })
    ).to.be.revertedWith("Min 2.5% tip required");
  });
});
