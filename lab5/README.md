# Lab 05: Type Hints, Generics, and Mypy

This project focuses on practicing Python type annotations and using the mypy static analysis tool to improve code reliability and clarity .

### System Requirements

- Python version: 3.10 or newer (required for the match operator).

- Dependencies: ```mypy```.

### Project Structure

```text
lab5/
├── README.md            # Instructions and project description
├── requirements.txt     # List of dependencies (empty)
├── src/                 
│   └── lab5.py          # Lab
└── report/              # Reports and explanations
    └── answers.md       # Answers to control questions
```

### Tasks Overview

The implementation covers the following tasks:

- Task A & B: Basic type annotations for functions and typed collections (e.g., ```List[int]```).

- Task C: Implementation of ```Optional``` types (Union of ```int | None```) for safe data searching .

- Task D & F: Working with higher-order functions using the ```Callable``` type, including functions that return other functions .

- Task E: Introduction of Generics using ```TypeVar``` to create flexible, type-safe functions.

- Task G: A data processing Pipeline utilizing lambda expressions and generator expressions to filter, transform, and aggregate data .

### Environment Setup

To ensure a clean installation of dependencies, follow these steps in your terminal:

- Create a virtual environment:
```
python -m venv venv
```
- Activate the environment:
```
venv\Scripts\activate
```
- Install required packages:
```
pip install -r requirements.txt
```

### Running the Project

Execute the Code

To run the main program and see the task demonstrations, use:
```
python src/lab5.py
```

Static Type Checking

The project is designed to pass strict type checking. Run the following command to verify:

```
mypy --strict src/
```
