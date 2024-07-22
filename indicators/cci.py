import pandas as pd

def cci(data, period=20):
    """
    Calculate Commodity Channel Index (CCI) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high', 'low', and 'close'.
    period (int): Number of periods to consider for calculating CCI.

    Returns:
    pd.Series: Series containing CCI values.
    """
    # Calculate Typical Price (TP)
    data['TP'] = (data['high'] + data['low'] + data['close']) / 3
    
    # Calculate Simple Moving Average (SMA) of Typical Prices
    data['SMA_TP'] = data['TP'].rolling(window=period).mean()
    
    # Calculate Mean Deviation (MD)
    data['MD'] = data['TP'].rolling(window=period).apply(lambda x: pd.Series(x).mad())
    
    # Calculate Commodity Channel Index (CCI)
    data['CCI'] = (data['TP'] - data['SMA_TP']) / (0.015 * data['MD'])
    
    return data['CCI']

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high', 'low', and 'close' columns
# bitcoin_data['CCI'] = calculate_cci(bitcoin_data)
