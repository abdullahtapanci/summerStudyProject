import pandas as pd

def rsi( data , window=14 )
    """
    Calculate the Relative Strength Index (RSI) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least one column named 'price'.
    window (int): The number of periods to use for calculating the RSI.

    Returns:
    pd.Series: A pandas Series containing the RSI values.
    """
    delta = data['price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi