# Lab 07 - Behavior, Protocols, ABC, Dataclasses, Slots

This project demonstrates the fundamentals of the Python Object Model using a custom Student class. The implementation covers:

### System Requirements

- Python version: 3.10 or newer (required for the match operator).

- Dependencies: mypy.

### Project Structure

```text
lab7/
├── README.md            # Instructions and project description
├── requirements.txt     # List of dependencies (empty)
├── src/                 
│   └── lab7.py          # Lab
└── report/              # Reports and explanations
    └── answers.md       # Answers to control questions
```

### Tasks Overview

The implementation covers the following tasks:

- Task A : Regular class (duck typing).

- Task B : Dataclass implementation.

- Task C : Slots.

- Task D : ABC version.

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
python src/lab7.py
```

Static Type Checking

The project is designed to pass strict type checking. Run the following command to verify:

```
mypy --strict src/
```

It should give one error about Task C but we expect that.