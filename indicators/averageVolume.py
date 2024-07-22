import pandas as pd

def averageVolume(data, period=20):
    """
    Calculate Average Volume for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'volume' column.
    period (int): Number of days to calculate average volume (default: 20).

    Returns:
    float: Average volume over the specified period.
    """
    # Calculate average volume over the specified period
    average_volume = data['volume'].tail(period).mean()
    
    return average_volume

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'volume' column
# average_volume = calculate_average_volume(bitcoin_data)
