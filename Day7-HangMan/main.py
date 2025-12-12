import random


print('''
  _    _                           __  __                 
 | |  | |                         |  \/  |                
 | |__| | __ _ _ __   __ _        | \  / | __ _ _ __      
 |  __  |/ _` | '_ \ / _` |       | |\/| |/ _` | '_ \     
 | |  | | (_| | | | | (_| |       | |  | | (_| | | | |    
 |_|  |_|\__,_|_| |_|\__, |       |_|  |_|\__,_|_| |_|    
                      __/ |                               
  ______ ______ _____|___/___ ______ ______ ______ ______ 
 |______|______|______|______|______|______|______|______|                                                

      ''')

list_1 = ["apple", "banana", "watermelon"]
computer = random.choice(list_1)
placeholder = " "

for word in computer:
    placeholder += "_"
print(f"You have to guess :{placeholder}" )

set_for_life = set(computer)
life = len(set_for_life)

life = (len(set_for_life))+1
game_over = False

correct_letters = []
while not game_over:
    display = " "
    user_letter = input("Enter a letter to guess: ").lower()
    if user_letter in correct_letters:
        print("This letter you have guessed already!")
    else: 
        for letter in computer:
            if letter == user_letter:
                correct_letters.append(letter)
                display += letter
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        life -= 1
        print(f"You have {life} chances left")
        print(f" You have to guess : {display}" )


        if "_" not in display:
            game_over = True
            print("Yayyyy.. You Won!")
        elif life == 0:
            game_over = True
            print("Oops.. You Lost!")
