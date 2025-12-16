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


def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    else:
        return a / b

operation = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division,
}

should_continue = True  
first_number = float(input("Enter the first number: "))

while should_continue:

    operand = input('''
Enter +  ---------------------> Addition
Enter -  ---------------------> Subtraction
Enter *  ---------------------> Multiplication
Enter /  ---------------------> Division
Your choice: ''')
    second_number = float(input("Enter the second number: "))
    print(f"{first_number} {operand} {second_number} = {operation[operand](first_number, second_number)}")

    continue_prompt = input("Enter 'yes' if you want to continue and 'no' to exit : ").lower()
    if continue_prompt == "no":
        should_continue = False
    elif continue_prompt == "yes":
        first_number = operation[operand](first_number, second_number)
    else:
        print("Invalid input. Enter the valid prompt!.")