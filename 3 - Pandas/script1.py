# In pandas we work with DATAFRAMAS ( like a table )
import pandas

# As a  List
df1 = pandas.DataFrame([[5,5000,20],[10,9000,23]], columns = ["Days","Visitors","BR"])

# As a Diary
df2 = pandas.DataFrame({"Days":[5,10], "Visitors":[5000,9000],"BR":[20,23]})

print(df1,"\n")
print(df2,"\n")
print("Max Visitors:",df1.Visitors.max())