#OBS: Comentar código já commitado para não ter erro e PARAR o RUN

# sqlite3 vem imbutida no Python ( não precisa instalar )
import sqlite3

# Create Connection -  "use"
con = sqlite3.connect("my1.db")
cursor = con.cursor() # Object Acess Data ( DAO )

# CREATE Table - Execute = Query
cursor.execute("create table if not exists employees(id integer primary key, name text, salary real, department text, position text) ")
con.commit() # Aplicar Query

# Functions --------------------------------------------------------------------------------

# Function to INSERT
def insert_value(id,name,sal,dep,func):
    cursor.execute("insert into employees values(?,?,?,?,?)",(id,name,sal,dep,func))
    con.commit()

# Function to UPDATE
def update_department(dep,id):
    cursor.execute("update employees set department=? where id=?",(dep, id))
    con.commit()

# Function to SELECT ALL
def select_all():
    cursor.execute("select * from employees")
    data = cursor.fetchall() # Vem como uma LISTA DE TUPLAS
    print(data)
    print("---")

# Function to DELETE ALL
def delete_all():
    cursor.execute("Delete from employees")
    con.commit()

# -----------------------------------------------------------------------------------------

# INSERT
#cursor.execute("insert into employees values(1,'Zanda',2000,'Projects','Dev')")
#con.commit()

# INSERT
#cursor.execute("insert into employees values(2,'Fernando',1050,'Projects','P.O')")
#con.commit()

# UPDATE
#cursor.execute("update employees set department='HR' where id=2")
#con.commit()

# SELECT
cursor.execute("select * from employees")
data = cursor.fetchall() # Vem como uma LISTA DE TUPLAS
print(data)

# Printa cada Tupla
for i in data:
    print(i)

print("---")

# Printa um Elemento Especifico da Tupla 
for i in data:
    print(i[1]) # 0 - Id, 1 - name, etc

print("---")

# SELECT
cursor.execute("select id, name from employees where department=='Projects'")
data = cursor.fetchall()
print(data)
print("---")

# DELETE ONE
# cursor.execute("delete from employees where name=='Gabriel'")
# con.commit()

# DELETE ALL
#cursor.execute("delete from employees")
#con.commit()

insert_value(5,"ZaaZ",950,"Admin","Manager")
update_department("Infra",1)
select_all()
# delete_all()

# Encerra Conexão
cursor.close()
con.close()
