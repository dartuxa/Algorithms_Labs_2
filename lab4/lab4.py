print("--- Task A - Higher-Order Function ---")
print()

def apply(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

print(apply(lambda x: x + 2, [1, 2, 3])) 

print()
print("--- Task B - map ---")
print()

numbers_b = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, numbers_b))

as_strings = list(map(str, squared))

print("Squares:", squared)
print("Strings squared:", as_strings)

print()
print("--- Task С - filter ---")
print()

numbers_c = [5, 10, 15, 20]

evens = list(filter(lambda x: x % 2 == 0, numbers_c))

greater_than_10 = list(filter(lambda x: x > 10, numbers_c))

print("Evens:", evens)
print("Greater than 10:", greater_than_10)

print()
print("--- Task D - map/filter vs comprehension ---")
print()

data_d = [1, 2, 3, 4, 5, 6]

res_mf = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data_d)))

res_comp = [x**2 for x in data_d if x % 2 == 0]

print("Map/Filter:", res_mf)
print("Comprehension:", res_comp)

print()
print("--- Task E - Simple Decorator ---")
print()

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"call #{wrapper.count}")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@call_counter
def say_hello():
    return "Hello!"

print("test:")
say_hello()
say_hello()

print()
print("--- Task F - Decorator with Arguments ---")
print()

def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{text}: {result}"
        return wrapper
    return decorator

@prefix("INFO")
def get_data():
    return "data"

print(get_data())

print()
print("--- Task G - Caching Decorator ---")
print()

def cache(func):
    memo = {}
    def wrapper(*args):
        if args in memo:
            print("calculating for n =", args[0])
            return memo[args]
        result = func(*args)
        memo[args] = result
        print("copying for n =", args[0])
        return result
    return wrapper

def count_ways(n):
    print("calculating for n =", n)
    if n < 0: return 0
    if n == 0: return 1
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

print()
print("Staircase n(no cache):", count_ways(3))
print()

@cache
def count_ways(n):
    if n < 0: return 0
    if n == 0: return 1
    return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

print()
print("Staircase n(with cache):", count_ways(3))
print()

print("-" * 34)
