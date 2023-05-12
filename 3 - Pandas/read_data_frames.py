# Reading Different Files
# Mesmo código do "jupyter"
import pandas

df1 = pandas.read_csv("Jupyter/traffic.csv")

df2 = pandas.read_excel("Jupyter/traffic.xlsx")

df3 = pandas.read_json("Jupyter/traffic.json")

df4 = pandas.read_csv("Jupyter/traffic-semi-colons.txt", sep=";") # Altera separador

# Lendo CSV de uma API
df5 = pandas.read_csv("https://raw.githubusercontent.com/uwlearning/pandas/master/traffic.csv")

# Lendo JSON de uma API
df6 = pandas.read_json("https://raw.githubusercontent.com/uwlearning/pandas/master/traffic.json")

print(df1,"\n")
print(df2,"\n")

# Toda DF vem com um index por LINHA ( podemos mudar )
# Esse é apenas um print alterado ( não salvo )
print(df2.set_index("Date"),"\n")  # Print com o index = "Date"
# Salvando mudança
df2 = df2.set_index("Date") # Save com novo Index

print(df2,"\n")
print(df3,"\n")
print(df4,"\n")
print(df5,"\n")
print(df6)