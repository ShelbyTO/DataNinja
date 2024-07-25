# DataNinja/data_analysis.py
import pandas as pd
import numpy as np

def calculate_statistics(df):
    """Calculate and return basic statistics of a DataFrame."""
    return df.describe()

def fill_missing_values(df, method='mean'):
    """Fill missing values in DataFrame."""
    if method == 'mean':
        return df.fillna(df.mean())
    elif method == 'median':
        return df.fillna(df.median())
    elif method == 'mode':
        return df.fillna(df.mode().iloc[0])
    else:
        raise ValueError("Method not recognized. Use 'mean', 'median', or 'mode'.")
