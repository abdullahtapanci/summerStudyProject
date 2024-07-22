import pandas as pd

def stochasticOscillator(data, window=14, smoothing=3):
    """
    Calculate Stochastic Oscillator (%K and %D) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high', 'low', and 'close'.
    window (int): Number of periods to consider for calculating %K.
    smoothing (int): Smoothing factor for calculating %D (typically a 3-period SMA).

    Returns:
    pd.DataFrame: DataFrame with %K and %D values.
    """
    # Calculate Lowest Low and Highest High over the window
    low_min = data['low'].rolling(window=window).min()
    high_max = data['high'].rolling(window=window).max()
    
    # Calculate %K
    percent_k = ((data['close'] - low_min) / (high_max - low_min)) * 100
    
    # Calculate %D (3-period SMA of %K)
    percent_d = percent_k.rolling(window=smoothing).mean()
    
    # Combine into a DataFrame
    stochastic_oscillator = pd.DataFrame({
        '%K': percent_k,
        '%D': percent_d
    })
    
    return stochastic_oscillator
