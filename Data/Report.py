import csv
import random
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Load gardens from CSV (assuming GID column exists)
gardens_df = pd.read_csv("Code/Garden.csv")
garden_ids = gardens_df["GID"].tolist()

# Start and end date
start_date = datetime(2025, 1, 1)
end_date = datetime.now()

# Thresholds for out-of-bounds conditions
THRESHOLDS = {
    "Light Level (Lux)": 200,  # Turn on Grow Lights if below this
    "Humidity (%)": 40,  # Turn on Humidifier if below this
    "Soil Moisture (%)": 20,  # Water if below this
    "Temperature (°C)": {"low": 18, "high": 30},  # Heating <18°C, Cooling >30°C
}

# Function to determine if an outlier should be generated
def is_outlier():
    return np.random.exponential(scale=3) > 15  # Small chance of extreme values

# Function to generate sensor readings with occasional outliers
def generate_value(normal_range, outlier_range, threshold=None, is_temp=False):
    if is_outlier():
        # Generate an extreme value outside the threshold
        if is_temp:
            value = random.choice(outlier_range)  # Pick either very low or very high
        else:
            value = random.uniform(*outlier_range)
    else:
        # Generate a normal value within the expected range
        value = round(random.uniform(*normal_range), 1)
    return round(value, 1)

reports = []
time_step = timedelta(seconds=30)

for gid in garden_ids:
    current_time = start_date

    while current_time <= end_date:
        report = {
            "GID": gid,
            "Time": current_time.strftime("%Y-%m-%d %H:%M:%S"),
            "Light Level (Lux)": generate_value((200, 1000), (50, 199), THRESHOLDS["Light Level (Lux)"]),
            "Humidity (%)": generate_value((40, 80), (10, 39), THRESHOLDS["Humidity (%)"]),
            "Soil Moisture (%)": generate_value((20, 50), (5, 19), THRESHOLDS["Soil Moisture (%)"]),
            "Temperature (°C)": generate_value((18, 30), (10, 35), THRESHOLDS["Temperature (°C)"], is_temp=True),
        }
        reports.append(report)
        
        # Increment by 30 seconds
        current_time += time_step

# Convert to DataFrame
df_reports = pd.DataFrame(reports)

# Save to CSV
csv_file = "Code/Report.csv"
df_reports.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Report data has been saved to {csv_file}")