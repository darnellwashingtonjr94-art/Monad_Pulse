import os
from pathlib import Path

def bootstrap_directories():
    dirs = [
        "1_research_agents/custom_skills",
        "2_strategy_synthesis/tests",
        "2_strategy_synthesis/strategy_templates",
        "3_execution_engine/user_data/strategies",
        "3_execution_engine/user_data/hyperopts",
        "3_execution_engine/web3_router",
        "4_smart_contracts/src",
        "4_smart_contracts/test",
        "4_smart_contracts/scripts",
        "5_hft_infrastructure/scripts"
    ]
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
    print("All project subdirectories successfully bootstrapped.")

if __name__ == "__main__":
    bootstrap_directories()
