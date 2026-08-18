import sys
import importlib.util

def validate_strategy_syntax(file_path: str) -> bool:
    spec = importlib.util.spec_from_file_location("strategy_module", file_path)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        return True
    except Exception as e:
        print(f"Strategy validation error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        validate_strategy_syntax(sys.argv[1])
