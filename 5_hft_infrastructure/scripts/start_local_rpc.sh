#!/bin/bash
echo "Booting Monad-BFT Consensus Daemon & Local IPC socket..."
cd ../monad-bft
cargo build --release
target/release/monad-bft-node --chain-id 10143 --rpc-port 8545
