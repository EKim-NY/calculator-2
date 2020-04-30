"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

print ("Welcome to the Prefix Calculator!")

# User's input is assigned to input_String as one string,
input_string = input (print ("Enter operator followed by two numbers:  "))

# Check if user wants to quit program. 
if input_string[0] == 'q': 
    break
else: 
    #

