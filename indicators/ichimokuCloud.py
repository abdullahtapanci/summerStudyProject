import pandas as pd

def ichimokuCloud(data, tenkan_period=9, kijun_period=26, senkou_span_b_period=52):
    """
    Calculate Ichimoku Cloud components for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'high', 'low', and 'close' column.
    tenkan_period (int): Number of periods for Tenkan-sen (default: 9).
    kijun_period (int): Number of periods for Kijun-sen (default: 26).
    senkou_span_b_period (int): Number of periods for Senkou Span B (default: 52).

    Returns:
    pd.DataFrame: DataFrame with 'Tenkan-sen', 'Kijun-sen', 'Senkou Span A', 'Senkou Span B', and 'Chikou Span' columns.
    """
    # Tenkan-sen (Conversion Line)
    data['Tenkan-sen'] = (data['high'].rolling(window=tenkan_period).max() + data['low'].rolling(window=tenkan_period).min()) / 2
    
    # Kijun-sen (Base Line)
    data['Kijun-sen'] = (data['high'].rolling(window=kijun_period).max() + data['low'].rolling(window=kijun_period).min()) / 2
    
    # Senkou Span A (Leading Span A)
    data['Senkou Span A'] = ((data['Tenkan-sen'] + data['Kijun-sen']) / 2).shift(kijun_period)
    
    # Senkou Span B (Leading Span B)
    data['Senkou Span B'] = ((data['high'].rolling(window=senkou_span_b_period).max() + data['low'].rolling(window=senkou_span_b_period).min()) / 2).shift(kijun_period)
    
    # Chikou Span (Lagging Span)
    data['Chikou Span'] = data['close'].shift(-kijun_period)
    
    return data[['Tenkan-sen', 'Kijun-sen', 'Senkou Span A', 'Senkou Span B', 'Chikou Span']]

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high', 'low', and 'close' columns
# bitcoin_data_with_ichimoku = calculate_ichimoku_cloud(bitcoin_data)
