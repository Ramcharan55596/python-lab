#A2.1:Write a program that:
#1.Stores your first name and last name in two separate string variables
first = "veluchuri"
last = "charan"
#2.Concatenates them into a full name with a space in between.
full_name = first + " " + last
#3.Prints the full name in UPPERCASE, lowercase, and Title Case.
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
#4.Prints the length of the full name.
print(len(full_name))
#5.Prints the first character and the last character of the full name.
print(full_name[0], full_name[-1])

#output
#veluchuri charan
#veluchuri charan
#veluchuri charan
#19
#y h

#Task A2.2: Use string slicing to extract and print only your first name from the full name string 
full_name = "veluchuri charan"

first_name = full_name[:full_name.index(" ")]
print(first_name)

#output
#veluchuri
