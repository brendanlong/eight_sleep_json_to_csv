# Eight Sleep JSON to CSV Converter

A Python script to extract timeseries data from Eight Sleep JSON export files and convert them to CSV format.

## Usage

```bash
./extract_timeseries.py --input sleep_nights.json --output data.csv --timeseries tnt
```

## Parameters

- `--input`: Path to the Eight Sleep JSON export file (sleep_nights.json)
- `--output`: Path for the output CSV file
- `--timeseries`: Type of data to extract:
  - `tnt`: Tosses and turns
  - `tempRoomC`: Room temperature (Celsius)
  - `tempBedC`: Bed temperature (Celsius)
  - `respiratoryRate`: Breaths per minute
  - `heartRate`: Heart beats per minute
  - `hrv`: Heart rate variability (milliseconds)

## Output Format

The script generates a CSV file with two columns:
- `timestamp`: ISO 8601 formatted timestamp
- `[timeseries_type]`: The extracted value

## Requirements

- Python 3.x
- No external dependencies required