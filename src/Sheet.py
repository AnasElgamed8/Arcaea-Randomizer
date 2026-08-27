from pathlib import Path

import pandas as pd
import streamlit as st


class Sheet:
    def __init__(self):
        # TODO: Find a way to automatically pull the latest sheet

        # Get the current directory and access the sheet
        project_dir = Path.cwd()
        data_dir = project_dir / "data"
        df = pd.read_csv(data_dir / "scores.csv")

        self.df = df.copy()
        self.cleaning()
        # Keep an unmodified version of the cleaned data frame
        self._original = self.df.copy()

    def cleaning(self):
        # Drop unneeded columns and null values
        cols_to_keep = ["Title", "Difficulty", "Chart Constant", "Note Count"]
        self.df = self.df[cols_to_keep].dropna()

        # Remove commas from numerical columns
        cols_to_clean = ["Chart Constant", "Note Count"]
        self.df[cols_to_clean] = self.df[cols_to_clean].replace(",", "", regex=True)

        # Type casting
        self.df = self.df.astype(
            {
                "Title": str,
                "Difficulty": str,
                "Chart Constant": float,
                "Note Count": int,
            }
        )

        # TODO: Make a parent class for random with the shared behavior, then inherit the class by true random and random

    def true_random(self, min_constant=1.0, max_constant=12.0, size=1, difficulty=None):

        self.df = self._original.copy()

        if difficulty is not None:
            df_by_dif = self.df["Difficulty"].isin(difficulty)
            self.df = self.df[df_by_dif]

        # Pick only charts with a suitable constant
        self.df = self.df[self.df["Chart Constant"] >= min_constant]
        self.df = self.df[self.df["Chart Constant"] <= max_constant]

        # Size error handling
        df_size = len(self.df)

        if df_size == 0:
            st.error("No charts fit your current requirements")

        elif df_size < size:
            st.warning(f"Note: Only {df_size} chart(s) fit your current requirements.")

        size = min(size, df_size)

        return self.df.sample(n=size)

    # Commented out for now
    # def random(self, min_constant=1.0, max_constant=12.0, size=1):
    #     # TODO: Implement a stack to keep track of already displayed charts, And find a way to track the state.
    #
    #     self.df = self._original.copy()
    #     # Pick only charts with a suitable constant
    #     self.df = self.df[self.df["Chart Constant"] >= min_constant]
    #     self.df = self.df[self.df["Chart Constant"] <= max_constant]
    #


if __name__ == "__main__":
    sheet = Sheet()
    print(sheet.true_random())
