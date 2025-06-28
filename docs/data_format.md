# Exported data

There are two JSON files included in the export. "user_profile.json" contains the profile for the EightSleep account. "sleep_nights.json" contains the sleep sessions saved under the EightSleep account.

### Sleep Sessions
The sleep sessions contain the detected and aggregated sessions throughout the usage of the product up to the point of export. Each sleep session contains a timestamp for when the session began, an ordered list of sleep stages with duration, and other detected timeseries data. Below is a sample single session.

```
{
    "ts": 1709881620
    "stages": [
        {
            "stage": "light",
            "duration": 120
        },
        {
            "stage": "deep",
            "duration": 240
        },
        {
            "stage": "light",
            "duration": 150
        },
        ...
    ],
    "timeseries": {
        "tnt": [["2024-03-08T08:20:30Z", 1], ...],
        "tempRoomC": [["2024-03-08T08:20:30Z", 23.1], ...],
        "tempBedC": [["2024-03-08T08:20:30Z", 26.2], ...],
        "respiratoryRate" = [["2024-03-08T08:20:30Z", 11.2], ...],
        "heartRate": [["2024-03-08T08:20:30Z", 47], ...],
        "hrv": [["2024-03-08T08:20:30Z", 81.7], ...]
    }
}
```

`ts` is a UNIX epoch timestamp. The sample's timestamp is March 8, 2024 7:07:00 AM.

`stages` are a list of ordered sleep stages, each with a stage type (light, deep, rem, awake, out) and a duration in seconds.

`timeseries` are different measured events marked with a timestamp
- `tnt` are tosses and turns
- `tempRoomC` are room temperature measurements in Celsius
- `tempBedC` are bed temperature measurements in Celsius
- `respiratoryRate` is detected breaths per minute
- `heartRate` is detected heart beats per minute
- `hrv` is detected heart rate variability in milliseconds


### Other notes
The attached files are of type [JSON](https://www.json.org/json-en.html). JSON can be parsed from a variety of internet tools or programmatic reader libraries.