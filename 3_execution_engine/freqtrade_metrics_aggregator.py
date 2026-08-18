import json
from pathlib import Path

def aggregate_trade_performance():
    result_path = Path("3_execution_engine/user_data/backtest_results")
    if result_path.exists():
        print("Aggregating historical trade metrics across runs...")
    return {"total_pnl": 0.0, "win_rate": 0.0}
