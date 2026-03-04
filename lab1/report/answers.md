## Task A: Binding vs Rebinding

Question: Explain why b still refers to the old value after a=7. 
Answer: In Python, names are bindings to objects, not fixed memory locations for values. 
When we set b = a, both names are bound to the same integer object 5. 
Performing a = 7 is a rebinding operation; it changes the name-object relationship for a so that it points to a new object 7. 
This does not affect b, nor does it modify the original object 5, as integer objects themselves are immutable and not modified.

## Task B: Mutation vs Rebinding

Question: Explain why both names see the change and the difference between mutation and rebinding. 
Answer: Both names see the change because a and b are bound to the exact same list object in memory. 
Mutation modifies the internal state of an existing object (like adding an element to a list) without changing which object the name points to. 
In contrast, rebinding assigns a name to a completely different object.

## Task C: Function Arguments

Question: Explain why mutation inside the function affects the caller, while rebinding does not. 
Answer: In Python, argument passing is binding, not copying. 
Function parameters are new local names created when the function is called. 
If the function mutates the object these names point to, the caller sees the change because the underlying object is shared. 
However, if the function rebinds the local parameter to a new object, it only updates that local name's binding and does not affect the caller’s original name.

## Task D: Default Argument Behavior

Question: Explain why the list keeps growing across multiple function calls. 
Answer: This happens because default values are evaluated only once-at the time the function is defined, not every time it is called. 
Because a list is mutable, the same object is reused across all calls to the function. 
Each call that modifies the list is affecting that single, persistent default object.

## Task E: Copy Semantics

Question: Explain the difference between a shallow copy and a deep copy. 
Answer: A shallow copy creates a new collection object, but it fills it with references to the same child objects found in the original. 
If the list contains nested objects (like a list within a list), both the original and the shallow copy will point to the same inner list. 
A deep copy is recursive; it creates a new collection and then proceeds to create new copies of all nested objects found inside, ensuring no shared state between the original and the copy.

## Task F: Reference Counting / GC

Question: Explain why the result for the integer 5 may look unusual compared to larger integers. 
Answer: The high reference count for 5 is due to a CPython optimization where small integers (typically -5 to 256) are pre-allocated and shared globally. 
In newer versions of CPython, these are treated as immortal objects to improve performance. 
This behavior is an implementation detail of CPython and is not guaranteed by the general Python language specification.

