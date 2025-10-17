# Simple Calculator Program

print("---- Simple Calculator ----")

# Take input from user
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))

# print("Choose operation:")
# print("1. Addition (+)")
# print("2. Subtraction (-)")
# print("3. Multiplication (*)")
# print("4. Division (/)")

# # Take operator input
# op = input("Enter your choice (+, -, *, /): ")

# # Perform operation
# if op == '+' or 1:
#     print("Result:", a + b)
# elif op == '-' or 2:
#     print("Result:", a - b)
# elif op == '*' or 3:
#     print("Result:", a * b)
# elif op == '/' or 4:
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Error: Division by zero not allowed!")
# else:
#     print("Invalid operator! Please choose +, -, *, or /.")


'''
3. Area of a Circle
Input the radius and calculate the area of a circle using πr².
'''

# PI = 22/7
# r = float(input("Enter radius of circle: "))

# AOC = PI*r**2

# print(AOC)

'''
4. Swap Two Numbers Without Using a Third Variable
Use arithmetic operations to swap the values of two numbers.

'''

x = int(input("Enter first: "))
y = int(input("Enter second: "))

x = x + y
y = x - y
x = x - y

print("After swapping = value of x:", x, "value of y:", y)