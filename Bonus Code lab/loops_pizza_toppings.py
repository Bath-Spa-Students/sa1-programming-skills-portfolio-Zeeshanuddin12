
# Prompt user for pizza toppings
while True:
    topping = input("Enter a pizza topping (type 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza!")
