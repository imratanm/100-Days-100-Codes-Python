print("Welcome to the Treasure Hunt!")
print("Your mission is to find the hidden treasure.")
print(''' 
  __                                                 ___ ___               __   
_/  |________   ____   ________ _________   ____    /   |   \ __ __  _____/  |_ 
\   __\_  __ \_/ __ \ /  ___/  |  \_  __ \_/ __ \  /    ~    \  |  \/    \   __\'
 |  |  |  | \/\  ___/ \___ \|  |  /|  | \/\  ___/  \    Y    /  |  /   |  \  |  
 |__|  |__|    \___  >____  >____/ |__|    \___  >  \___|_  /|____/|___|  /__|  
                   \/     \/                   \/         \/            \/      
      ''')

print("You are at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice1 = input("> ").lower()
if choice1 == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice2 = input("> ").lower()
    if choice2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors: red, yellow, and blue.")
        print("Which color do you choose?")
        choice3 = input("> ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")   
