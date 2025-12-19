import random
from art import logo

def deal_cards():
    '''Deals card from deck'''
    cards = [11 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''Calculate the score'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score, c_score):
    '''
    Compares Users and Computers score
    
    :param u_score: Users Score
    :param c_score: Computer Score
    '''
    if u_score == c_score:
        print("Draw")
    elif c_score == 0:
        print("Loose, Opponenet has BlackJack!")
    elif u_score == 0:
        print("You win a BlackJack")
    elif u_score > 21:
        print("You went over you loose")
    elif c_score > 21:
        print("Opponenet went over. You Win!")
    elif u_score > c_score:
        print("You Win!")
    else:
        print("You Loose")

def play_game():
    print(logo)
    computer_cards = []
    computer_score = -1
    user_cards = []
    user_score = -1
    is_game_over = False

    for _ in range(2):
        computer_cards.append(deal_cards())
        user_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are : {user_cards} and your score is : {user_score}")
        print(f"Computer first card : {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else: 
            user_should_deal = input("Type 'y' to dealt a card or 'n' to pass. : " )
            if user_should_deal == "y":
                user_cards.append(deal_cards())

            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}, final score is {user_score}")
    print(f"Computer final hand is {computer_cards} and final score is {computer_score}")
    compare_score(u_score=user_score , c_score=computer_score)

while input("Do you want to play again? Type y or n : ") == "y":
    print("\n" * 50)
    play_game()

