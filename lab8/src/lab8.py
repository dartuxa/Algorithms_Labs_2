from typing import List, Optional, Type, Any

class GradeDescriptor:
    
    def __init__(self) -> None:
        self._name: str = ''
    
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self._name = '_' + name

    def __get__(self, instance: Any, owner: Type[Any]) -> Any:
        if instance is None:
            return self
        return getattr(instance, self._name)

    def __set__(self, instance: Any, value: int) -> None:
        if not (0 <= value <= 100):
            raise ValueError(f"Grade must be between 0 and 100. Got: {value}")
        setattr(instance, self._name, value)

class Student:
    
    grade = GradeDescriptor()

    def __init__(self, name: str, group: str, grade: int) -> None:
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"Student (name = '{self.name}', group = '{self.group}', grade = {self.grade})"

class StudentIterator:
    
    def __init__(self, students: List[Student]) -> None:
        self._students = students
        self._index = 0

    def __iter__(self) -> 'StudentIterator':
        return self

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        
        student = self._students[self._index]
        self._index += 1
        return student


class StudentCollection:
    
    def __init__(self, students: List[Student]) -> None:
        self.students: List[Student] = students
    
    def __iter__(self) -> StudentIterator:
        return StudentIterator(self.students)
    
    def __enter__(self) -> 'StudentCollection':
        print("[Entering the context]")
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]],
                 exc_val: Optional[BaseException],
                 exc_tb: Optional[Any]) -> None:
        print("[Exiting the context]")


student1 = Student("Glib", "KN-124", 89)
student2 = Student("Vlad", "KN-124", 99)
student3 = Student("Nikita", "KN-123", 90)

my_students = [student1, student2, student3]
collection = StudentCollection(my_students)



print("--- Task A - Iteration ---")
print()

for student in collection:
    print(student)

print()
print("What do we see? All student objects are sequentially displayed from the collection.")
print()
print("Why does it work? The 'for' loop implicitly calls the __iter__() method, which returns a StudentIterator object. "
      "The __next__() method is then called for each step until a StopIteration exception is thrown.")
print()



print("--- Task B - Context Manager ---")
print()

with collection:
    print("Doing some work inside the collection context...")

print()
print("What do we see? The message '[Entering the context]' appears before the code block is executed, "
      "and '[Exiting the context]' appears after.")
print()
print("Why does it work? The 'with' statement calls the __enter__() method before executing the nested code block, "
      "and guarantees to call the __exit__() method after its completion.")
print()



print("--- Task C - Descriptor ---")
print()

try:
    print("Спроба встановити оцінку 120 для студента...")
    student1.grade = 120
except ValueError as e:
    print(f"Validation Error Caught: {e}")

print()
print("What do we see? The attempt to assign an invalid value caused a ValueError, which we caught.")
print()
print("Why does it work? The 'grade' field is managed by the GradeDescriptor. "
      "When trying to change the value (student1.grade = 120), Python intercepts this and calls the __set__ "
      "method of the descriptor, where the validation occurs.")
print()



print("--- Task D - Integration ---")
print()

with StudentCollection(my_students) as integrated_collection:
    for student in integrated_collection:
        print(f"Verified Grade for {student.name}: {student.grade}")

print()
print("What do we see? The message '[Entering the context]' appears before the code block is executed, "
      "and '[Exiting the context]' appears after.")
print()
print("Why does it work? The 'with' statement calls the __enter__() method before executing the nested code block, "
      "and guarantees to call the __exit__() method after its completion.")
print()