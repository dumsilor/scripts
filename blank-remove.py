import pandas as pd

# Read the input file
input_file = '1.xlsx'
output_file = 'VM List-17-11-2024-updated(1).xlsx'

# Load the data into a pandas DataFrame
df = pd.read_csv(input_file, sep='\t')

# Remove completely blank rows
df.dropna(how='all', inplace=True)

# Save the cleaned DataFrame to a new file
df.to_csv(output_file, sep='\t', index=False)

print(f'Blank rows removed and saved to {output_file}')


