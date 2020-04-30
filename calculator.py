"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print ("Welcome to the Prefix Calculator!")

# User's input is assigned to input_String as one string,
input_string = input (print ("Enter your equation:  "))

# Assign more readable names to tokenized items. 
operator = input_string [0]
num1 = input_string [1]
num2 = input_string [2] 

# Insert while loop here. Keep asking for equation until user quits. 

# Check if user wants to quit program. 
if input_string[0] == 'q': 
    break
else: 
    # Call the function determined by 'operator'. 
    if operator == '+': 
        add (num1, num2)
    elif operator == '-':
        subtract (num1, num2)
    elif operator == '*': 
        multiply (num1, num2)
    elif operator == '/': 
        divide (num1, num2)
    elif operator == 'square': 
        square (num1, num2)
    elif operator == 'cube': 
        cube (num1, num2)
    elif operator == 'pow': 
        power (num1, num2) 
    elif operator == '%': 
        mod (num1, num2)
    else: 
        print ("You did not enter an available operator.")


