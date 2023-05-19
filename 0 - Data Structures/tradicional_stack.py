# Stacks in Python are Implemented using LISTS

# Push - Add item at tpop
stack = []
stack.append(2)
stack.append(4)
stack.append(7)
print(stack)

# Pop - Removes top Item
stack.pop()
print(stack)

# Peek - Look at top Item
top = stack[-1]
print(top)
print(stack)

# IsEmpty 
if len(stack) == 0:
    print("Stack is Empty")
else:
    print("Isn't Empty")

