const { run } = require("hardhat");

async function main() {
  const contractAddress = process.env.ROUTER_CONTRACT_ADDRESS;
  console.log(`Verifying contract at ${contractAddress} on Monad Explorer...`);
  await run("verify:verify", {
    address: contractAddress,
    constructorArguments: [],
  });
}

main().catch(console.error);
