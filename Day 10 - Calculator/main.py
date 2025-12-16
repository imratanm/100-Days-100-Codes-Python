print('''
_________            .__                     .__               __                         
\_   ___ \  _____    |  |     ____    __ __  |  |   _____    _/  |_    ____   _______     
/    \  \/  \__  \   |  |   _/ ___\  |  |  \ |  |   \__  \   \   __\  /  _ \  \_  __ \    
\     \____  / __ \_ |  |__ \  \___  |  |  / |  |__  / __ \_  |  |   (  <_> )  |  | \/    
 \______  / (____  / |____/  \___  > |____/  |____/ (____  /  |__|    \____/   |__|       
        \/       \/              \/                      \/                                                                                                                                                                                                              
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______ 
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/      
    ''')

def calculation(first_number , operation):
    second_number = float(input("Enter second number : "))
    result = 0
    if operation == "+":
        result += first_number + second_number
    elif operation == "-":
        result += first_number - second_number
    elif operation == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero!")
        else:
            result += first_number / second_number
    elif operation == "*":
        result += first_number * second_number
    else: 
        print("Please give valid input!")
        result = first_number

    return result
        
should_continue = True
user_first_number = float(input("Enter the first number : "))

while should_continue:
    
    operand = input('''
Enter + ------------------> Addition
Enter - ------------------> Substraction
Enter / ------------------> Divition
Enter * ------------------> Multiplication
Enter your input : ''').lower()
    calculation_result = calculation(first_number=user_first_number, operation=operand)
    print(f"Here is your result : {calculation_result}")

    continue_propmpt = input("Do you want to continue with the current result? Type yes to continue no to exit : ").lower()
    if continue_propmpt == "no":
        should_continue = False
    elif continue_propmpt == "yes":
        should_continue = True
        first_number = calculation_result
    else: 
        print("Please enter valid prompt")