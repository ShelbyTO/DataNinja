# DataNinja/dataframe.py
import pandas as pd

def create_dataframe(data, columns=None):
    """Create a DataFrame using the provided data."""
    if not isinstance(data, dict):
        raise ValueError("Data must be provided as a dictionary.")
    
    df = pd.DataFrame(data, columns=columns)
    return df
