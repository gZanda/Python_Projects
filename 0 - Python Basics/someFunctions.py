def hello():
    print("Hello!")

def bye():
    print("Bye!")

def add(x,y):
    return x + y

print(__name__) 

# Caso seja input vai ignorar 
if __name__ == "__main__":  # Identificar se esse arquivo é MAIN ou INPUT
    print(add(1,1))
