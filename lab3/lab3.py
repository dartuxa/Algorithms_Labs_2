print("--- Task A - Functions as Objects --- \n")

def apply_twice(func, x):
    return func(func(x))

rlambda = apply_twice(lambda x: x + 1, 3)
print(f"lambda (x + 1): {rlambda}")

rabs = apply_twice(abs, -10)
print(f"abs: {rabs}")

def square(n):
    return n * n

rsquare = apply_twice(square, 2)
print(f"(x^2): {rsquare}")

def add_exclamation(text):
    return text + "!"

rstrings = apply_twice(add_exclamation, "hi")
print(f"punctuation: {rstrings}")
print()

print("--- Task B - Sorting with Lambda --- \n")

people = [
    ("Alice", 25),
    ("Bob", 20),
    ("Carol", 30),
    ("Dave", 22)
]

byname = sorted(people, key=lambda x: x[0])
byage = sorted(people, key=lambda x: x[1])

print("sorted by age:")
print(byage)

print("sorted by name:")
print(byname)
print()

print("--- Task C - Function Factory --- \n")

def make_multiplier(k):
    def multiplier(x):
        return x * k
    return multiplier

times3 = make_multiplier(3)
print(f"times3(10) -> {times3(10)}")

times5 = make_multiplier(5)
print(f"times5(10) -> {times5(10)}")

times2 = make_multiplier(2)
print(f"times2(7) -> {times2(7)}")
print()

print("--- Task D - Closure Counter --- \n")

def counter():
    count = 0
    
    def increment():
        nonlocal count
        count += 1
        return count
    
    return increment

c = counter()

print(f"first time:  c() -> {c()}")
print(f"second time:  c() -> {c()}")
print(f"third time:  c() -> {c()}")
print()

print("--- Task E - Lambda vs def  --- \n")

def square_def(n):
    return n * n

square_lambda = lambda n: n * n

test_numbers = [5, -3, 0, 10]

print(f"{'number':<7} | {'def':<7} | {'lambda':<7} | {'match?':<10}")
print("-" * 38)

for num in test_numbers:
    res_def = square_def(num)
    res_lambda = square_lambda(num)
    match = (res_def == res_lambda)
    
    print(f"{num:<7} | {res_def:<7} | {res_lambda:<7} | {str(match):<10}")
print()

print("--- Task F - Functional Composition --- \n")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

pipeline_result = sum((lambda x: x**2)(n) for n in numbers if (lambda x: x % 2 == 0)(n))

print(f"original: {numbers}")
print()
print(f"result: {pipeline_result}")
print()

print("-" * 39)
