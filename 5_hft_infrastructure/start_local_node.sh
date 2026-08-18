#!/bin/bash
echo "Initializing Monad C++ Execution Engine & Monad-BFT Consensus..."

# Load local node configurations
export MONAD_CHAIN_ID=10143
export RPC_PORT=8545

# Start local container or binary daemon
docker-compose -f docker-compose.yml up -d monad-node monad-bft

echo "Monad node active on http://localhost:$RPC_PORT"
