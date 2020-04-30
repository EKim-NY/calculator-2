"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print ("Welcome to the Prefix Calculator!")

# User's input is assigned to input_String as one string,
input_string = input ("Enter your equation:  ")

#Tokenize input. 
tokens = input_string.split(' ')

# Assign more readable names to tokenized items. 
operator = tokens [0]
num1 = tokens [1]
num2 = tokens [2] 

# Insert while loop here. Keep asking for equation until user quits. 

# Call function as long as user does not quit program. 
while operator != 'q': 
    # Call the function determined by 'operator'. 
    if operator == '+': 
        result = add (num1, num2)
    elif operator == '-':
        result = subtract (num1, num2)
    elif operator == '*': 
        result = multiply (num1, num2)
    elif operator == '/': 
        result = divide (num1, num2)
    elif operator == 'square': 
        result = square (num1, num2)
    elif operator == 'cube': 
        result = cube (num1, num2)
    elif operator == 'pow': 
        result = power (num1, num2) 
    elif operator == '%': 
        result = mod (num1, num2)
    else: 
        # Exit WHILE loop if user entered 'q' or something irrelevant. 
        break 
    print (result)
    


