const { ethers } = require("hardhat");

async function main() {
  const Router = await ethers.getContractFactory("MonadOptionalTipRouter");
  console.log("Deploying MonadOptionalTipRouter to Monad EVM...");
  
  const router = await Router.deploy();
  await router.waitForDeployment();

  console.log(`Router deployed to: ${await router.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
