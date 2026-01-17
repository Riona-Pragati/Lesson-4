# Initialize three numbers
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

print(f"Before swap: a = {a}, b = {b}, c = {c}")

# Swap the numbers
# The variables on the left are assigned the values from the tuple on the right
# The new order for a, b, c will be c, a, b
a, b, c = c, a, b

print(f"After swap: a = {a}, b = {b}, c = {c}")