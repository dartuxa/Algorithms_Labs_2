from typing import List, Optional, Callable, TypeVar

print("--- Task A - Basic Type Hints ---")
print()

def add(a: int, b: int) -> int:
    return a + b

def square_list(data: List[int]) -> List[int]:
    return [x * x for x in data]

print(f"Add 5 + 3: {add(5, 3)}")
print(f"Square list [1, 2, 3]: {square_list([1, 2, 3])}")

print()
print("--- Task B - Typed Collections ---")
print()

def filter_even(data: List[int]) -> List[int]:
    return [x for x in data if x % 2 == 0]

nums_b = [1, 2, 3, 4, 5, 6]

print(f"Filter even from {nums_b}: {filter_even(nums_b)}")

print()
print("--- Task C - Optional ---")
print()

def find(data: List[int], x: int) -> Optional[int]:
    return x if x in data else None

nums_c = [1, 5, 2, 8, 3, 10]

print(f"Find 10 in {nums_c}: {find(nums_c, 10)}")
print(f"Find 4 in {nums_c}: {find(nums_c, 4)}")

print()
print("--- Task D - Function Type ---")
print()

def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

print(f"Apply lambda (x + 10) to 5: {apply(lambda x: x + 10, 5)}")
print(f"Apply lambda (x * 2) to 5: {apply(lambda x: x * 2, 5)}")

print()
print("--- Task E - Generics ---")
print()

E = TypeVar('E')

def first(items: List[E]) -> E:
    return items[0]

print(f"First in int list [10, 20]: {first([10, 20])}")
print(f"First in str list ['apple', 'orange']: {first(['apple', 'orange'])}")

print()
print("--- Task F - Function Returning Function ---")
print()

def make_multiplier(k: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * k
    return multiplier

double = make_multiplier(2)
print(f"Double of 15: {double(15)}")

print()
print("--- Task G - Pipeline ---")
print()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

pipeline_result = sum(x**2 for x in numbers if x % 2 == 0)

print(f"Pipeline result (sum of squares of even numbers from {numbers}):")
print(f"Result: {pipeline_result}")
print()