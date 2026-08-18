import os

def run_full_audit():
    folders = [
        "1_research_agents",
        "2_strategy_synthesis",
        "3_execution_engine",
        "4_smart_contracts",
        "5_hft_infrastructure"
    ]
    for f in folders:
        assert os.path.isdir(f), f"Missing core folder: {f}"
    print("Monad-Pulse-Node workspace directory layout validated successfully.")

if __name__ == "__main__":
    run_full_audit()
