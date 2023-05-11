# Password: 1 Upper, 1 Lower, 1 Number, 1 Special
import random

upper_char = ['A','B','C','D','E']
lower_char = ['a','b','c','d','e']
number = ['1','2','3','4','5']
special = ['@','#','$','%','&']
options = [upper_char,lower_char,number,special]
useds = []
password = ""

while len(options) > 0 :
    selected = random.choice(options)
    useds.append(selected)
    password += random.choice(selected)
    options.remove(selected) # removing one at time

print("Your Password: " + password)

options = useds.copy()  # Restore the optins list
useds.clear()           # Clear the useds list