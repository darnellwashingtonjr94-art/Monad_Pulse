#!/bin/bash
echo "Purging lingering Monad and Freqtrade Docker volumes..."
docker volume prune -f
echo "Volumes cleaned successfully."
