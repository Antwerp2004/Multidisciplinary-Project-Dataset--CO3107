import pandas as pd
from datetime import datetime, timedelta
import random

# Load necessary files
df_changelog = pd.read_csv("Code/ChangeLog.csv")
df_has = pd.read_csv("Code/has.csv")  # Links Users to Gardens

# Create a dictionary mapping GID to list of Users managing it
garden_users = df_has.groupby("GID")["Username"].apply(list).to_dict()

# Define warning messages based on category
WARNING_MESSAGES = {
    "Lighting": "Lighting system in Garden {GID} is malfunctioning.",
    "Humidity": "Humidity in Garden {GID} is critically low/high.",
    "Watering": "Watering system in Garden {GID} failed to activate.",
    "Heating": "Heating system in Garden {GID} is malfunctioning.",
    "Cooling": "Cooling system in Garden {GID} is not operating correctly.",
}

# List to store warnings
warnings = []

# Generate warnings based on ChangeLog issues
for _, row in df_changelog.iterrows():
    gid = row["GID"]
    time_created = datetime.strptime(row["Time"], "%Y-%m-%d %H:%M:%S") + timedelta(seconds=30)  # Warning issued 30 sec after event
    category = row["Category"]

    if category in WARNING_MESSAGES:
        # Choose a random user managing this garden
        if gid in garden_users:
            username = random.choice(garden_users[gid])
            description = WARNING_MESSAGES[category].format(GID=gid)

            # Append warning entry
            warnings.append([username, time_created.strftime("%Y-%m-%d %H:%M:%S"), description])

# Convert to DataFrame
df_warnings = pd.DataFrame(warnings, columns=["Username", "Time_created", "Description"])

# Save to CSV
csv_file = "Code/Warnings.csv"
df_warnings.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Warnings have been saved to {csv_file}")