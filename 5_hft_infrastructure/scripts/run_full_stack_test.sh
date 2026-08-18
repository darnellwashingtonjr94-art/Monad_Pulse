#!/bin/bash
set -e
echo "Executing complete end-to-end integration test harness..."
python3 -m unittest discover -s 4_smart_contracts/test
echo "All integration sanity checks passed."
