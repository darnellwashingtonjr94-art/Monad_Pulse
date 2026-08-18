#!/bin/bash
set -e
echo "Building Category Labs Monad C++ Execution Engine..."
cd ../monad
mkdir -p build && cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j$(nproc)
echo "Monad C++ build finished successfully."
