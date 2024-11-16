def check_even_odd(number):
    # Determine if the number is even or odd
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

def main():
    # Prompt the user to enter a number
    number = int(input("Enter a number: "))
    # Call the function to check if the number is even or odd
    result = check_even_odd(number)
    # Display the result to the user
    print(result)

if __name__ == "__main__":
    # Execute the main function
    main()