# Using Wikipedia text we gonna make a list of "readable" words to use in the pass
import random

special = ['@','#','$','%','&']
word_list = []

with open("SampleText/wikipedia_text.txt",'r') as file:
    data = file.readlines()     # Read line by line

    # Divide lines in a List of Words
    for line in data:
        words = line.split()
        
        # Select just the words with = len > 5
        for item in words:
            if len(item) > 6:
                word_list.append(item.capitalize()) # Capitalize the first letter
    
word = random.choice(word_list)     # Choose one Eligible Word
numb = str(random.randint(0,99))    # Random int
symbol = random.choice(special)     # Choose one Symbol

password = word + symbol + numb
print("Your Password: " + password)
