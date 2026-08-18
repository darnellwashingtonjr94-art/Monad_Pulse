from pathlib import Path

def clean_old_logs(max_age_days=7):
    logs_dir = Path("3_execution_engine/user_data/backtest_results")
    if logs_dir.exists():
        for file in logs_dir.glob("*.json"):
            file.unlink()
        print("Cleared historical backtest artifacts.")
