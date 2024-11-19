# Python supports both homogeneous and heterogeneous lists.
# Unlike C or Java, Python allows lists to store elements of different data types.

# Homogeneous List Example
subjects = ["Math", "Science", "History"]
print(subjects)

# Heterogeneous List Example
student_info = ["Alice", 101, 3.8]
print(student_info)

# Repetition Operator (*) to repeat list elements
numbers = [1, 2, 3, 4]
repeated_numbers = numbers * 2
print(repeated_numbers)

# Positive Indexing: Access elements using 0-based index
numbers = [10, 20, 30, 40, 50]
print(numbers[2])  # Access the third element (index 2)

# Negative Indexing: Access elements using negative indices, starting from -1
numbers = [10, 20, 30, 40, 50]
print(numbers[-2])  # Access the second-to-last element

# `len()` function returns the number of elements in a list
numbers = [10, 20, 30, 40, 50]
print("Number of elements in the list:", len(numbers))

# Lists are mutable, meaning elements can be changed
numbers = [10, 20, 30, 40, 50]
numbers[0] = 99  # Changing the first element
print(numbers)

# Concatenation: Combine two lists using `+`
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

# List Slicing: Extract a portion of a list
numbers = [5, 10, 15, 20, 25, 30]
sliced_list = numbers[1:4]  # Extract elements from index 1 to 3
print(sliced_list)

# Check if an element exists in a list using `in`
numbers = [1, 2, 3, 4, 5]
if 3 in numbers:
    print("Found")
else:
    print("Not Found")

# Check if an element is not in a list using `not in`
if 7 not in numbers:
    print("7 is not in the list")
else:
    print("7 is in the list")

# Built-in Methods for Lists

# `append()`: Add an element to the end of the list
numbers = [1, 2, 3]
numbers.append(99)
print(numbers)

# `index()`: Find the index of an element
print(numbers.index(99))  # Returns the index of 99

# `sort()`: Sort the list in ascending order
numbers = [5, 2, 8, 3]
numbers.sort()
print(numbers)

# `reverse()`: Reverse the order of elements in the list
numbers.reverse()
print(numbers)

# `remove()`: Remove the first occurrence of a value
numbers.remove(8)
print(numbers)

# `max()` and `min()`: Find the maximum and minimum values in a list
print("Max:", max(numbers))
print("Min:", min(numbers))
