#!/usr/bin/env python3
"""
Extract timeseries data from Eight Sleep JSON export files.

Usage:
    ./extract_timeseries.py --input sleep_nights.json --output data.csv --timeseries tnt
"""

import argparse
import json
import csv
from pathlib import Path
from typing import List, Tuple, Dict, Any


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Extract timeseries data from Eight Sleep JSON export files'
    )
    parser.add_argument(
        '--input',
        type=Path,
        required=True,
        help='Input JSON file containing sleep sessions'
    )
    parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help='Output CSV file'
    )
    parser.add_argument(
        '--timeseries',
        type=str,
        required=True,
        help='Timeseries type to extract (e.g., tnt, tempRoomC, tempBedC, respiratoryRate, heartRate, hrv)'
    )
    return parser.parse_args()


def extract_timeseries(json_file: Path, timeseries_type: str) -> List[Tuple[str, Any]]:
    """
    Extract specified timeseries data from JSON file.
    
    Args:
        json_file: Path to input JSON file
        timeseries_type: Type of timeseries to extract
        
    Returns:
        List of (timestamp, value) tuples
    """
    data_points: List[Tuple[str, Any]] = []
    
    with open(json_file, 'r') as f:
        data: Dict[str, Any] = json.load(f)
        
    sessions: List[Dict[str, Any]] = data.get('sessions', [])
    
    for session in sessions:
        timeseries: Dict[str, List[List[Any]]] = session.get('timeseries', {})
        
        if timeseries_type in timeseries:
            # Each timeseries is a list of [timestamp, value] pairs
            for timestamp, value in timeseries[timeseries_type]:
                data_points.append((timestamp, value))
                
    return data_points


def write_csv(data_points: List[Tuple[str, Any]], output_file: Path, timeseries_type: str) -> None:
    """
    Write data points to CSV file.
    
    Args:
        data_points: List of (timestamp, value) tuples
        output_file: Path to output CSV file
        timeseries_type: Type of timeseries (for header)
    """
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['timestamp', timeseries_type])
        
        # Write data
        for timestamp, value in data_points:
            writer.writerow([timestamp, value])


def main() -> None:
    """Main function."""
    args = parse_arguments()
    
    # Extract timeseries data
    print(f"Extracting '{args.timeseries}' data from '{args.input}'...")
    data_points = extract_timeseries(args.input, args.timeseries)
    
    if not data_points:
        print(f"Warning: No '{args.timeseries}' data found in input file")
    else:
        print(f"Found {len(data_points)} data points")
    
    # Write to CSV
    print(f"Writing data to '{args.output}'...")
    write_csv(data_points, args.output, args.timeseries)
    
    print("Done!")


if __name__ == '__main__':
    main()