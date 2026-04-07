### 1. What is stored in ```obj.__dict__```?

It is a dictionary that stores all of an object's writable attributes. 
Each key is the attribute name, and the value is the current data assigned to that attribute .

### 2. What is the difference between a class and an object?

- Class: A blueprint or template that defines the structure and behavior (methods and attributes).

- Object: A specific instance of a class created from that blueprint, containing its own unique data.

### 3. What does ```__init__``` do?

The ```__init__``` method is a constructor used to initialize a new object's state.
It sets the initial values for the object's attributes when the class is instantiated.

### 4. Who calls ```__str__```, and when?

The ```__str__``` method is called by the built-in ```print()``` and ```str()``` functions. 
It is triggered whenever a "user-friendly" or readable string representation of the object is needed.

### 5. What is the difference between ```==``` and ```is```?

- ```==```: Checks for equality of value by calling the ```__eq__``` method.

- ```is```: Checks for identity, determining if two variables point to the exact same memory location (the same object).

### 6. Why do we use ```other: object``` in ```__eq__``` and ```__lt__```?

Using ```object``` ensures type safety and compliance with strict mypy requirements. 
Since Python allows comparing an object with any other type (like a string or integer), 
we must accept a general ```object``` and then safely verify its type within the method using ```isinstance()```.
