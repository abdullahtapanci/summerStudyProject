import pandas as pd

def ema(data, window=14):
    """
    Calculate the Exponential Moving Average (EMA) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least one column named 'price'.
    window (int): The number of periods to use for calculating the EMA.

    Returns:
    pd.Series: A pandas Series containing the EMA values.
    """
    ema = data['price'].ewm(span=window, adjust=False).mean()
    return ema