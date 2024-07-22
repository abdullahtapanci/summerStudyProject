import pandas as pd

def mfi(data, window=14):
    """
    Calculate Money Flow Index (MFI) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high', 'low', 'close', and 'volume'.
    window (int): Number of periods to consider for calculating MFI.

    Returns:
    pd.Series: Series containing MFI values.
    """
    typical_price = (data['high'] + data['low'] + data['close']) / 3
    raw_money_flow = typical_price * data['volume']

    positive_flow = raw_money_flow * (typical_price > typical_price.shift(1))
    negative_flow = raw_money_flow * (typical_price < typical_price.shift(1))

    positive_mf = positive_flow.rolling(window=window, min_periods=1).sum()
    negative_mf = negative_flow.rolling(window=window, min_periods=1).sum()

    money_ratio = positive_mf / negative_mf
    mfi = 100 - (100 / (1 + money_ratio))

    return mfi

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high', 'low', 'close', and 'volume' columns
# bitcoin_data['MFI'] = calculate_mfi(bitcoin_data)
