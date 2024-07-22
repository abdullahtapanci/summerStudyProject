import pandas as pd

def weightedAveragePrice(data):
    """
    Calculate Weighted Average Price (WAP) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with 'price' and 'volume' columns.

    Returns:
    float: Weighted Average Price (WAP).
    """
    # Calculate the sum of (Price * Volume)
    weighted_sum = (data['price'] * data['volume']).sum()
    
    # Calculate the sum of Volume
    total_volume = data['volume'].sum()
    
    # Calculate Weighted Average Price (WAP)
    wap = weighted_sum / total_volume
    
    return wap

# Example usage:
# Assuming 'trades_data' DataFrame has 'price' and 'volume' columns
# wap = calculate_weighted_average_price(trades_data)
