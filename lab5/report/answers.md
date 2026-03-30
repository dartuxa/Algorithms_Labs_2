### 1 - What is the purpose of type hints in Python?

The main purpose is to improve code reliability and clarity by allowing static type checking. 
They help developers catch logical errors early (before runtime) and provide better documentation 
for functions and variables.

### 2 - What is the difference between ```Any``` and a generic type ```T```?

```Any``` is a complete opt-out from type checking, allowing a variable to be anything without restrictions. 
A generic type ```T``` (TypeVar) acts as a placeholder that enforces consistency; 
it ensures that if a specific type is provided as an input, the same specific type is maintained for the output .

### 3 - What does ```Callable[[int], int]``` describe?

It describes a function type that accepts exactly one integer as an argument and returns an integer as a result.

### 4 - Why does ```mypy --strict``` require more annotations?

The ```--strict``` mode enforces a disciplined typing policy where every function must have explicit input and output 
annotations, and no "hidden" untyped code is allowed. This eliminates ambiguity and ensures that the entire codebase 
is fully verified by the static analyzer.
