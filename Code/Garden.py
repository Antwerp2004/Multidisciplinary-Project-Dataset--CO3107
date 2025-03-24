import csv
import random
import numpy as np
import pandas as pd

# Garden ID
def generate_gid(index):
    return f"GAR{index:04d}"

# Garden Name
def generate_garden_name():
    adjectives = ["Green", "Sunny", "Hidden", "Tranquil", "Secret", "Enchanted", "Wild", "Blooming", 
                  "Lush", "Majestic", "Serene", "Whispering", "Golden", "Peaceful", "Sacred"]
    nouns = ["Garden", "Oasis", "Haven", "Retreat", "Meadow", "Sanctuary", "Grove", "Paradise", "Park"]
    # Choose the number of adjectives (1 to 3) using exponential distribution
    num_adjectives = min(3, max(1, np.random.geometric(0.5)))  # Bias towards shorter names
    selected_adjectives = random.sample(adjectives, num_adjectives)  # Pick adjectives
    noun = random.choice(nouns)  # Pick noun
    return " ".join(selected_adjectives) + " " + noun  # Combine and return

# Generate gardens
gardens = []
num_gardens = 300

for i in range(1, num_gardens + 1):
    garden = {
        "GID": generate_gid(i),
        "Name": generate_garden_name(),
    }
    gardens.append(garden)

# Convert to DataFrame and save as CSV
df_gardens = pd.DataFrame(gardens)
csv_file = "Code/Garden.csv"
df_gardens.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Garden data has been saved to {csv_file}")