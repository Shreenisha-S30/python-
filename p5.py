import pandas as pd
# Display only "Name" column using dot notation
df_alt = pd.DataFrame([
    {'Name': 'Ravi', 'Age': 20, 'City': 'Chennai'},
    {'Name': 'Meena', 'Age': 19, 'City': 'Mumbai'},
    {'Name': 'John', 'Age': 21, 'City': 'Delhi'}
])
print("Names:\n", df_alt.Name)

# Select students older than 19 and display names and cities
older_students = df_alt[df_alt['Age'].gt(19)][['Name', 'City']]
print("Names and Cities of students > 19:\n", older_students)