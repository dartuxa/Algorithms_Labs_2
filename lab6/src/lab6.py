class Student:

    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.avg_grade = average_grade

    def __str__(self) -> str:
        return f"Student: {self.name} (group {self.group}, grade = {self.avg_grade})"

    def __repr__(self) -> str:
        return f"Student(name = '{self.name}', group = '{self.group}', average_grade = {self.avg_grade})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return False
        return (self.name == other.name and 
                self.group == other.group and 
                self.avg_grade == other.avg_grade)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Student):
            return NotImplemented
        return self.avg_grade < other.avg_grade


print("--- Task A - Define the Student class ---")
print()

stud1 = Student("Vlad", "KH-124", 90.5)

print("Name:", stud1.name)
print("Group:", stud1.group)
print("Average grade:", stud1.avg_grade)

print()
print("--- Task B - Inspect internal structure ---")
print()

print("Original stud1 __dict__:", stud1.__dict__)

stud1.__dict__["avg_grade"] = 95.0

print("Modified stud1 __dict__:", stud1.__dict__)
print("Updated average_grade:", stud1.avg_grade)

print()
print("--- Task C - Implement __str__ ---")
print()

print(stud1)

print()
print("--- Task D - Implement __repr__ ---")
print()

print(repr(stud1))

print()
print("--- Task E - Implement equality (__eq__) ---")
print()

stud2 = Student("Glib", "KH-124", 100.0)
stud3 = Student("Vanya", "KH-1624", 96.0)

print(f"stud1 - {stud1}")
print(f"stud2 - {stud2}")
print(f"stud3 - {stud3}")
print()

print("Result of stud1 == stud2:", stud1 == stud2)
print("Result of stud1 == stud3:", stud1 == stud3)
print("Result of stud1 == 100:", stud1 == 10)

print()
print("--- Task F - Implement ordering (__lt__) ---")
print()

try:
    print("stud1 < stud2:", stud1 < stud2)
    print("stud2 < stud1:", stud2 < stud1)
    print()

    print("try: stud1 < 5")
    print(stud1 < 5)
except TypeError as e:
    print("Error:", e)

print()
print("--- Task G - Sorting ---")
print()

students = [
    Student("Roman", "KH-124", 92.6),
    Student("Nikita", "KH-123", 96.0),
    Student("Kiril", "KH-125", 60.0),
]

print("Before sorting:")
for s in students:
    print(s)
print()

students.sort()

print("After sorting:")
for s in students:
    print(s)