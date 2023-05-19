# Tuples are Like LISTS, but IMUTABLE

# Creating ------------------------------------------------------------------------
empty_tuple = ()
fruits = ('apple', 'banana', 'cherry')
mixed_tuple = (1, 'hello', True)

# Acessing ------------------------------------------------------------------------
print(fruits[0])

# Operations ------------------------------------------------------------------------
concatenated_tuple = fruits + mixed_tuple
print(concatenated_tuple)

# Unpacking ------------------------------------------------------------------------
a,b,c = fruits
print(a)
print(b)
print(c)

# Methods ------------------------------------------------------------------------
print(fruits.count('apple'))    # Number of Ocurrences
print(fruits.index('banana'))   # index of First Ocurrence

# Use cases:
# A single entity that should remain unchanged
# Tuples can be used to return multiple values from a function