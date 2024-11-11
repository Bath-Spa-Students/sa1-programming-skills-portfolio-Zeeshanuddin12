# This is the code for defining the days in each month (default for non-leap years)
days_of_month = { 1: 30, 2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31 }

# This is the code for function to get the number of days in a specific month
try:
    # This is the code for asking the user to input the month number
    month_nane = int(input("Enter the month number (1-12): "))
    
    # This is the code validating the month number
    if month_nane < 1 or month_nane > 12:
        print("Invalid month number. Please enter a number between 1 and 12.")
        exit()
    # This is the code for checking whether the month is February and handle leap year
    if month_nane == 2:
        # This is the code for asking whether it's a leap year
        leapyear = input("Is it a leap year? (yes or no): ").strip().lower()
        if leapyear == "yes":
            print("February has 29 days in a leap year.")
        else:
            print("February has 28 days in a non-leap year.")
    else:
        # This is the code for outputing the number of days for the selected month
        print(f"The month {month_nane} has {days_of_month[month_nane]} days.")

except ValueError:
    print("Invalid input. Please enter a number.")