# Input two numbers as strings
n1 = input("Enter the first number: ")#Enter the first number: 10
n2 = input("Enter the second number: ")#Enter the second number: 5

# Convert strings to float
n1 = float(n1)
n2 = float(n2)

# Perform arithmetic operations
print("Sum =", n1 + n2)#Sum = 15.0
print("Difference =", n1 - n2)#Difference = 5.0
print("Product =", n1 * n2)#Product = 50.0
# Check for division by zero
if n2 != 0:
    print("Quotient =", n1 / n2)
else:
    print("Quotient = Cannot divide by zero")#Quotient = 2.0
