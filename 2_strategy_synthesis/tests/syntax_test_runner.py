import subprocess
import glob

def test_generated_strategies():
    strategies = glob.glob("3_execution_engine/user_data/strategies/*.py")
    for strat in strategies:
        result = subprocess.run(["python3", "-m", "py_compile", strat], capture_output=True)
        assert result.returncode == 0, f"Compilation failed for {strat}: {result.stderr.decode()}"
    print("All synthesized strategy scripts passed syntax verification.")
