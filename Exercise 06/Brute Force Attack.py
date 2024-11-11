#This is the code for defining the correct password.
password=12345

#This is the code for setting the maximum number of attempts.
maximum_attempts=5

#This is the code for initializing the attempt counter to 0.
attempts_counter=0

#This is the code for starting the loop to ask for the password.
while attempts_counter<maximum_attempts:
    enter_password=(int(input("Enter the password:"))) 
    #This is the code for checking whether the entered password is correct.
    if enter_password==password:
        print("Access Granted")
        break

    else:
        attempts_counter += 1 

    #This is the code for calculating remaining attempts.
    attempts_remaining=maximum_attempts-attempts_counter

    #This is the code for checking feedback on remaining attempts.
    if attempts_remaining>0:
        print(f"Incorrect password. You have {attempts_remaining} attempts left")
    else:
        print("Maximum attempts reached. The authorities have been alerted.")