## README.md

### Description

This laboratory explores the fundamental nature of Python's object model. Instead of traditional variables, the lab demonstrates how names serve as bindings to objects. 
Through six distinct sections (A-F), the program illustrates the mechanics of rebinding, mutability, function argument passing, and CPython’s memory management (reference counting).

### Requirements

Computer

Python 3.10.11

### Environment Setup

Follow these steps to set up a virtual environment and install necessary dependencies:
Create a virtual environment:

```python -m venv .venv```

Activate the environment:

```.venv\Scripts\activate```

### Usage

To execute the lab and observe the behaviors, run the following command from the project root:

```python src/lab01.py```

### Program Output

The program generates a structured output divided into six sections, demonstrating the following concepts:



A) Binding / Rebinding: Shows how names point to objects and how changing a name's target doesn't affect other names.

B) Mutation vs Rebinding: Compares modifying an object in-place versus pointing a name to a new object.

C) Function Arguments: Demonstrates that passing arguments creates new local bindings.

D) Default Argument Behavior: Illustrates the "trap" where mutable default arguments are shared across function calls.

E) Copy Semantics: Highlights the difference between shallow and deep copies when dealing with nested lists.

F) Reference Counting / GC: Displays the internal reference counts of objects and explains CPython optimizations for small integers
