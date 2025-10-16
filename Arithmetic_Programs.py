# Simple Calculator Program

print("---- Simple Calculator ----")

# Take input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Take operator input
op = input("Enter your choice (+, -, *, /): ")

# Perform operation
if op == '+' or 1:
    print("Result:", a + b)
elif op == '-' or 2:
    print("Result:", a - b)
elif op == '*' or 3:
    print("Result:", a * b)
elif op == '/' or 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Error: Division by zero not allowed!")
else:
    print("Invalid operator! Please choose +, -, *, or /.")
