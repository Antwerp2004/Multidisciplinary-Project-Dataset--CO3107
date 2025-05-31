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

# List of random cities worldwide
cities = [
    "New York, USA", "Paris, France", "Tokyo, Japan", "London, UK", "Sydney, Australia",
    "Rio de Janeiro, Brazil", "Cape Town, South Africa", "Dubai, UAE", "Moscow, Russia",
    "Singapore", "Rome, Italy", "Bangkok, Thailand", "Toronto, Canada", "Istanbul, Turkey",
    "Seoul, South Korea", "Barcelona, Spain", "Berlin, Germany", "Mexico City, Mexico"
]

# List of random garden descriptions
descriptions = [
    "A peaceful retreat filled with vibrant flowers and serene pathways.",
    "A lush green space perfect for relaxation and meditation.",
    "A hidden gem featuring rare plants and a tranquil atmosphere.",
    "An enchanted garden with a diverse collection of flora and fauna.",
    "A breathtaking paradise with cascading waterfalls and colorful blooms.",
    "A majestic garden known for its intricate landscaping and beauty.",
    "A quiet haven where nature lovers can immerse themselves in greenery.",
    "A vibrant oasis bursting with exotic flowers and tropical trees.",
    "A secret garden offering a tranquil escape from the bustling city.",
    "A charming retreat where every season brings a new burst of color."
]

# Generate gardens
gardens = []
num_gardens = 5

for i in range(1, num_gardens + 1):
    garden = {
        "GID": generate_gid(i),
        "Name": generate_garden_name(),
        "Location": random.choice(cities),
        "Description": random.choice(descriptions)
    }
    gardens.append(garden)

# Convert to DataFrame and save as CSV
df_gardens = pd.DataFrame(gardens)
csv_file = "Data/Garden.csv"
df_gardens.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Garden data has been saved to {csv_file}")