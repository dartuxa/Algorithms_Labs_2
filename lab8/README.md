# Lab 08 — Iteration, Context Managers, and Descriptors

This project demonstrates how Python's core protocols work by implementing a custom `StudentCollection` and `Student` model. It features an iterator protocol for looping through students, 
a context manager for handling execution flow, and a custom descriptor for validating student grades.

### System Requirements

- Python version: 3.10 or newer (required for the match operator).

- Dependencies: mypy.

### Project Structure

```text
lab8/
├── README.md            # Instructions and project description
├── requirements.txt     # List of dependencies (empty)
├── src/                 
│   └── lab8.py          # Lab
└── report/              # Reports and explanations
    └── answers.md       # Answers to control questions
```

### Tasks Overview

The implementation covers the following tasks:

- Task A : Iteration.

- Task B : Context Manager.

- Task C : Descriptor.

- Task D : Integration.

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
python src/lab8.py
```

Static Type Checking

The project is designed to pass strict type checking. Run the following command to verify:

```
mypy --strict src/
```

It should give one error about Task C but we expect that.