#!/bin/bash
echo "Monitoring CPU and RAM usage for Monad HFT infrastructure..."
top -b -n 1 | head -n 20
