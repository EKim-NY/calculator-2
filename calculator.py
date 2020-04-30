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

# Call function as long as user does not quit program. 
while operator != 'q': 
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
        # Exit WHILE loop if user entered 'q' or something irrelevant. 
        break 



