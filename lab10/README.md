# Report Tool

A powerful and flexible Python CLI utility designed to process numeric data, perform statistical analysis, and generate reports in multiple formats. Refactored in Lab 10 to support command-line arguments, file-based I/O, JSON export, and professional logging.

# Features

- CLI Interface: Fully controllable via command-line arguments (input, output, format, and logging).

- Flexible Data Parsing: Handles numeric input from files with various delimiters (commas, semicolons, or spaces).

- Advanced Analysis: Calculates comprehensive statistics (sum, count, min, max, mean).

- Multi-format Output: Supports both human-readable Text reports and machine-readable JSON data.

- Robust Logging: Integrated Python logging with adjustable verbosity levels for better debugging and transparency.

# Project Structure

```
lab10/
├── README.md
├── requirements.txt
├── src/
│   └── report_tool/
│       ├── __init__.py
│       ├── __main__.py
│       ├── functions.py
│       ├── report_output.py
│       └── saveit.py
└── report/
    └── report.md
```

# Installation

Ensure you have Python 3.6+ installed.

- Navigate to the project root directory.

- (Optional) Install dependencies:

```
pip install -r requirements.txt
```

# Usage

Running as a CLI Tool

The tool is designed to be executed as a module. Use the following syntax:

```
python -m report_tool --input <input_file> --out <output_file> --format <text|json> --log-level <DEBUG|INFO|WARNING|ERROR>
```

# Example Commands

Generate a standard text report:

```
python -m report_tool --input data.txt --out report.txt --format text --log-level INFO
```

Generate a JSON report with detailed debugging logs:

```
python -m report_tool --input numbers.txt --out data.json --format json --log-level DEBUG
```

# Using as a Library

You can still import the tool's public API directly into your scripts:

```
from report_tool import parse_numbers, analyze_numbers, build_json_report

data = "1,2; 3 4.5"
numbers = parse_numbers(data)
stats = analyze_numbers(numbers)

# Get JSON string
json_output = build_json_report(stats)
print(json_output)
```

# Public API

The following functions are exposed via ```__init__.py```:

- ```parse_numbers(text)```: Parses strings into lists of floats (supports ```,```, ```;```, and ``` ```).

- ```analyze_numbers(numbers)```: Returns a dictionary with statistical calculations.

- ```build_sorted_report(numbers, stats)```: Formats statistics into a sorted text string.

- ```build_json_report(stats)```: Formats statistics into a JSON string.

- ```read_input_file(path)```: Reads raw data from a file using ```pathlib```.

- ```save_report(text, path)```: Saves content to the specified path.