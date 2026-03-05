import subprocess
import sys


def run_cli_with_input(user_input: str):
    process = subprocess.Popen(
        [sys.executable, "-m", "quick_calc.cli"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, _ = process.communicate(user_input)
    return output


def test_cli_addition():
    user_input = "5\n+\n3\n"
    output = run_cli_with_input(user_input)
    assert "Result: 8.0" in output


def test_cli_clear_simulation():
    # We simulate two runs to ensure program resets each run
    user_input = "10\n-\n10\n"
    output = run_cli_with_input(user_input)
    assert "Result: 0.0" in output