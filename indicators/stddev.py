import pandas as pd

def stddev(data, period=20):
    """
    Calculate Standard Deviation Indicator for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'close' column.
    period (int): Number of periods to consider for calculating Standard Deviation.

    Returns:
    pd.Series: Series containing Standard Deviation values.
    """
    # Calculate the Mean (Simple Moving Average)
    data['Mean'] = data['close'].rolling(window=period).mean()
    
    # Calculate Squared Deviations
    data['Squared Deviation'] = (data['close'] - data['Mean']) ** 2
    
    # Calculate Variance
    variance = data['Squared Deviation'].rolling(window=period).mean()
    
    # Calculate Standard Deviation
    data['Std Deviation'] = variance.apply(lambda x: x ** 0.5)
    
    return data['Std Deviation']

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'close' column
# bitcoin_data['Std Deviation'] = calculate_stddev(bitcoin_data)
