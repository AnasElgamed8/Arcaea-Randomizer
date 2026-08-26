from pathlib import Path

import pandas as pd

## Get the current directory and access the sheet
current_dir = Path.cwd()
data_dir = current_dir / 'data'
df = pd.read_csv(data_dir / 'scores2.csv')

## Drop unneeded columns and null values
cols_to_keep = ['Title', "Chart Constant", "Score", "Note Count", "Play Potential"]
df = df[cols_to_keep].dropna()

# Data cleaning: drop duplicates
df = df.drop_duplicates()

# Data cleaning: remove commas ONLY from columns that will become numbers
# (This prevents accidental removal of commas in your song titles)
cols_to_clean = ['Score', 'Note Count', 'Chart Constant']
df[cols_to_clean] = df[cols_to_clean].replace(',', '', regex=True)

# Type casting
df = df.astype({'Score': int, 'Note Count': int, 'Chart Constant': float})

# Pick only charts with a suitable constant
max_constant= 10
min_constant = 9.5
df = df[df["Chart Constant"] >= min_constant]
df = df[df["Chart Constant"] <= max_constant]
# Randomly select and print 1 chart (maintaining the original index number)
print(df.sample(n=1))
