import pandas

df1 = pandas.read_csv("Jupyter/traffic.csv")

# Raw
print(df1,"\n")

# Size
print(df1.shape,"\n")   # (10,6) - ( rows, columns )

# "Selecting" data by Names - LOC
print(df1.loc[2:5,"Country":"Clicks"],"\n") # Index 2 to 5 and Country to Clicks
print(df1.loc[4,"Date":"Country"],"\n")
print(df1.loc[:,"Visitors"],"\n")

# "Selecting" data by Index - ILOC
print(df1.iloc[2:5,1:4],"\n") # Exclui o 4 e o 5

# Deleting ROWS or COLUMS
print(df1.drop("Day",axis=1),"\n")  # Must be 1 - DELETE COLUMN
print(df1.drop(1,axis=0),"\n")           # Must be 0 - DELETE ROW

# Adding Columns
df1["New"] = ["Z"]*df1.shape[0]  # tem quer ser o msm número de rows
print(df1,"\n")

# Updating Columns
df1["Day"] = df1["Day"] + " Voaida"
print(df1,"\n")

# TRAVERSING ( rows become columns and Vice-Versa )
print(df1.T)

# Adding Rows: TRAVERSE -> Add a new column -> TRAVERSE back 