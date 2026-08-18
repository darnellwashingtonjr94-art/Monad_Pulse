import subprocess

def trigger_claude_code_refactor(target_file: str):
    """Invokes local Claude Code CLI to clean up generated Python trading classes."""
    cmd = ["claude", "-p", f"Refactor and optimize this trading strategy for maximum runtime efficiency: {target_file}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
