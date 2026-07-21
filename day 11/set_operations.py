#1. Set Operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

#1.1 Union (All unique elements)
print(f"Union: {set_a | set_b}") 

#1.2 Intersection (Common elements)
print(f"Intersection: {set_a & set_b}")

#1.3 Difference (In A but not in B)
print(f"Difference: {set_a - set_b}")

#1.4 Symmetric Difference (In A or B, but not both)
print(f"Symmetric Difference: {set_a ^ set_b}")

#2. Set Method
fruits = {"apple", "banana", "cherry"}
print("Original set:", fruits)

# add() - add single element
fruits.add("orange")
print("After add('orange'):", fruits)

# update() - add multiple elements
fruits.update(["mango", "grape"])
print("After update():", fruits)

# remove() - removes element (error if not found)
fruits.remove("banana")
print("After remove('banana'):", fruits)

# discard() - removes element (no error if not found)
fruits.discard("pineapple")  # no error
print("After discard('pineapple'):", fruits)

# pop() - removes random element
popped = fruits.pop()
print(f"Popped element: {popped}")
print("After pop():", fruits)

print("-" * 40) 

#3. Subset, Superset, Disjoint 
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}

print("Is x subset of y?", x.issubset(y))       # True
print("Is y superset of x?", y.issuperset(x))   # True
print("Are x and y disjoint?", x.isdisjoint(y)) # False

print("-" * 40)

#4. Real-World Example - Common friends
charan_friends = {"Ravi", "Kiran", "Anu", "Sai"}
rahul_friends = {"Sai", "Anu", "Vikas", "Meena"}

common = charan_friends & rahul_friends
all_friends = charan_friends | rahul_friends
only_charan = charan_friends - rahul_friends

print("Common friends:", common)
print("All friends combined:", all_friends)
print("Only Charan's friends:", only_charan)

