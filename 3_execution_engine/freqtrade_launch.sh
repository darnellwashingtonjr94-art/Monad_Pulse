#!/bin/bash
echo "Launching Freqtrade Bot with Monad Strategy Integration..."
cd freqtrade
freqtrade trade --config ../config/freqtrade.config.json --strategy VibeAlphaMonad
