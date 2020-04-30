"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print ("Welcome to the Prefix Calculator!")

# User's input is assigned to input_String as one string,
input_string = input (print ("Enter operator followed by two numbers:  "))

# Assign more readable names to tokenized items. 
operator = input_string [0]
num1 = input_string [1]
num2 = input_string [2] 

# Check if user wants to quit program. 
if input_string[0] == 'q': 
    break
else: 
    # Look for the right function. 
    if 

