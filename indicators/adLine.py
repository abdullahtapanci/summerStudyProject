import pandas as pd

def adLine(data):
    """
    Calculate Accumulation/Distribution Line (A/D Line) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'high', 'low', 'close', and 'volume'.

    Returns:
    pd.Series: Series containing A/D Line values.
    """
    adr = ((data['close'] - data['low']) - (data['high'] - data['close'])) / (data['high'] - data['low'])
    ad_line = (adr * data['volume']).cumsum()
    
    return ad_line

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high', 'low', 'close', and 'volume' columns
# bitcoin_data['AD_Line'] = calculate_ad_line(bitcoin_data)
