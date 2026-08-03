#B5. Bitwise Operators
#Operators: & (AND) , | (OR) , ^ (XOR) , ~ (NOT) , << (left shift) , >> (right shift)
#Task B5.1: Take two integers p = 12 and q = 10. Print the result of p & q, p | q, p ^ q, ~p, p << 2, and p
#>> 2. Convert p and q to their binary form using bin() and verify the bitwise results manually
p = 12
q = 10
print(bin(p), bin(q))
print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(p << 2)
print(p >> 2)

#output
#0b1100 0b1010
#8
#14
#6
#-13
#48
#3
