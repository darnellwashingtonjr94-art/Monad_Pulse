import pickle
from pathlib import Path

def save_vector_cache(data, cache_path="1_research_agents/vibe_trading/cache/embeddings.pkl"):
    Path(cache_path).parent.mkdir(parents=True, exist_ok=True)
    with open(cache_path, "wb") as f:
        pickle.dump(data, f)
    print("Vibe-Trading factor vectors cached successfully.")
