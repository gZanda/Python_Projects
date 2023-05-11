import os   # Pra brincar com files
import someFunctions as func   # Para acessar as funções do outro arquivo
# or "from someFunctions import *" to get ALL and acess without using the variable
from abc import ABC, abstractclassmethod

# Variable and Casting ( Variável sem escopo = GLOBAL) 
print( "\nVarible Demonstration: " )

a = 1
global glob
glob = 78 
print (a, " is a number")   # Concatenar ( + ou , )

# User input ( Com ou sem tipo ) ----------------------------------------------------------
print( "\nInput Demonstration: " )

userName = input("What's your name ? ")
userHeight = float(input("What's your height ? "))  
print("Your name is " + userName)

# IF statement --------------------------------------------------------------------
print( "\nIF Demonstration: " )

if userHeight >5:
    print( "You are +5ft tall" )
elif userHeight == 2:
    print( "You are EXACTLY 2ft tall")
else: 
    print( "You are NOT +5ft tall")

# While --------------------------------------------------------------------
print( "\nWhile Demonstration: " )

resp = False
while resp != "yes":
    print( "Are u sure ?")
    resp = input()

# For ( Starts in 0 ) - É UM FOR EACH ------------------------------------------------------------
print( "\nFor Demonstration: " )

for i in range(1,11):   # Start, End, Gap
    print( i , end=" ")

print( " " )

for i in userName:
    print( i , end=" ")

# BREAK & CONTINUE --------------------------------------------------------------------
print( "\nBreak & Continue Demonstration: " )

for i in userName:
    if i == "a":
        print( "Parei")
        break
    else:
        print ( i , end=" ")

for i in userName:
    if i == "a":
        print( "Skippei")
        continue
    else:
        print ( i , end=" ")

# String Manipulation --------------------------------------------------------------------
print( "\nString Manipulation Demonstration: " )
str1 = "Pirarucu"
str2 = "Pancreas Dinamico "

print(str1[1])
print(str2[0:3])
print(str2.lstrip())    # Remove whitespace in the left
print(str1.capitalize())
print(str1.islower())
print(str2.replace("Dinamico","Acabado"))
print(str1.split(","))  # Split vectors, lists, etc
print(str2 * 3)

# str.FORMAT --------------------------------------------------------------------
print( "\nFORMAT Demonstration: " )

print("I love pizza")
print("{} love {}".format("I","Pizza"))
print("{Who} love {What}".format(Who="I", What="Pizza"))
who = "I"
what = "Pizza"
print("{} love {}".format(who,what))

# List ( Array ) --------------------------------------------------------------------

print( "\nList Demonstration: " )

food = ["pizza", "hot dog", "cucumber"]
food[1] = "Shrimp"  # Overwrite
print( "Food[1] = " + food[1])

food.insert(0,"666")  # Insert
food.remove("cucumber") # Remove

# food.clear()

print(food)
numbers =[ 43,23,12,54,3 ]
numbers.sort()      # Ordena
print(numbers)
numbers.reverse()   # Inverte
print(numbers)
print(numbers.count(3)) # Conta Ocorrências

# Tuples ( Imutáveis ) --------------------------------------------------------------------
print( "\nTuple Demonstration: " )

tuple1 = ("a","b","c")
print(tuple1[0:2]) # [1:] - 1 till end
tuple2 = ( 1, 2, 3)
print( tuple1 + tuple2)

# Dictionary ( HASH ) --------------------------------------------------------------------
print( "\nDictionary Demonstration: " )

capitals = {"USA": "Washington", "Brazil" : "Brasilia", "Russia" : "Moscow"}
print (capitals["USA"])         # Busca pela KEY
capitals["France"] = "Paris"    # Add a new one
capitals.update({"Brazil" : "DF"})
print(capitals)                 # Print all
print(capitals.keys())
print(capitals.values())

# Function --------------------------------------------------------------------
print( "\nFunction Demonstration: " )

def introduce(param):
    print( "I'm a " + param )
    return 2

x = introduce("Function")
print(x)

# Argument Types --------------------------------------------------------------------
print( "\n*Args Demonstration: " )

#Positional
def price(item, price=99):
    print("Item: ", item)
    print("Price: ", price)

price("Pao",23)

#Keyword
price(price=44, item="Molho")

#Default
price("Arroz")

#Multiple *Args Values
def nick(name,*nick):   # Sinaliza que pode receber mais de 1 valor
    print(name , nick)

nick("John", "Pipe", "Guy", "Macro")

#Another Example
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(2,4,5))

# Modules ( outside functions ) ----------------------------------------------------
print( "\nModule Demonstration: " )

# Import no Início
func.hello()
func.bye()

# OOP ----------------------------------------------------------------------------------
print( "\nOOP Demonstration: " )

# Self - Endereço de memória do objeto
# Contrutor é ÚNICO ( não adianta ter mais de um )
class Student: 
    def __init__(self):         # Constructor 
        self.name = "Zanda"
        self.age = 20
        self.note = 10
    
    def talk(self):             # Method
        print(self.name + " is talking rn.")

student1 = Student()
print(student1.age)     # Show
student1.name = "ZaZa"  # Modify
student1.talk()

class Stuud:                    # Parametrized Constructor
    def __init__(self, n, a, m):
        self.__name = n             # Private
        self.__age = a              # Private
        self.__mark = m             # Private
        self.media = 21             # Public

    def display(self):
        print("Hi "+ self.__name)               
        print("You'r",self.__age,"yo")          
        print("Your mark is:",self.__mark)     

    def getName(self):         # GETTER
        return self.__name
    
    def setAge(self,new):       # SETTER
        self.__age = new
    
student2 = Stuud("John",21,7)
# print(student2.__name) - Private Error
student2.setAge(88)
print(student2.getName())
student2.display()

