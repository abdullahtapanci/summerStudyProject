import pandas as pd

def sar(data, af_start=0.02, af_max=0.20):
    """
    Calculate Parabolic SAR (Stop and Reverse) for a given DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'high' and 'low' column.
    af_start (float): Starting value for Acceleration Factor (default: 0.02).
    af_max (float): Maximum value for Acceleration Factor (default: 0.20).

    Returns:
    pd.Series: Series containing Parabolic SAR values.
    """
    # Initialize variables
    data['SAR'] = 0
    data['EP'] = 0
    data['AF'] = af_start
    
    # Determine initial trend direction
    is_upward = True  # Assume upward trend initially
    
    for i in range(1, len(data)):
        if is_upward:
            # Calculate SAR for upward trend
            if data['high'][i] > data['EP'][i-1]:
                data.at[i, 'EP'] = data['high'][i]
                data.at[i, 'AF'] = min(data['AF'][i-1] + af_start, af_max)
            else:
                data.at[i, 'EP'] = data['EP'][i-1]
                data.at[i, 'AF'] = data['AF'][i-1]
            
            data.at[i, 'SAR'] = data['SAR'][i-1] + data['AF'][i] * (data['EP'][i-1] - data['SAR'][i-1])
            
            # Check for trend reversal
            if data['low'][i] < data['SAR'][i]:
                is_upward = False
                data.at[i, 'SAR'] = data['EP'][i-1]
                data.at[i, 'AF'] = af_start
        
        else:
            # Calculate SAR for downward trend
            if data['low'][i] < data['EP'][i-1]:
                data.at[i, 'EP'] = data['low'][i]
                data.at[i, 'AF'] = min(data['AF'][i-1] + af_start, af_max)
            else:
                data.at[i, 'EP'] = data['EP'][i-1]
                data.at[i, 'AF'] = data['AF'][i-1]
            
            data.at[i, 'SAR'] = data['SAR'][i-1] - data['AF'][i] * (data['SAR'][i-1] - data['EP'][i-1])
            
            # Check for trend reversal
            if data['high'][i] > data['SAR'][i]:
                is_upward = True
                data.at[i, 'SAR'] = data['EP'][i-1]
                data.at[i, 'AF'] = af_start
    
    return data['SAR']

# Example usage:
# Assuming 'bitcoin_data' DataFrame has 'high' and 'low' columns
# bitcoin_data['SAR'] = calculate_sar(bitcoin_data)
