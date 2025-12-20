import random
from art import logo

def compare(c_choice , u_choice):
    ''' This function compares users choice and computerr choice'''
    global life
    life -= 1
    global game_over
    if c_choice == u_choice:
        print(f"Yay! You nailed it in the correct number was {c_choice}")
        game_over = True
    elif c_choice > u_choice:
        print("Lowww! Guess High...")
    elif u_choice > c_choice:
        print("High! Guess Low...")

def level():
    '''Checks game difficuty level'''
    global life
    choose_level = input("Enter the level you want to play: Easy Medium Hard : ").lower()
    if choose_level == "easy":
        life  = 15
    elif choose_level == "medium":
        life = 10
    elif choose_level == "hard":
        life = 5
    else:
        print("Enter correct value")
        level()

    return life

life = 0
game_over = False


def game():
    print("\n" *50)
    '''Starts the Game'''
    print(logo)
    selected_level = level()
    computer_choice = random.randint(0, 100)
    global life
    global game_over
    while not game_over:
        user_choice = int(input("Enter your guess number : "))
        compare(c_choice=computer_choice , u_choice= user_choice)
        print(f"You have {life} attempt left")

        if life == 0 or game_over == True :
            if input("Do you want to play again? : ") == "y":
                if input("Do you want to play same level again? : ") == "y":
                    life = selected_level
                    game_over = False
                    game()
                else:
                    game_over = False
                    game()
            else:
                game_over =  True
            
game()
