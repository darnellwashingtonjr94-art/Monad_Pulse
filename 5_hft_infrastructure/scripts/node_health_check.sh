#!/bin/bash
RPC_ENDPOINT="http://localhost:8545"

response=$(curl -s -X POST -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}' \
  $RPC_ENDPOINT)

if [[ $response == *"result"* ]]; then
  echo "Monad node is healthy and responding."
  exit 0
else
  echo "Monad node health check failed."
  exit 1
fi
