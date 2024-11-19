# While loop: Runs as long as the condition is true
value = 1
while value < 10:
    print(value)
    value += 1  # Increment 'value' by 1

# Another While loop example
steps = 1
while steps <= 5:
    print("Step number:", steps)
    steps += 1

# Infinite loop demonstration with break statement
counter = 1
while counter < 6:
    print(counter)
    if counter == 3:  # Exit loop when 'counter' equals 3
        break
    counter += 1  # Increment 'counter'

# For loop: Iterates through elements in a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# For loop with a range: Iterates through numbers from 0 to 14
for number in range(0, 15):
    print(number)

# For loop with custom step size (e.g., 2)
for number in range(0, 15, 2):  # Counts in steps of 2
    print(number, end=",")
print()  # New line after the loop

# User-controlled loop: Print numbers in a user-defined range
max_value = int(input("Enter the upper limit for range: "))
for num in range(0, max_value, 5):  # Increment by 5
    print(num, end=",")
print()

# Sum of user inputs
total = 0
for _ in range(5):
    number = float(input("Enter a number: "))
    total += number  # Add 'number' to 'total'
print("Total sum:", total)

# While loop with sentinel value to stop
total_sum = 0
while True:
    user_input = float(input("Enter a number (-1 to stop): "))
    if user_input == -1:  # Sentinel value to break the loop
        break
    total_sum += user_input
print("Total sum:", total_sum)

# Nested loops: Multiply values from two lists
list_a = [10, 20, 30]
list_b = [1, 2, 3]
for i in list_a:
    for j in list_b:
        print(f"Outer value: {i}, Inner value: {j}")