# Inheritance ---------------------------------------------------------------------------
print( "\nInheritance Demonstration: " )

# Father Class
class Polygon:
    __width = 0
    __height = 0

    def setValues(self,width,height):
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
# Child Class    
class Square1(Polygon):      # Inherit ( pode ser múltipla )
    def area(self):
        return self.getHeight() * self.getWidth()
    
form1 = Square1()
print(form1.getHeight())
form1.setValues(4,4)

# "Super" keyword ---------------------------------------------------------------------------
print( "\nSuper Keyword Demonstration: " )

# Whitout SUPER
class Parent:
    def __init__(self,name):
        print("Parent",name,"Inited")

class Child(Parent):
    def __init__(self):
        print("Child Inited")
        Parent.__init__(self,"john")

child1 = Child()

# With SUPER
class Parent2:
    def __init__(self,name):
        print("Parent",name,"Inited")

class Child2(Parent2):
    def __init__(self):
        print("Child Inited")
        super().__init__("john")    # Super here

child2 = Child2()

# Composition ---------------------------------------------------------------------------
print( "\nComposition Demonstration: " )

# "PART OF" - STRONG
# Chama uma classe dentro de outra
class Salary1:
    def __init__(self,pay,reward):
        self.__pay = pay
        self.__reward = reward
    
    def calculateSalary(self):
        return self.__pay*12 + self.__reward
    
class Employee1:
    def __init__(self,name,position,pay,reward):
        self.__name = name
        self.__position = position
        self.__finalSalary = Salary1(pay,reward) # __finalSalary CRIA um Objeto "Salary"
    
    def showSalary(self):
        return self.__finalSalary.calculateSalary() 

emp = Employee1("Zaaz","Dev", 100, 321)
print(emp.showSalary())

# Composition ---------------------------------------------------------------------------
print( "\nAggregation Demonstration: " )

# "HAS A" - WEAK
# Usa um objeto para cada class, faz relação entre eles
class Salary:
    def __init__(self,pay,reward):
        self.__pay = pay
        self.__reward = reward
    
    def calculateSalary(self):
        return self.__pay*12 + self.__reward
    
class Employee:
    def __init__(self,name,position, sal):  # Object as argument
        self.__name = name
        self.__position = position
        self.__finalSalary = sal            # __finalSalary RECEBE um objeto "Salary"
    
    def showSalary(self):
        return self.__finalSalary.calculateSalary() 

sal = Salary(200,123)           # Cria um obj para o salário
emp = Employee("Zaaz","Dev", sal)
print(emp.showSalary())

# Abstract Class ----------------------------------------------------------------------
print( "\nAbstract class Demonstration: " )

# 1. When users won't be able to create objects from father class
# 2. When you NEED methods on the Parent class in the child ones.
# Abstract Class
class Shape(ABC):           # Inherit from lib
    @abstractclassmethod    # PRECISA definir esse método
    def area(self):
        pass

    @abstractclassmethod    # PRECISA definir esse método
    def perimeter(self):
        pass

# Child Class
class Square(Shape):
    def __init__(self,side):
        self.__side = side

    def area(self):             # Definição
        return self.__side * self.__side
    
    def perimeter(self):        # Definição
        return 4 * self.__side

# obj1 = Shape() -  ERROR
sqrObj = Square(12)
print(sqrObj.area())

# Operator Overloading -------------------------------------------------------------------
print( "\nAbstract class Demonstration: " )

class Book:
    def __init__(self,pages):
        self.__pages = pages
    
    def __add__(self,other):                    # Operator "+" ( add ) overloadings
        return self.__pages + other.__pages     # What he's going to do
    
b1 = Book(100)
b2 = Book(200)
print(b1 + b2)

# Exceptions -------------------------------------------------------------------
print( "\nException Demonstration: " )

# User defined Exception
class by3Exception(Exception):
    def __init__(self,arg):
        self.msg = arg


# "Exception" type é o caso geral 
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))

try:
    result = n1/n2                  # Can't be Zero or Wrong Types
    print("Result =",result)
    if(n2 == 3):
        raise by3Exception("Division by 3 Alert !")
except TypeError as e:              # e =  Cause of exception 
    print("Error of Types -",e)
except ZeroDivisionError as e:      # e =  Cause of exception 
    print("Error of ZERO -",e)
except Exception as e:              # e =  Cause of exception ( CASO GERAL )
    print("Error -",e)
else:
    print("No errors at all")       # In case of no exception
finally:
    print("FINISH ! ! !")           # Always run

# raise Exception ("And result greater than 2")   # Personal Exception

# Exceptions -------------------------------------------------------------------
print( "\n__name__ Demonstration: " )

print(func.add(3,2))
# Mesmo sem estar aqui o "print(add)" do "someFunctions" aparecia
# Mas agora com a verificação de MAIN ou INPUT, não mais

# Files ---------------------------------------------------------------------------
print( "\nFiles Demonstration: " )

# W R I T I N G
file = open("Example.txt","w")  # WRITING - Rewrite all that is in it
#r+ -  Preserves previous content and append
#w+ - Override previous content

file.write("Ai minha voaida\n") 
file.write("Linha 2\n") 
file.write("Linha 3\n") 
for i in range(1,11):
    file.write("%d " %i)        # Tem que converter pois .txt apenas aceita STRING
file.write("\n") 

file.close()

# R E A D I N G
# Trabalha com POINTER de leitura ( cabeçote )
file = open("Example.txt","r")

print(file.read(2))       # Le até o 2 caracter
file.seek(0)

print(file.readlines()[0])     # Separa linhas como LISTAS ( só funciona sozinho )
file.seek(0)

print(file.readline())    # Vem com linha em branco automático
file.seek(0)

print(file.read())

file.close()

