print("\nTask A - Binding vs Rebinding \n")
a = -6
b = 3

print (f"before rebind, a = {a}")
print (f"before rebind, b = {b}")
print (f"before rebind, a(id) = {id(a)}")
print (f"before rebind, b(id) = {id(b)}\n")

a = 5

print (f"after rebind, a = {a}")
print (f"after rebind, b = {b}")
print (f"after rebind, a(id) = {id(a)}")
print (f"after rebind, b(id) = {id(b)}")

print ("\n***********************************")

print("\nTask B - Mutation vs Rebinding \n")

a = [1, 3, 5]
b = a

print (f"before rebind, a = {a}")
print (f"before rebind, b = {b}")
print (f"before rebind, a(id) = {id(a)}")
print (f"before rebind, b(id) = {id(b)}\n")

b.append(7)

print (f"after rebind, a = {a}")
print (f"after rebind, b = {b}")
print (f"after rebind, a(id) = {id(a)}")
print (f"after rebind, b(id) = {id(b)}\n")

if id(a) == id(b):
    print("id(a) == id(b)")
else :
    print("ploxo delo")

print ("\n***********************************")

print("\nTask C - Function arguments are new bindings")

a = []

print(f"\n'a' at the start = {a}\n")

def mutate_list(lst):
    lst.append(1)

def rebind_list(lst):
    lst = [9, 9, 9]

mutate_list(a)

print(f"'a' after mutation = {a}\n")

rebind_list(a)

print(f"'a' after rebinding = {a}\n")

print ("\n***********************************")

print("\nTask D - Default argument trap")

def f(a = []):
    a.append(1)
    return a

print(f"\nfirst time calling function {f()}")
print(f"\nsecond time calling function {f()}\n")

print ("***********************************")

print("\nTask E - Copy Semantics\n")
import copy

a = [[1, 2]]
b = a.copy()
c = copy.deepcopy(a)

print(f"a before start = {a}")
print(f"b before start = {b}")
print(f"c before start = {c}")

b[0].append([7])

print(f"\na after start = {a}")
print(f"b after start = {b}")
print(f"c after start = {c}")

print ("\n***********************************")

print("\nTask F - Reference counting\n")
import sys

a = []
print(f"a = {a}")
print(f"initial reference count for a: {sys.getrefcount(a)}")

b = a
print(f"\nb is a copy of a, b = {b}")
print(f"initial reference count for b: {sys.getrefcount(b)}")

a = 5
print(f"\nrefcount for 5: {sys.getrefcount(a)}")

b = 123456
print(f"refcount for 123456: {sys.getrefcount(a)}")

print ("\n***********************************")