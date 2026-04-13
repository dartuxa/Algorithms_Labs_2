from typing import Protocol, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod



class Serializable(Protocol):
    def serialize(self) -> str: ...

def export(obj: Serializable) -> None:
    print(obj.serialize())



print("--- Task A - Regular class (duck typing) ---")
print()

class StudentRegular:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"StudentRegular (name = {self.name}, group = {self.group}, grade = {self.average_grade})"

student_a = StudentRegular("Roman Malakhov", "KN-124", 98.5)
export(student_a)

print()
print()
print("What do we see?: Object succesfully serialized through the function 'export'.")
print()
print("Why does it work?: Because of 'duck typing', Python does not indicate obvious inheritance. Functions 'export' is sufficient if the object has a serialize() method, as Protocol.")

print()



print("--- Task B - Dataclass implementation ---")
print()

@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentData(name = {self.name}, group = {self.group}, grade = {self.average_grade})"

student_b = StudentData("Vlad Savchenko", "KN-124", 99.9)
export(student_b)

print()
print()
print("What do we see?: The object behaves just like the primary class, but the code looks significantly cleaner (less boilerplate code).")
print()
print("Why does it work?: The @dataclass decorator automatically generates an __init__ method, and our implementation of the serialize() method is completely satisfied with Protocol.")

print()



print("--- Task C - Slots ---")
print()

@dataclass(slots = True)
class StudentSlots:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentSlots(name = {self.name}, group = {self.group}, grade = {self.average_grade})"

student_c = StudentSlots("Sofia Lytvynenko", "KN-124", 100.0)
export(student_c)

print()

try:
    student_c.new_attribute = "This should fail"
except AttributeError as e:
    print(f"Error while adding attribute : {e}")

print()
print()
print("What do we see?: Protocol is still running, but when trying to add a new attribute 'new_attribute' it throws AttributeError.")
print()
print("Why does it work?: The 'slots=True' wiki is used to create a dynamic dictionary '__dict__' for an object. This strictly demarcates the structure of the object with significant fields and saves memory.")


print()



print("--- Task D - ABC version ---")
print()

class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"StudentABC(name = {self.name}, group = {self.group}, grade = {self.average_grade})"

student_d = StudentABC("Glib Gazin", "KN-124", 95.5)
export(student_d)

print()
print()
print("What do we see?: The object successfully operates both with the export() (Protocol) function and as an ABC-based interface.")
print()
print("Why does it work?: The class clearly inherits from SerializableABC and implements the abstract serialize() method. This shows that one and the same class can be satisfied with both structural typing (Protocol) and contract through inheritance (ABC).")



print()