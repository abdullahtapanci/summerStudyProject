import pandas as pd

def bollingerBands(data, window=20, factor=2):
    """
    Calculate Bollinger Bands (Middle, Upper, Lower) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least one column named 'price'.
    window (int): Window size for calculating the Simple Moving Average (Middle Band).
    factor (float): Number of standard deviations to add/subtract to calculate Upper/Lower Bands.

    Returns:
    pd.DataFrame: DataFrame with Middle Band, Upper Band, Lower Band.
    """
    # Calculate Middle Band (SMA)
    middle_band = data['price'].rolling(window=window).mean()
    
    # Calculate Standard Deviation
    std_dev = data['price'].rolling(window=window).std()
    
    # Calculate Upper and Lower Bands
    upper_band = middle_band + (factor * std_dev)
    lower_band = middle_band - (factor * std_dev)
    
    # Combine into a DataFrame
    bollinger_bands = pd.DataFrame({
        'Middle Band': middle_band,
        'Upper Band': upper_band,
        'Lower Band': lower_band
    })
    
    return bollinger_bands
