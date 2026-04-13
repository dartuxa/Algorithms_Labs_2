## 1. What is duck typing?

It is a concept where an object's suitability is determined by the presence of certain methods and 
properties rather than its actual type. 
If it "walks and quacks like a duck," Python treats it as one.


Failure case: If a required method is missing, the program will raise an AttributeError at runtime.

### 2. How does Protocol differ from ABC?

Protocol uses structural typing, meaning a class doesn't need to inherit from it to be compatible. 
ABC requires explicit inheritance to satisfy the interface.

### 3. Does Protocol require inheritance? Why or why not?

No, it does not. It works based on the structure of the class. As long as the class implements 
the methods defined in the Protocol, it is considered a valid subtype.

### 4. What problem does ABC solve?

ABC enforces a formal contract between a base class and its subclasses. It ensures that any child 
class provides specific method implementations.
Failure case: ABC prevents the creation of an object if the required abstract methods are not implemented.

### 5. What does @dataclass generate automatically?

It automatically generates special methods like init(), repr(), and eq() based on the defined fields.

### 6. What changes when using slots?

Using slots=True restricts the object structure by preventing the creation of a dynamic dictionary (dict).
Failure case: You cannot add new attributes to the object that were not defined in the class.

### 7. Why does Protocol work with different implementations?

Protocol only cares about the "external" behavior (the presence of the serialize method). 
Whether the internal storage uses regular attributes, dataclasses, or slots, the object 
still provides the required interface.