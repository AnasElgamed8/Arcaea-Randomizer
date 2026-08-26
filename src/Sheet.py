from pathlib import Path

import pandas as pd


class Sheet:
    def __init__(self):
        #TODO: Find a way to automatically pull the latest sheet

        # Get the current directory and access the sheet
        project_dir = Path.cwd()
        data_dir = project_dir / 'data'
        df = pd.read_csv(data_dir / 'scores.csv')

        self.df = df.copy()
        self.cleaning()
        # Keep an unmodified version of the cleaned data frame
        self._original = self.df.copy()

    def cleaning(self):
        # Drop unneeded columns and null values
        cols_to_keep = ['Title', "Chart Constant", "Note Count"]
        self.df = self.df[cols_to_keep].dropna()

        # Remove commas from numerical columns
        cols_to_clean = ['Chart Constant','Note Count']
        self.df[cols_to_clean] = self.df[cols_to_clean].replace(',', '', regex=True)

        # Type casting
        self.df = self.df.astype({'Title': str,'Chart Constant': float, 'Note Count': int })


    def true_random(self,min_constant=0.0,max_constant=14.0,size=1):
        self.df = self._original.copy()
        # Pick only charts with a suitable constant
        self.df = self.df[self.df["Chart Constant"] >= min_constant]
        self.df = self.df[self.df["Chart Constant"] <= max_constant]

        return self.df.sample(n=size)


    def random(self,min_constant=0.0,max_constant=14.0,size=1):
        #TODO: Implement a stack to keep track of already displayed charts, And find a way to track the state.

        self.df = self._original.copy()
        # Pick only charts with a suitable constant
        self.df = self.df[self.df["Chart Constant"] >= min_constant]
        self.df = self.df[self.df["Chart Constant"] <= max_constant]


if __name__ == "__main__":
    sheet = Sheet()
    print(sheet.true_random())
