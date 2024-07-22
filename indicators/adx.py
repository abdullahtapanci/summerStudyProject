import pandas as pd

def adx(data, period=14):
    """
    Calculate Average Directional Index (ADX) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high', 'low', and 'close'.
    period (int): Number of periods to consider for calculating ADX.

    Returns:
    pd.Series: Series containing ADX values.
    """
    # Calculate True Range (TR)
    data['TR'] = data.apply(lambda row: max(row['high'] - row['low'],
                                           abs(row['high'] - row['close']),
                                           abs(row['low'] - row['close'])), axis=1)
    
    # Calculate Directional Movement (DM) and Directional Index (DI)
    data['plus_dm'] = (data['high'] - data['high'].shift(1)).apply(lambda x: x if x > 0 else 0)
    data['minus_dm'] = (data['low'].shift(1) - data['low']).apply(lambda x: x if x > 0 else 0)
    
    data['plus_di'] = 100 * (data['plus_dm'].rolling(window=period).sum() / data['TR'].rolling(window=period).sum())
    data['minus_di'] = 100 * (data['minus_dm'].rolling(window=period).sum() / data['TR'].rolling(window=period).sum())
    
    # Calculate Directional Index (DX)
    data['dx'] = 100 * abs((data['plus_di'] - data['minus_di']) / (data['plus_di'] + data['minus_di']))
    
    # Calculate ADX
    adx = data['dx'].ewm(span=period, min_periods=period).mean()
    
    return adx

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high', 'low', and 'close' columns
# bitcoin_data['ADX'] = calculate_adx(bitcoin_data)
