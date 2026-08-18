#!/bin/bash
echo "Tearing down Monad HFT infrastructure containers..."
docker-compose down -v
docker system prune -f
echo "Environment cleaned successfully."
