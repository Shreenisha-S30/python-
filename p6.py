# Add "Marks" column
import pandas as pd
df_alt = pd.DataFrame
df_alt['Marks'] = [85, 90, 75]
print("After adding Marks:\n", df_alt)

# Delete the "City" column using 'del'
del df_alt['City']
print("After removing City:\n", df_alt)