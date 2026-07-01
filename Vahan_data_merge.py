import pandas as pd
from IPython.display import display, FileLink
import glob

# Ensure the correct path concatenation
files_path = r'D:\Professional\Python\Working files\Vahan Data\Raw data\Chennai till date jun 2026\\'

# Use the correct wildcard to match all Excel files
excel_files = glob.glob(files_path + '*.xlsx')

master_df = pd.DataFrame()

# Loop through each file and process
for file in excel_files:
    print(file)

    # Read the Excel file
    df = pd.read_excel(file)

    # Extract the state name from the first column name
    state_name = list(df.columns)[0].replace("Vehicle Class Wise Fuel Data  of ", '')

    # Rename columns appropriately
    df.columns = ['S.No', 'Vehicle Category'] + list(df.iloc[2][2:len(df.columns)-1]) + ['Total']

    # Drop the first three rows and reset the index
    df = df[3:].reset_index(drop=True)

    # Add the state name as a new column
    df['state'] = state_name

    # Concatenate to the master DataFrame
    master_df = pd.concat([master_df, df], ignore_index=True)

# Save the master DataFrame as an Excel file
output_path = r'D:\Professional\Python\Working files\Vahan Data\Processed data\Chennai till date jun 2026.xlsx'
master_df.to_excel(output_path, index=False)

# Display link to the saved file
display(FileLink(output_path))
