from art import game_logo, vs_logo
from data import data
import random
import os
clear = lambda: os.system('cls')

def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["Name"]
    account_description = account["Description"]
    account_country = account["Country"]
    return(f"{account_name}, a {account_description}, form {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got the guess right"""
    if a_followers > b_followers:
        return guess == "a" 
    else:
        return guess == "b"

# 1. Display art
print(game_logo)
score = 0
game_continuation = True
account_b = random.choice(data)

# 8. Make the game repeatable
while game_continuation:
    # 2. Generate a random account
    # 9. Making account at position B become the next account at positionn A
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    # 3. Format the account data into a printable data
    print(f"Comapare A: {format_data(account_a)}.")
    print(vs_logo)
    print(f"Against B: {format_data(account_b)}.")

    # 4. Ask user for a guess
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()

    # 5. Check if user is correct
    ## Get follower count of each account
    ## use if statement to check if user is correct
    a_follower_count =  account_a["Follower"]
    b_follower_count =  account_b["Follower"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # 10. Clear the screen between rounds
    clear()
    print(game_logo)

    # 6. Give user feedback on their guess
    # 7. Score keeping
    if is_correct:
        score +=1
        print(f"You're right! Current score: {score}")
    else:
        game_continuation = False
        print(f"Sorry, that's wrong. Final score: {score}")










