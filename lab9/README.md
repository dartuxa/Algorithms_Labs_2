# Report Tool

A simple and reliable Python utility designed to process numeric data, perform statistical analysis, and generate formatted text reports. This tool was refactored as part of a lab assignment to demonstrate clean code principles, proper package structure, and a stable public API.

## Features

* **Data Parsing**: Converts string input (comma or semicolon separated) into numeric lists[cite: 122].
* **Statistical Analysis**: Calculates sum, count, minimum, maximum, and mean values.
* **Formatted Reporting**: Generates clean, human-readable text reports with optional data sorting.
* **File Management**: Saves generated reports to text files and allows reading them back for verification.

## Project Structure

```text
lab09/report_tool
├── README.md
├── requirements.txt
├── src/
│   └── report_tool/
│       ├── __init__.py
│       ├── __main__.py
│       ├── helpers.py
│       ├── textstuff.py
│       └── saveit.py
└── report/
    └── report.md
```

## Installation

Ensure you have Python 3.x installed.

Navigate to the project root directory.

(Optional) Install dependencies (though currently, only the standard library is used):

```
pip install -r requirements.txt
```

## Usage

Running as a Package

You can run the tool directly as a module to see a demonstration of its capabilities:

```
# From the /src directory:

python -m report_tool
```

This will display a help message, an example workflow, and demonstrate the file saving/reading features.

## Running Individual Modules

Each module can be executed independently to see its specific documentation and usage examples:

```
python src/report_tool/functions.py

python src/report_tool/report_output.py
```

## Using as a Library

You can import the tool's public functions directly from the package into your own scripts:

```
from report_tool import parse_numbers, analyze_numbers, build_report

data = "10, 20, 30.5"
numbers = parse_numbers(data)
stats = analyze_numbers(numbers)
print(build_report(stats))
```

## Public API

The following functions are available as part of the public API:

```parse_numbers(text)```: Parses strings into lists of floats.

```analyze_numbers(numbers)```: Returns a dictionary with statistics.

```build_report(stats)```: Formats statistics into a string.

```save_report(text, filename)```: Saves text to a .txt file.

```read_back(filepath)```: Reads content from a file.
