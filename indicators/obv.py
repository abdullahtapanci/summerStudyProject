import pandas as pd

def obv(data):
    """
    Calculate On-Balance Volume (OBV) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least columns 'close' and 'volume'.

    Returns:
    pd.Series: Series containing OBV values.
    """
    # Initialize OBV with zero
    obv = [0]

    # Calculate OBV values
    for i in range(1, len(data)):
        if data['close'].iloc[i] > data['close'].iloc[i - 1]:
            obv.append(obv[-1] + data['volume'].iloc[i])
        elif data['close'].iloc[i] < data['close'].iloc[i - 1]:
            obv.append(obv[-1] - data['volume'].iloc[i])
        else:
            obv.append(obv[-1])

    return pd.Series(obv, index=data.index)

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'close' and 'volume' columns
# bitcoin_data['OBV'] = calculate_obv(bitcoin_data)
