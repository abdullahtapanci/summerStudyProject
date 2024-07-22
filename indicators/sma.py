import pandas as pd

def sma(data, window=14):
    """
    Calculate the Simple Moving Average (SMA) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least one column named 'price'.
    window (int): The number of periods to use for calculating the SMA.

    Returns:
    pd.Series: A pandas Series containing the SMA values.
    """
    sma = data['price'].rolling(window=window).mean()
    return sma
