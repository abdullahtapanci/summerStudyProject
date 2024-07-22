import pandas as pd
import numpy as np

def historicalVolatility(data, period=30):
    """
    Calculate Historical Volatility for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'close' column.
    period (int): Number of trading days to calculate historical volatility (default: 30).

    Returns:
    float: Historical volatility over the specified period.
    """
    # Calculate daily returns
    data['daily_return'] = data['close'].pct_change() * 100
    
    # Calculate historical volatility
    historical_volatility = np.sqrt(np.sum(data['daily_return'].tail(period).var())) * np.sqrt(period)
    
    return historical_volatility

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'close' column
# historical_volatility = calculate_historical_volatility(bitcoin_data)
