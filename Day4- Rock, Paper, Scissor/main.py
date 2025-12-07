print(''' 
      __________               __         __________                                 _________      .__                           
      \______   \ ____   ____ |  | __     \______   \_____  ______   ___________    /   _____/ ____ |__| ______ _________________ 
      |       _//  _ \_/ ___\|  |/ /      |     ___/\__  \ \____ \_/ __ \_  __ \   \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \.
      |    |   (  <_> )  \___|    <       |    |     / __ \|  |_> >  ___/|  | \/   /        \  \___|  |\___ \ \___ (  <_> )  | \/
      |____|_  /\____/ \___  >__|_ \ /\   |____|    (____  /   __/ \___  >__| /\  /_______  /\___  >__/____  >____  >____/|__|   
             \/            \/     \/ )/                  \/|__|        \/     )/          \/     \/        \/     \/             
      ''')


import random
print("Welcome to Rock, Paper, Scissors!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_art = [rock, paper, scissors]

choice = input("Enter 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\nYour choice: ").lower()
computer_choice = random.choice(['rock', 'paper', 'scissors'])
print(f"You chose: {choice}")
print(choice_art[['rock', 'paper', 'scissors'].index(choice)])

print(f"Computer chose: {computer_choice}")
if computer_choice == 'rock':
    print(choice_art[0])
elif computer_choice == 'paper':
    print(choice_art[1])
elif computer_choice == 'scissors':
    print(choice_art[2])


if choice == 'exit':
    print("Thanks for playing!")
elif choice in ['rock', 'paper', 'scissors']:
    if choice == computer_choice:
        print("It's a tie!")
    elif (choice == 'rock' and computer_choice == 'scissors') or \
         (choice == 'paper' and computer_choice == 'rock') or \
         (choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")