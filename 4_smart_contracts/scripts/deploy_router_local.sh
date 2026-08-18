#!/bin/bash
set -e
echo "Deploying MonadOptionalTipRouter to local development instance..."
npx hardhat run scripts/deploy.js --network monadTestnet
