### 1. What is the difference between a list comprehension and a generator expression?

A list comprehension creates the entire list at once and stores it in memory. In contrast, a generator expression creates an iterator object that produces elements one by one only when requested.

### 2. Why are generators considered lazy?

Generators are considered "lazy" because they do not compute their values in advance. Instead, they wait until the program requests the next element, which significantly saves memory and CPU resources.

### 3. What happens when a generator finishes execution?

When a generator exhausts all available values, it raises a StopIteration exception. In for loops, this mechanism is handled automatically, leading to a clean termination of the iteration.

### Why does Python treat empty containers as False?

Python uses truthiness, where an object's boolean value is determined by its ```__len__``` or ```__bool__``` method. Empty containers return a length of 0, which evaluates to False, allowing for more concise code like ```if not my_list```: instead of checking if the length is zero.

### When should ```is``` be used instead of ```==```?

Use == : To check if two objects have the same value.

Use is : To check if two variables point to the exact same object in memory.

### Why is match convenient for analyzing structured data?

The match-case statement (structural pattern matching) is efficient because it simultaneously:

- Verifies the "shape" of the data .

- Extracts values into variables directly from the structure.

- Replaces complex nested if-else blocks with a more readable, declarative syntax.



