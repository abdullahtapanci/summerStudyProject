import pandas as pd

def ppo(data, short_period=12, long_period=26, signal_period=9):
    """
    Calculate Percentage Price Oscillator (PPO) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'close' column.
    short_period (int): Number of periods for short-term EMA.
    long_period (int): Number of periods for long-term EMA.
    signal_period (int): Number of periods for signal line EMA.

    Returns:
    pd.DataFrame: DataFrame with 'PPO' and 'PPO Signal' columns.
    """
    # Calculate short-term and long-term EMAs
    short_ema = data['close'].ewm(span=short_period, min_periods=short_period).mean()
    long_ema = data['close'].ewm(span=long_period, min_periods=long_period).mean()
    
    # Calculate PPO Line
    data['PPO'] = ((short_ema - long_ema) / long_ema) * 100
    
    # Calculate PPO Signal Line
    data['PPO Signal'] = data['PPO'].ewm(span=signal_period, min_periods=signal_period).mean()
    
    return data[['PPO', 'PPO Signal']]

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'close' column
# bitcoin_data_with_ppo = calculate_ppo(bitcoin_data)
