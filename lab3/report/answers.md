### 1. What does it mean that functions in Python are first-class objects?

It means functions are treated like any other variable. They can be assigned to variables , passed as arguments to other functions , and returned as values from other functions.

### 2. What is the difference between a function defined with ```def``` and a ```lambda``` expression?

A def function is a statement used for reusable, multi-line logic with a specific name. A lambda expression is an anonymous, single-line expression used for short, one-time tasks where a formal name isn't necessary.

### 3. What is a closure?

A closure is a nested function that remembers and has access to variables from its enclosing local scope, even after the outer function has finished executing.

### 4. In what situations are closures useful?

Closures are useful for data hiding without using classes , maintaining internal state between function calls like a counter, and creating specialized functions through "function factories".

