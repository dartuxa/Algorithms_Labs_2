### 1. What is the difference between a list comprehension and a generator expression?

A list comprehension creates the entire list at once and stores it in memory. In contrast, a generator expression creates an iterator object that produces elements one by one only when requested.

### 2. Why are generators considered lazy?

Generators are considered "lazy" because they do not compute their values in advance. Instead, they wait until the program requests the next element, which significantly saves memory and CPU resources.

### 3. What happens when a generator finishes execution?

When a generator exhausts all available values, it raises a StopIteration exception. In for loops, this mechanism is handled automatically, leading to a clean termination of the iteration.
