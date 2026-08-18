import time
import glob
import subprocess

def watch_and_compile():
    print("Watching synthesis output directory for fresh alpha classes...")
    while True:
        for strat in glob.glob("2_strategy_synthesis/pending/*.py"):
            subprocess.run(["python3", "-m", "py_compile", strat])
        time.sleep(5)
