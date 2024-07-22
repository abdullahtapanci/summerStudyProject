import pandas as pd

def macd(data, short_window=12, long_window=26, signal_window=9):
    """
    Calculate MACD (Moving Average Convergence Divergence) and its Signal line for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least one column named 'price'.
    short_window (int): Short-term EMA window.
    long_window (int): Long-term EMA window.
    signal_window (int): Signal line EMA window.

    Returns:
    pd.DataFrame: DataFrame with MACD Line, Signal Line, and MACD Histogram.
    """
    # Calculate short-term EMA
    short_ema = data['price'].ewm(span=short_window, adjust=False).mean()
    
    # Calculate long-term EMA
    long_ema = data['price'].ewm(span=long_window, adjust=False).mean()
    
    # Calculate MACD Line
    macd_line = short_ema - long_ema
    
    # Calculate Signal Line (9-period EMA of MACD Line)
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
    
    # Calculate MACD Histogram
    macd_histogram = macd_line - signal_line
    
    # Combine into a DataFrame
    macd_data = pd.DataFrame({
        'MACD Line': macd_line,
        'Signal Line': signal_line,
        'MACD Histogram': macd_histogram
    })
    
    return macd_data
