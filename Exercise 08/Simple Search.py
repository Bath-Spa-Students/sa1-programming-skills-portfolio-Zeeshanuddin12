#Initializing the list of names.
list_names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Inputing the search term.
search_term = input("Enter a name to search: ")

#Checking whether the inputed name is in the list and print the result
if search_term in list_names:
    print(f"'{search_term}' was found in the list.")
else:
    print(f"'{search_term}' was not found in the list.")
