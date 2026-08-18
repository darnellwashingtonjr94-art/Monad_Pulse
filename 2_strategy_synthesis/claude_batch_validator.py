import glob
import subprocess

def validate_all_synthesized_files():
    for filepath in glob.glob("2_strategy_synthesis/*.py"):
        res = subprocess.run(["python3", "-m", "py_compile", filepath], capture_output=True)
        if res.returncode != 0:
            print(f"Compilation error in {filepath}")
        else:
            print(f"Verified syntax for {filepath}")
