# Typecasting, also known as type conversion,
# is the process of converting one data type to another in Python

# In Python, typecasting can be performed using the following functions:

# int(): Converts a number or string to an integer
# float(): Converts a number or string to a floating-point number
# str(): Converts any data type to a string
# bool(): Converts any data type to a Boolean value (True or False)
# list(): Converts a tuple or string to a list
# tuple(): Converts a list or string to a tuple
# set(): Converts a list or tuple to a set
# dict(): Converts a list of tuples to a dictionary

# by default input method accept string value
height = input("please enter your height")

# convert string to float
height = float(height)
print(height, type(height))

# convert float data type into string
height = int(height)
print(height, type(height))
