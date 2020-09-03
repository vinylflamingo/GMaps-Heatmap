import pandas as pd
file_name = "datasets\\LastYear_New_Orleans.csv"
colnames = ['address', 'incidentDate', 'latitudes', 'longitudes']
df = pd.read_csv(file_name, names=colnames)

# Notes:
# - the `subset=None` means that every column is used
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone
df.drop_duplicates(subset=['address'], inplace=True)

# Write the results to a different file
df.to_csv(file_name, index=False, header=False)
