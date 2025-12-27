"""
Analysis script for ray morphometrics.
Contains functions for calculating morphological ratios.
"""

import csv
import os


def calculate_disc_ratio(total_length, disc_width):
    """
    Calculate the disc width ratio (disc_width / total_length).
    
    This ratio is useful for distinguishing between dorsoventrally flattened
    species (like thornback rays) and more torpedo-shaped species (like electric rays).
    
    Parameters
    ----------
    total_length : float
        Total length of the ray in cm.
    disc_width : float
        Disc width (width across the pectoral fins) in cm.
    
    Returns
    -------
    float
        Disc width ratio (unitless).
    
    Raises
    ------
    ZeroDivisionError
        If total_length is zero.
    """
    if total_length == 0:
        raise ZeroDivisionError("Total length cannot be zero.")
    return disc_width / total_length


def load_measurements(filepath):
    """
    Load ray measurement data from a CSV file.
    
    Parameters
    ----------
    filepath : str
        Path to CSV file with columns: species_id, total_length, disc_width, weight.
    
    Returns
    -------
    list of dict
        Each dict contains measurement fields.
    """
    measurements = []
    with open(filepath, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric columns
            row['total_length'] = float(row['total_length'])
            row['disc_width'] = float(row['disc_width'])
            row['weight'] = float(row['weight'])
            measurements.append(row)
    return measurements


def main():
    """Example usage: compute disc width ratios for the sample dataset."""
    data_path = os.path.join('data', 'ray_measurements.csv')
    if not os.path.exists(data_path):
        print("Data file not found:", data_path)
        return
    
    measurements = load_measurements(data_path)
    print("Disc width ratios:")
    for m in measurements:
        ratio = calculate_disc_ratio(m['total_length'], m['disc_width'])
        print(f"{m['species_id']}: total_length={m['total_length']:.1f}, "
              f"disc_width={m['disc_width']:.1f}, ratio={ratio:.3f}")


if __name__ == '__main__':
    main()