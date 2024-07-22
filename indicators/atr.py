import pandas as pd

def atr(data, window=14):
    """
    Calculate Average True Range (ATR) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high', 'low', and 'close'.
    window (int): Number of periods to consider for calculating ATR.

    Returns:
    pd.Series: Series containing ATR values.
    """
    # Calculate True Range (TR)
    data['TR'] = data.apply(lambda row: max(row['high'] - row['low'],
                                           abs(row['high'] - row['close']),
                                           abs(row['low'] - row['close'])), axis=1)
    
    # Calculate ATR (Average True Range)
    data['ATR'] = data['TR'].rolling(window=window).mean()
    
    return data['ATR']
