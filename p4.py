#Create a DataFrame
#Create a DataFrame with the following data:
#Name	Age	City
#Ravi	20	Chennai
#Meena	19	Mumbai
#John	21	Delhi
#Print:
#The shape of the DataFrame
#The column names
#The first and last row      
import pandas as pd

# Create DataFrame using a list of dictionaries
df_alt = pd.DataFrame([
    {'Name': 'Ravi', 'Age': 20, 'City': 'Chennai'},
    {'Name': 'Meena', 'Age': 19, 'City': 'Mumbai'},
    {'Name': 'John', 'Age': 21, 'City': 'Delhi'}
])

# Print shape
print("Shape:", df_alt.shape)

# Print column names
print("Columns:", list(df_alt.columns))

# Access first row using the head() method
print("First row:\n", df_alt.head(1))

# Access last row using tail()
print("Last row:\n", df_alt.tail(1))