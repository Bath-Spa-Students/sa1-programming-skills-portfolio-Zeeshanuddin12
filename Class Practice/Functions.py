# Functions are blocks of reusable code in Python. 
# Functions can be categorized as:
# 1. Void functions: Perform a task and do not return a value.
# 2. Value-returning functions: Perform operations and return a value.

# Function names should describe their purpose (e.g., `calculate_area`, `generate_report`).
# Functions are created using the `def` keyword.
# Proper indentation is required for the function body.

# Example of a void function
def greet():
    print("Welcome to the Python class!")

# Calling the void function
greet()

# Example of a local variable
def greet():
    message = "Welcome to the Python class!"  # This variable is local to the function.
    print(message)

greet()

# Trying to access a local variable outside its function raises an error
# Uncommenting the line below will result in a NameError:
# print(message)

# Example of functions with the same local variable name but no conflict
def func1():
    data = "Function 1 data"
    print(data)

def func2():
    data = "Function 2 data"
    print(data)

func1()
func2()

# Passing an argument to a function
def greet_user(name):  # The parameter `name` will hold the passed argument.
    print(f"Hello, {name}!")

greet_user("Alice")

# Example: Function to double a value
def main():
    num = 10
    double_value(num)

def double_value(x):
    print(x * 2)

main()

# Example: Passing multiple arguments
def show_details(name, age):
    print(f"Name: {name}, Age: {age}")

show_details("John", 30)

# For additional details, refer to:
# https://www.w3schools.com/python/python_functions.asp
