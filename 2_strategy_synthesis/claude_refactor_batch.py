import subprocess
import glob

def batch_refactor_strategies():
    for filepath in glob.glob("2_strategy_synthesis/pending/*.py"):
        print(f"Running Claude Code optimization pass on {filepath}...")
        subprocess.run(["claude", "-p", f"Optimize this script for zero-latency execution: {filepath}"])
