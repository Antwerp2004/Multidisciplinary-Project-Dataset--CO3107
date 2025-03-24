import pandas as pd
from datetime import datetime, timedelta

# Load the report data
df_reports = pd.read_csv("Code/Report.csv")

# Define threshold conditions for triggering changes
THRESHOLDS = {
    "Light Level (Lux)": 200,  # Turn on Grow Lights if below this
    "Humidity (%)": 40,  # Turn on Humidifier if below this
    "Soil Moisture (Arbitrary Scale)": 20,  # Water if below this
    "Temperature (°C)": {"low": 18, "high": 30},  # Heating <18°C, Cooling >30°C
}

# Define time offsets for each category
TIME_OFFSETS = {
    "Lighting": 5,      # +5 sec
    "Humidity": 10,     # +10 sec
    "Watering": 15,     # +15 sec
    "Heating": 20,      # +20 sec
    "Cooling": 25,      # +25 sec
}

# List to store change logs
change_logs = []

# Iterate through each report entry
for _, row in df_reports.iterrows():
    gid = row["GID"]
    base_time = datetime.strptime(row["Time"], "%Y-%m-%d %H:%M:%S")

    # Check conditions and log necessary changes
    if row["Light Level (Lux)"] < THRESHOLDS["Light Level (Lux)"]:
        time_offset = base_time + timedelta(seconds=TIME_OFFSETS["Lighting"])
        change_logs.append([gid, time_offset.strftime("%Y-%m-%d %H:%M:%S"), "Lighting", "Turned on grow lights"])

    if row["Humidity (%)"] < THRESHOLDS["Humidity (%)"]:
        time_offset = base_time + timedelta(seconds=TIME_OFFSETS["Humidity"])
        change_logs.append([gid, time_offset.strftime("%Y-%m-%d %H:%M:%S"), "Humidity", "Activated humidifier"])

    if row["Soil Moisture (Arbitrary Scale)"] < THRESHOLDS["Soil Moisture (Arbitrary Scale)"]:
        time_offset = base_time + timedelta(seconds=TIME_OFFSETS["Watering"])
        change_logs.append([gid, time_offset.strftime("%Y-%m-%d %H:%M:%S"), "Watering", "Watered the soil"])

    if row["Temperature (°C)"] < THRESHOLDS["Temperature (°C)"]["low"]:
        time_offset = base_time + timedelta(seconds=TIME_OFFSETS["Heating"])
        change_logs.append([gid, time_offset.strftime("%Y-%m-%d %H:%M:%S"), "Heating", "Turned on heater"])

    if row["Temperature (°C)"] > THRESHOLDS["Temperature (°C)"]["high"]:
        time_offset = base_time + timedelta(seconds=TIME_OFFSETS["Cooling"])
        change_logs.append([gid, time_offset.strftime("%Y-%m-%d %H:%M:%S"), "Cooling", "Turned on cooling system"])

# Convert to DataFrame
df_changelog = pd.DataFrame(change_logs, columns=["GID", "Time", "Category", "Description"])

# Save to CSV
csv_file = "Code/ChangeLog.csv"
df_changelog.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Change logs have been saved to {csv_file}")