import shutil
from pathlib import Path

def backup_execution_state():
    src = Path("3_execution_engine/user_data/backtest_results")
    dst = Path("3_execution_engine/user_data/backtest_backup")
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print("Freqtrade user state backed up successfully.")
