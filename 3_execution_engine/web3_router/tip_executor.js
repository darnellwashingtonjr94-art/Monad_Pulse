import { ethers } from "ethers";

// 1. Connect to Monad RPC Node
const provider = new ethers.JsonRpcProvider("RPC_URL_HERE");
const wallet = new ethers.Wallet("YOUR_PRIVATE_KEY", provider);

const contractAddress = "YOUR_DEPLOYED_CONTRACT_ADDRESS";
const abi = [ ... ]; // ABI from compiled contract above
const contract = new ethers.Contract(contractAddress, abi, wallet);

// Example 1: Send 10 MON with 2.5% optional tip
async function sendMonWithTip() {
    const tx = await contract.processMON(
        "0xDestinationRecipientAddress...", 
        true,  // applyTip = true
        250,   // tipBps = 250 (2.5%)
        { value: ethers.parseEther("10.0") }
    );
    await tx.wait();
}

// Example 2: Send 10 MON with NO tip (0%)
async function sendMonNoTip() {
    const tx = await contract.processMON(
        "0xDestinationRecipientAddress...", 
        false, // applyTip = false
        0,     // tipBps ignored
        { value: ethers.parseEther("10.0") }
    );
    await tx.wait();
}
