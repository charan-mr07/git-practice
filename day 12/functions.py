# Basic syntax for functions 
def greet():
    print("Hello, welcome")
greet()    # function call
greet()    # code repeat

# Parameters 
def greet(name):
    print("Hello,", name)
greet("charan")
greet("sai")

# Return value
def add(a, b):
    result = a + b
    return result 
sum_value = add(5, 10)

# 1. Function to add two numbers and return the result
def add_numbers(a, b):
    return a + b

# 2. Function to square a number and return the result
def square(num):
    return num * num

# 3. Function to print a greeting message with a default parameter
def welcome(name="Guest"):
    print(f"Hello, {name}!")

# Call functions to test
print(add_numbers(5, 10))   # Output: 15
print(square(4))            # Output: 16
welcome()                   # Output: Hello, Guest!
welcome("Charan")           # Output: Hello, Charan!


