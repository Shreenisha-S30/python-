import pandas as pd
data = { 'Name':['Jeevan','Raju','Ravi'], 'Age':[25,30,22], 'City': ['New York','London','Paris']}
#display whole datqa frame
df = pd.DataFrame(data)

print(df)
#display one column
print("\nName column:",df['Name'])
#display first two rows
print("Displaying first two rows:\n",df.head(2))