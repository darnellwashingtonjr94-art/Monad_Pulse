import subprocess

def format_strategy_code(file_path: str):
    """Applies black/flake8 formatting rules to Claude-generated Python strategies."""
    subprocess.run(["black", file_path], capture_output=True)
    print(f"Formatted strategy file: {file_path}")
