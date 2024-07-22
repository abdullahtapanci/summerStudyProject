import pandas as pd

def aroon(data, period=25):
    """
    Calculate Aroon Indicator and Aroon Oscillator for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high' and 'low'.
    period (int): Number of periods to consider for calculating Aroon.

    Returns:
    pd.DataFrame: DataFrame with 'Aroon Up', 'Aroon Down', and 'Aroon Oscillator' columns.
    """
    # Calculate Aroon Up
    data['Aroon Up'] = data['high'].rolling(window=period+1).apply(lambda x: x.argmax(), raw=True) / period * 100

    # Calculate Aroon Down
    data['Aroon Down'] = data['low'].rolling(window=period+1).apply(lambda x: x.argmin(), raw=True) / period * 100

    # Calculate Aroon Oscillator
    data['Aroon Oscillator'] = data['Aroon Up'] - data['Aroon Down']

    return data[['Aroon Up', 'Aroon Down', 'Aroon Oscillator']]

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high' and 'low' columns
# bitcoin_data_with_aroon = calculate_aroon(bitcoin_data)
