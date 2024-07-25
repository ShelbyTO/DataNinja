# DataNinja/visualization.py
import matplotlib.pyplot as plt
import missingno as msno
from ydata_profiling import ProfileReport

def plot_missing_data(df):
    """Plot a visualization of missing data."""
    msno.matrix(df)
    plt.show()

def generate_data_profile(df):
    """Generate and display a data profile report."""
    profile = ProfileReport(df, title="Data Profile Report", explorative=True)
    return profile.to_notebook_iframe()
