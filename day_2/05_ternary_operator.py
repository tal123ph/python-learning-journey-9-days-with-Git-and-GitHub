# Program using Ternary Operator (Conditional Expression)
# Syntax: value_if_true if condition else value_if_false

x = 15
y = 20

# Classic way
# if x > y:
#     max_val = x
# else:
#     max_val = y

# Ternary way
max_val = x if x > y else y

print(f"The maximum value between {x} and {y} is {max_val}.")

# Another example: Check even/odd in one line
status = "Even" if x % 2 == 0 else "Odd"
print(f"{x} is {status}.")
