# A nested loop in Python is a loop that is inside another loop.
# The inner loop runs to completion for each iteration of the outer loop.
# This allows you to perform multiple iterations of a set of instructions
# for each iteration of another loop.

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}, {j}")

# Nested loops can be useful for processing 2-dimensional arrays,
# for example, or for iterating over combinations of elements from multiple lists.
# However, be careful with nested loops, as they can lead to long execution times
# if the number of iterations is too high.
