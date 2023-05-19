# Creating a List ------------------------------------------------------------------------
empty = []
numbers = [1,2,3,4]
string = ["abcd","efgh"]
mixed = [1,2,3,"abc"]

# Acessing a List ------------------------------------------------------------------------
print(numbers[0])
print(numbers[-1])  # Do fim pro começo
print(numbers)

# Modifying a List -----------------------------------------------------------------------
numbers[0] = 9      # Basta Sobrescrever
print(numbers)

# Slicing a List -----------------------------------------------------------------------
print(numbers[0:])      # 0 to end
print(numbers[0:2]) 
print(numbers[0::2])    # 0 to end Pulando de 2 em 2

# List Methods() -----------------------------------------------------------------------
numbers.append(99)      # Add no FIM
numbers.insert(0,-2)    # add (Index, Number)
numbers.remove(3)       # Remove an element - da erro se n tiver !!! 
numbers.pop(1)          # Remove and Returns ( index)
numbers.index(99)       # Return the index of the first ocurrence of the number
numbers.count(99)       # Return the number of ocurrences of a number
numbers.sort()          # SORT - Quick
numbers.reverse()       # Reverse
len(numbers)            # Return the LENGTH of the list
print(99 in numbers)    # Return true or false if the elements is IN
print(numbers)

# List concatenation ------------------------------------------------------------------
numbers2 = [50,51,52,53,54]
print(numbers+numbers2)
print(numbers * 3)          # Repete

# List Comprehension ------------------------------------------------------------------
squares = [ x ** 2 for x in numbers]
print(squares)