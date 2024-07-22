import pandas as pd

def volumeChange(new_volume, old_volume):
    """
    Calculate Volume Change percentage.

    Parameters:
    new_volume (float): New volume value.
    old_volume (float): Old volume value.

    Returns:
    float: Volume change percentage.
    """
    volume_change = ((new_volume - old_volume) / old_volume) * 100
    return volume_change

# Example usage:
# Assuming new_volume and old_volume are provided as float values
# volume_change = calculate_volume_change(new_volume, old_volume)
