import pandas as pd
import os

def load_data(filepath):
    """
    Loads data from a given CSV filepath.
    Throws an explicit error if the file is missing so your pipeline fails fast.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CRITICAL ERROR: File not found at {filepath}")
    return pd.read_csv(filepath)
