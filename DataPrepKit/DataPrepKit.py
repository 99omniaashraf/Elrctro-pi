import numpy as np
import pandas as pd

def read_data(file_path):
    """
    Read data from a CSV file and return a Pandas DataFrame.

    Parameters:
        - file_path: Path to the file.

    Returns:
        - DataFrame: Pandas DataFrame containing the read data.
    """
    extension = file_path.split('.')[-1].lower()

    if extension == 'csv':
        return pd.read_csv(file_path)
    elif extension == 'xlsx' or extension == 'xls':
        return pd.read_excel(file_path)
    elif extension == 'json':
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Supported formats: CSV, Excel, JSON.")

def data_summary(data):
    """
    Generate a summary of the data including basic statistics.

    Parameters:
        - data: Input Pandas DataFrame.

    Returns:
        - DataFrame: Summary DataFrame containing statistics.
    """
    return data.describe()

def handle_missing_values(data, strategy='mean'):
    """
    Handle missing values in the DataFrame based on the specified strategy.

    Parameters:
        - data: Input Pandas DataFrame.
        - strategy: Strategy to handle missing values. Options: 'mean', 'median', 'mode'.

    Returns:
        - DataFrame: DataFrame with missing values handled based on the specified strategy.
    """
    if strategy == 'mean':
        return data.fillna(data.mean())
    elif strategy == 'median':
        return data.fillna(data.median())
    elif strategy == 'mode':
        return data.fillna(data.mode().iloc[0])
    else:
        raise ValueError("Invalid strategy. Supported strategies: 'mean', 'median', 'mode'.")

def encode_categorical_data(data, columns):
    """
    Encode categorical data in the DataFrame using one-hot encoding.

    Parameters:
        - data: Input Pandas DataFrame.
        - columns: columns data.

    Returns:
        - DataFrame: DataFrame with categorical data encoding.
    """
    return pd.get_dummies(data, columns=columns)