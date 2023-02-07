# In Python, logical operators are used to compare values and make decisions based on the result of the comparison. The following are the logical operators available in Python:

# 1 and: Returns True if both the operands are True, False otherwise.
# 2 or: Returns True if either of the operands is True, False otherwise.
# 3 not: Returns True if the operand is False, False otherwise.

# example1
one = 1
two = 2
sum = one + two
print(one + two == sum)


# example2
a = True
b = True
c = False

if a and b:
    print(a, "and", b, "is", a and b)

if a or b:
    print(a, "or", b, "is", a or b)

# this not printed out since a and c is false and doesn't fulfill the if condition
if a and c:
    print(a, "and", c, "is", a and c)

if a or c:
    print(a, "or", c, "is", a or c)
