# Python dictionaries store data as key-value pairs. 
# The key is immutable, while the value can be modified.
# Curly braces `{}` define a dictionary.
# Operators like `in` and `not in` are used to check the presence of keys in the dictionary.
# The `len()` function can be used to find the length of a dictionary, list, or tuple.

# Creating an empty dictionary
data = {}
print(data)

# Checking the type of an empty dictionary
data = {}
print(data, type(data))

# Alternative way to create a dictionary using the `dict` function
data = dict()
print(data, type(data))

# Example of a populated dictionary
info = {'language': 'Python', 'editor': 'VS Code', 'OS': 'Linux'}
print(info)

# Adding elements to a dictionary
profile = {'Username': 'Alex', 'ID': '5678', 'Country': 'Canada'}
print(profile, type(profile))
# Here, 'Username', 'ID', and 'Country' are keys, while their corresponding values are mutable.

# Accessing a value by its key
profile = {'Username': 'Alex', 'ID': '5678', 'Country': 'Canada'}
print(profile["Username"], type(profile))

# Attempting to access a non-existent key raises a KeyError
profile = {'Username': 'Alex', 'ID': '5678', 'Country': 'Canada'}
# print(profile["Age"])  # Uncommenting this line will raise an exception.

# Using the `get()` method to avoid errors when accessing keys
print(profile.get("Age"))

# Using a default value with the `get()` method
print(profile.get("Age", "Unknown"))

# Using the `.items()` method to view key-value pairs as tuples
profile = {'Username': 'Alex', 'ID': '5678', 'Country': 'Canada'}
print(profile.items())

# Viewing all keys in the dictionary
print(profile.keys())

# Using the `del` statement to remove a key-value pair
del profile["ID"]
print(profile.items())

# Using the `pop()` method to remove a specific key-value pair and return its value
removed = profile.pop("Username")
print(removed)
print(profile.keys())
print(profile.values())

# Using `popitem()` to remove the last key-value pair as a tuple
last_item = profile.popitem()
print(last_item)
print(profile.keys())
print(profile.values())

# Iterating through a dictionary using a for loop
settings = {'theme': 'dark', 'notifications': 'on', 'auto-update': 'enabled'}
for key, value in settings.items():
    print(f"{key}: {value}")
