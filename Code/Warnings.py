import pandas as pd
from datetime import datetime, timedelta
import random

# Load necessary files
df_changelog = pd.read_csv("Code/ChangeLog.csv")
df_has = pd.read_csv("Code/has.csv")  # Links Users to Gardens

# Create a dictionary mapping GID to list of Users managing it
garden_users = df_has.groupby("GID")["Username"].apply(list).to_dict()

# Define two warning messages per category
WARNING_MESSAGES = {
    "Lighting": [
        "Lighting system in Garden {GID} is malfunctioning.",
        "Garden {GID} is experiencing abnormal light fluctuations."
    ],
    "Humidity": [
        "Humidity in Garden {GID} is critically low/high.",
        "Unexpected humidity changes detected in Garden {GID}."
    ],
    "Watering": [
        "Watering system in Garden {GID} failed to activate.",
        "Garden {GID} irrigation system detected an issue."
    ],
    "Heating": [
        "Heating system in Garden {GID} is malfunctioning.",
        "Temperature regulation failure detected in Garden {GID}."
    ],
    "Cooling": [
        "Cooling system in Garden {GID} is not operating correctly.",
        "Garden {GID} cooling system is underperforming."
    ],
}

# List to store warnings
warnings = []

# Process ChangeLog entries
for _, row in df_changelog.iterrows():
    if random.random() <= 0.1:  # 10% chance to raise a warning
        gid = row["GID"]
        time_created = datetime.strptime(row["Time"], "%Y-%m-%d %H:%M:%S") + timedelta(seconds=30)
        category = row["Category"]

        if category in WARNING_MESSAGES and gid in garden_users:
            description = random.choice(WARNING_MESSAGES[category]).format(GID=gid)
            
            # Send warning to all users managing the garden
            for username in garden_users[gid]:
                warnings.append([username, time_created.strftime("%Y-%m-%d %H:%M:%S"), description])

# Convert to DataFrame
df_warnings = pd.DataFrame(warnings, columns=["Username", "Time_created", "Description"])

# Save to CSV
csv_file = "Code/Warnings.csv"
df_warnings.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Warnings have been saved to {csv_file}")