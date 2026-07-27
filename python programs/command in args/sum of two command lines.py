# Program 2: Sum of Two Command Line Arguments
import sys
if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("Sum =", a + b)

#output
# Command: python sum.py 10 20
# Sum = 30
#If incorrect arguments are given:
# Command: python sum.py 10
# Usage: python sum.py <num1> <num2>
