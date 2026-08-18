#!/bin/bash
echo "Gracefully stopping Monad consensus and execution engine..."
docker-compose stop monad-node
echo "Monad node stopped."
