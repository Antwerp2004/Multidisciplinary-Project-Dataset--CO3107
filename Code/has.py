import csv
import random
import numpy as np
import pandas as pd

# Load users and gardens
user_df = pd.read_csv("Code/User.csv")
usernames = user_df["Username"].tolist()

gardens_df = pd.read_csv("Code/Garden.csv")
gardens = gardens_df["GID"].tolist()

relations = []

for gid in gardens:
    # Assign 1-5 users to each garden (exponential distribution)
    num_users = min(5, max(1, np.random.geometric(0.75)))  # Bias towards smaller numbers
    assigned_users = random.sample(usernames, num_users)

    # Save each (Garden, User) pair
    for user in assigned_users:
        relation = {
            "GID": gid,
            "Username": user
        }
        relations.append(relation)

# Convert to DataFrame and save as CSV
df_relations = pd.DataFrame(relations)
csv_file = "Code/has.csv"
df_relations.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Relation data has been saved to {csv_file}")