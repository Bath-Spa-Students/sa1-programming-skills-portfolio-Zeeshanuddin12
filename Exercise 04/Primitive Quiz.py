# Basic requirements.
#Asking the user to input the answer.
answer = input("What is the capital of France? ").strip()
#For checking the output.
if answer.lower() == "paris":
    print("Correct! The answer is Paris.")
else:
    print("Incorrect. The correct answer is Paris.")

# Advanced requirements.
#Quiz.
questions = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Denmark": "Copenhagen"
}
#For counting score.    
score = 0
#For asking questions and checking the output.  
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip()
    if answer.lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {capital}.")
    
    print(f"\nYour final score: {score}/{len(questions)}")