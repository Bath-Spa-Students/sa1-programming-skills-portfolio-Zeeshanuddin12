#This is the code for inputing user's first name.
first_name=str(input("Enter your first name: "))

#This is the code for inputing user's second name.
second_name=str(input("Enter your second name: "))

#This is the code for inputing user's hometown.
home_town=str(input("Enter your hometown: "))

#This is the code for inputing user's age.
while True:
    try:
        user_age=int(input("Enter your age:"))
        break
    except ValueError:
        print("Invalid input for age. Enter the number.")

#This is the code for storing the information in dictionary.
user_information= {
    "First name": first_name,
    "Second name": second_name,
    "Hometown": home_town,
    "Age": user_age
}

#This is the code for printing values
print(f"First Name: {user_information['First name']}\nSecond Name: {user_information['Second name']}\nHometown: {user_information['Hometown']}\nAge: {user_information['Age']}")