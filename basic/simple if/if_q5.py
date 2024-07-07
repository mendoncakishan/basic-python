# --------------------------------consider the list collection & print the revers of the last value only if its a string

# k=eval(input("Enter a list:"))
# if type([k-1])== str:
#     print("last value is string and revers order is:",k[-1][::-1])

import ast

# Prompt the user to enter a list
k = ast.literal_eval(input("Enter a list: "))

# Check if the last element is a string
if isinstance(k[-1], str):
    # Print the last value and its reverse
    print("Last value is a string and its reverse order is:", k[-1][::-1])
else:
    print("Last value is not a string.")


