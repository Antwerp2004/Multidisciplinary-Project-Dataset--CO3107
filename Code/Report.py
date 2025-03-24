import csv
import random
import pandas as pd
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker for generating timestamps
fake = Faker()

# Load gardens from CSV (assuming GID column exists)
gardens_df = pd.read_csv("Code/Garden.csv")
garden_ids = gardens_df["GID"].tolist()

# Start date: January 1, 2024
start_date = datetime(2024, 1, 1)
end_date = datetime.now()

reports = []
for gid in garden_ids:
    current_date = start_date

    while current_date <= end_date:
        for hour in [6, 18]:  # 6 AM and 6 PM
            report_time = current_date.replace(hour=hour, minute=0, second=0)
            report = {
                "GID": gid,
                "Time": report_time.strftime("%Y-%m-%d %H:%M:%S"),
                "Light Level (Lux)": round(random.uniform(100, 1000)),
                "Humidity (%)": round(random.uniform(30, 90), 1),
                "Soil Moisture (Arbitrary Scale)": round(random.uniform(10, 60), 1),
                "Temperature (°C)": round(random.uniform(15, 35), 1),
            }
            reports.append(report)

        # Move to the next day
        current_date += timedelta(days=1)

# Convert to DataFrame
df_reports = pd.DataFrame(reports)

# Save to CSV
csv_file = "Code/Report.csv"
df_reports.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Report data has been saved to {csv_file}")