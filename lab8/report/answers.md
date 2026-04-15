**1. How does a for loop work with custom objects?**
A `for` loop works by implicitly calling the `__iter__()` method on the custom object to retrieve an iterator. Then, it repeatedly calls the `__next__()` 
method on that iterator to get the next item until a `StopIteration` exception is raised, which signals the loop to terminate.

**2. What methods are required for iteration?**
To support the iteration protocol, an object must implement the `__iter__()` method, and the iterator object it returns must 
implement both `__iter__()` (returning itself) and `__next__()` methods.

**3. How does the with statement work internally?**
The `with` statement utilizes the context manager protocol. It evaluates the expression, calls the `__enter__()` method on the 
resulting object before the block of code is executed, and guarantees that the `__exit__()` method is called after the block finishes.

**4. When is exit called?**
The `__exit__()` method is called immediately after the code block inside the `with` statement finishes execution. It is called 
regardless of whether the block completed successfully or if an error/exception occurred inside it.

**5. What problem do descriptors solve?**
Descriptors provide a powerful way to manage attribute access across multiple classes without duplicating code. They solve the 
problem of writing repetitive getter and setter logic by encapsulating attribute validation, computation, or access tracking in a single reusable class.

**6. What happens if a descriptor is not used?**
If a descriptor is not used, attribute access is direct and uncontrolled. This means invalid values (such as negative grades or values exceeding 100) 
could be directly assigned to an object's attributes, potentially breaking the internal logic of the program.

**7. Why is direct iteration preferred over index-based loops in Python?**
Direct iteration is considered more "Pythonic" because it is more readable, less prone to "off-by-one" index errors, and works 
universally with many iterable types (like sets, generators, and dictionaries) that do not support index-based access.

### Limitations and Failure Cases
* **What happens if `StopIteration` is not raised?** If the `__next__()` method does not raise `StopIteration`, the `for` 
loop will never know when the collection is exhausted, resulting in an infinite loop.
* **What happens if `__exit__` is missing?** If `__exit__` is missing, attempting to use the object within a `with` statement 
will raise an `AttributeError`, because the context manager protocol is incomplete.
* **What happens if validation is not implemented?** If validation is not implemented, the system will accept any arbitrary or 
corrupted data (e.g., negative integers or strings instead of valid grades), leading to inconsistent object states and unpredictable program behavior downstream.