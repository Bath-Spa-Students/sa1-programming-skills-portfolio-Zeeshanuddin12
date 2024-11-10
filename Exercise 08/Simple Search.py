#create a list of strings with names in it.
Names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Enter the string you want to search for in the string list above.
Search_name = "Sam"

#Look for the name in the above list.
if Search_name in Names :
    print("{Search_name} in present in the list.")
else:
    print("{Search_name}is not present in the list.")