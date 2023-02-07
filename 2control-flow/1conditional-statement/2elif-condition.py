# The elif statement in Python is used in conjunction with the if statement
# to provide additional conditions.
# The elif statement is used to check multiple conditions and execute
# the corresponding code block if the condition is True.

# examples

x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
else:
    print("x is positive")


bill = 120
discount = 30
if bill > 100:
    print("I don't have enough money to buy I need ", bill-100, "extra money")


bill = bill - discount
if bill > 100:
    print("I don't have enough money to buy I need ", bill-100, "extra money")
elif bill < 100:
    print("I have enough money and ", 100-bill, "extra")
