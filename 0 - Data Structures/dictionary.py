# Creating a Dictionary ------------------------------------------------------------------
empty = {}  
person = {'name': 'John', 'age': 30, 'city': 'New York'}  # Yes, can be mixed

# Acessiing ------------------------------------------------------------------------
print(person['age'])
print(person.get('age'))
print(person)

# Modifying ------------------------------------------------------------------------
person['age'] = 69  # Yes, apenas sobrescreve
print(person)

# Adding and Removing ----------------------------------------------------------------
person['sex'] = "male"      # Add a new key
del person['age']           # Delete a key
person.pop('city')          # Removes the key and returns the value
print(person)

# Methods ---------------------------------------------------------------------------
print(person.keys())        # Return a lists of the keys
print(person.values())      # List of values
print(person.items())       # Returns Key and Values as a list of Tuples
print(len(person))          # Length 

# Existence ---------------------------------------------------------------------------
print('name' in person)
print('sons' in person)

# Comprehension -----------------------------------------------------------------------
keys2 = { x: x * 2 for x in person}
print(keys2)