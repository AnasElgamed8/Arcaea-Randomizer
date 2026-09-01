from pathlib import Path

import pandas as pd
import streamlit as st


class Sheet:
    def __init__(self):
        project_dir = Path(__file__).resolve().parent.parent
        data_dir = project_dir / "data"

        with open(data_dir / "about.md") as f:
            self.about = f.read()

        try:
            df = pd.read_csv(
                """https://docs.google.com/spreadsheets/d/e/2PACX-1vTpK2YzTTppr13-tjxtEtVgJY0KhRCfOm33-ZagMIVwhrnn_zkHLabd71h9Cvtb8zx_CP_ZXqiP1PtC/pub?gid=1548130374&single=true&output=csv"""
            )
        except:
            st.warning("Couldn't access the online sheet. Using the backup sheet")
            df = pd.read_csv(data_dir / "scores.csv")
        # idk man, I won't even try to calculate it
        self.max_ptt = 14.000
        self.df = df.copy()
        self._cleaning()
        # Keep an unmodified version of the cleaned data frame
        self._original = self.df.copy()

    def _cleaning(self):
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

    @property
    def ptt(self):
        return self._ptt

    @ptt.setter
    def ptt(self, value=-1.0):
        self._ptt = value

    def _filtered_random_pool(self, min_constant, max_constant, difficulty):
        pool = self._original.copy()

        if difficulty is not None:
            df_by_dif = pool["Difficulty"].isin(difficulty)
            pool = pool[df_by_dif]

        if self.ptt >= 0:
            pool = pool[pool["Chart Constant"] > (self.ptt - 2.200)]
        else:
            # Pick only charts with a suitable constant
            pool = pool[pool["Chart Constant"] >= min_constant]
            pool = pool[pool["Chart Constant"] <= max_constant]
        return pool

    def true_random(self, min_constant=1.0, max_constant=12.0, size=1, difficulty=None):
        pool = self._filtered_random_pool(min_constant, max_constant, difficulty)

        # Size error handling
        df_size = len(pool)

        if df_size == 0:
            st.error("No charts fit your current requirements")
            return

        elif df_size < size:
            st.warning(f"Note: Only {df_size} chart(s) fit your current requirements.")

        size = min(size, df_size)

        return pool.sample(n=size)

    def random(self, min_constant=1.0, max_constant=12.0, size=1, difficulty=None):
        pool = self._filtered_random_pool(min_constant, max_constant, difficulty)

        # Size error handling
        df_size = len(pool)

        if df_size == 0:
            st.error("No charts fit your current requirements")
            return

        return pool


if __name__ == "__main__":
    sheet = Sheet()
