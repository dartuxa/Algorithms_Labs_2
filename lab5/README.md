# Lab 04: Higher-Order Functions and Decorators

This project focuses on practicing higher-order functions, functional transformations using ```map``` and ```filter```, and modifying function behavior with decorators.

### System Requirements

- Python version: 3.10 or newer (required for the match operator).

- Dependencies: No external libraries required.

### Project Structure

```text
lab4/
├── README.md            # Instructions and project description
├── requirements.txt     # List of dependencies (empty)
├── src/                 
│   └── lab4.py          # Lab
└── report/              # Reports and explanations
    └── answers.md       # Answers to control questions
```

### Tasks Overview

The implementation covers the following tasks:

- Task A (Higher-Order Function): Implementation of a custom ```apply(func, data)``` function without using built-in map .

- Task B (map): Transforming lists by squaring numbers and converting them to strings .

- Task C (filter): Filtering lists to keep only even numbers or values greater than 10 .

- Task D (map/filter vs comprehension): Solving the same transformation task using two different Pythonic approaches .

- Task E (Simple Decorator): A ```@call_counter``` decorator that tracks and prints the number of times a function is executed .

- Task F (Decorator with Arguments): A ```@prefix(text)``` decorator that prepends a specific string to the function's return value .

- Task G (Caching Decorator): A ```@cache``` decorator used to optimize recursive calculations by storing previously computed results .

### Execution Instructions

To run the laboratory work code, execute the following command from the project root directory :
```
python src/lab4.py
```
