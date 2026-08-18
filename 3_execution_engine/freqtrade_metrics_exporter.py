import json
from pathlib import Path

def export_execution_metrics():
    state_file = Path("3_execution_engine/user_data/backtest_results/latest_metrics.json")
    if state_file.exists():
        data = json.loads(state_file.read_text())
        print(f"Active Trades Count: {data.get('total_trades', 0)}")
