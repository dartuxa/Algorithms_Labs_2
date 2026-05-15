import json
import subprocess
import pytest
from pathlib import Path


def run_cli(input_path: Path, *args) -> subprocess.CompletedProcess:

    cmd = ["python", "-m", "src.async_tool", str(input_path)] + list(args)

    return subprocess.run(cmd, capture_output=True, text=True, timeout=5)

def test_cli_basic_execution_and_structure(tmp_path: Path):

    input_data = [
        {"id": 1, "delay": 0.01, "good": True},
        {"id": 2, "delay": 0.01, "good": True}
    ]
    
    input_file = tmp_path / "input.json"
    input_file.write_text(json.dumps(input_data))

    result = run_cli(input_file)

    assert result.returncode == 0

    output_data = json.loads(result.stdout)
    
    assert len(output_data) == 2
    assert output_data[0]["id"] == 1
    assert output_data[1]["id"] == 2
    assert output_data[0]["status"] == "done"

def test_cli_mode_behavior(tmp_path: Path):
    
    input_data = [{"id": 1, "delay": 0.01, "good": True}]
    input_file = tmp_path / "input.json"
    input_file.write_text(json.dumps(input_data))

    result = run_cli(input_file, "--mode", "async")

    assert result.returncode == 0
    output_data = json.loads(result.stdout)
    assert output_data[0]["status"] == "done"

def test_cli_error_without_flag(tmp_path: Path):

    input_data = [{"id": 1, "delay": 0.01, "good": False}]
    input_file = tmp_path / "input.json"
    input_file.write_text(json.dumps(input_data))

    result = run_cli(input_file)

    assert result.returncode != 0

def test_cli_error_with_flag(tmp_path: Path):

    input_data = [
        {"id": 1, "delay": 0.01, "good": True},
        {"id": 2, "delay": 0.01, "good": False}
    ]
    input_file = tmp_path / "input.json"
    input_file.write_text(json.dumps(input_data))

    result = run_cli(input_file, "--continue-on-error")

    assert result.returncode == 0

    output_data = json.loads(result.stdout)
    
    assert len(output_data) == 2
    assert output_data[1]["id"] == 2
    assert output_data[1]["status"] == "error"
    
    assert "message" in output_data[1]