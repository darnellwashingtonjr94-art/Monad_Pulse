import importlib.util
from pathlib import Path

def load_dynamic_strategy(file_path: str):
    path = Path(file_path)
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, path.stem.capitalize(), None)
