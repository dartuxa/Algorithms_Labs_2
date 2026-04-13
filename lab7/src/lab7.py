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