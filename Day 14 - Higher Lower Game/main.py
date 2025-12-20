import random
from art import *
from game_data import data





def format_data(account):    
    """Takes the account data and returns the printable format."""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(user_guess , a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return user_guess == "a"
    else:
        return user_guess == "b"




print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}.")
    print(vs)
    print(f"Against B : {format_data(account_b)}.")

    guess = input("Who has more follower? 'A' or 'B' : ").lower()

    print("\n" * 30)
    print(logo)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}.")

    else:
        print(f"You're wrong! Your final score is {score}.")
        game_should_continue = False

    



