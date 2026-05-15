# Async Batch Processor


A command-line interface (CLI) tool designed to process a batch of tasks in various execution modes. This tool simulates I/O-bound task processing to demonstrate sequential execution, concurrent execution, and controlled concurrency using semaphores, now featuring a comprehensive test suite.


## Project Structure


The project follows the directory layout below:

```
lab12/
├── src/
│   └── async_tool/
│       ├── __init__.py
│       ├── __main__.py
│       ├── classes.py
│       └── functions.py
├── tests/
│   ├── __init__.py
│   ├── test_process_item.py
│   └── test_cli.py
└── report/
    └── answers.md
```


## Prerequisites


- Python: Version 3.11 or higher is required.

- Dependencies: The core tool utilizes built-in Python libraries : ```asyncio```, ```argparse```, ```json```, ```pathlib```
and libraries such as ```pytest``` and ```pytest-asyncio``` which need to be installed.

- Typing: The code is designed to pass ```mypy --strict``` and ```pytest``` checks.


## Setup


Install the testing dependencies:

```
pip install pytest pytest-asyncio
```


## Usage


Run the tool as a module from the src/ directory:


```
python -m async_tool input.json [OPTIONS]
```

You can also run tests with:

```
python -m pytest tests/ -v
```


## Arguments


### Required Argument:


- ```input.json```: The path to the input JSON file containing the batch tasks.


### Options:

- ```--mode {sync,async,limited}```: Determines the execution behavior.

    - ```sync```: Sequential execution (default).

    - ```async```: Runs all tasks concurrently.

    - ```limited```: Runs tasks concurrently but restricts the number of active tasks.


- ```--limit N```: Sets the concurrency limit. Used exclusively with ```--mode limited``` (Default: 5).

- ```--continue-on-error```: Dictates error handling behavior.

    - If not provided: The program stops on the first error and exits with a non-zero code.

    - If provided: All tasks are processed, and failed tasks produce standard error results.

- ```--log-level {DEBUG,INFO,WARNING,ERROR}```: Sets the logging threshold (Default: WARNING).


## Data Formats


### Input Format

The tool receives a JSON file containing a list of tasks. Each task object must contain the following attributes:

- ```id```: A unique identifier.

- ```delay```: The time to wait in seconds.

- ```good```: A boolean indicating whether the task succeeds or fails.


#### Example input.json:


```
[
    {"id": 1, "delay": 1, "good": true},
    {"id": 2, "delay": 2, "good": false},
    {"id": 3, "delay": 1, "good": true}
]
```


### Output Format


The program prints the final results as valid JSON to standard output (```stdout```).

- The output order will strictly match the input order.

- Each task will produce exactly one result.


### Example Output (with ```--continue-on-error```):


```
[
  {
    "id": 1,
    "status": "done"
  },
  {
    "id": 2,
    "status": "error",
    "message": "Task 2 failed"
  },
  {
    "id": 3,
    "status": "done"
  }
]
```