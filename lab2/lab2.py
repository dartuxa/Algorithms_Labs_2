print("... Task A: Truthiness ...")

values = [0, 1, [], [1], "hello", None]
for val in values:
    print(f"value: {repr(val)} -> {bool(val)} ")
print()



print("... Task B: Identity vs Equality ...")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"Equal values but different objects: a == b -> {list1 == list2}, a is b -> {list1 is list2}")

list3 = list1
print(f"Identical objects: a == b -> {list1 == list3}, a is b -> {list1 is list3}")

x = 100
y = 100
print(f"Behaviour with immutable values: x == y -> {x == y}, x is y -> {x is y} \n")



print("... Task C: Control Flow ...")

def describe_number(x):
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    elif 0 < x < 10:
        return "small positive"
    else:
        return "large positive"

test_nums = [-5, 0, 5, 15]
for n in test_nums:
    print(f"{n} -> {describe_number(n)} ")
print()



print("... Task D: Pattern Matching ...")

def process_event(event):
    match event:
        case ("click", x, y):
            print(f"click at {x} {y}")
        case ("keypress", key):
            print(f"key pressed: {key}")
        case ("quit",):
            print("quit event")

events = [("click", 10, 20), ("keypress", "A"), ("quit",)]
for e in events:
    process_event(e)
print()


print("... Task E: Comprehensions ...")

squares = [x**2 for x in range(1, 21)]
print(f"Squares 1-20: {squares}")

even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(f"Even squares: {even_squares}")

square_dict = {x: x**2 for x in range(1, 11)}
print(f"Dictionary: {square_dict}\n")



print("... Task F: Generators ...")

def even_numbers(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

print("Generator output:")
for num in even_numbers(8):
    print(num)
print()



print("Additional requirement")
sum_val = sum(x**2 for x in range(1000000) if x % 2 == 0)
print(f"sum of even squares < 1000000: {sum_val}")