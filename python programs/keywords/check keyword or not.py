#check given keyword is a python keyword or not

import keyword
# Get input from the user
word = int
# Check if the word is a Python keyword
if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is not a Python keyword.")
    
