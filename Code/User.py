import csv
import bcrypt
import random
import string
import pandas as pd

# Function to generate a random username
def generate_username(index):
    return f"USER{index:04d}"

# Function to generate a secure random password
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=10))

# Function to hash password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

# Create data for each user
def generate_user_data(num_users):
    users = []
    for i in range (1, num_users + 1):
        user = {
            "Username": generate_username(i),
            "Password": hash_password(generate_password()),
        }
        users.append(user)
    return users

# Generate user data
num_users = 100  # Number of users to generate

# Convert to DataFrame
df = pd.DataFrame(generate_user_data(num_users))

# Extract to CSV (MySQL-friendly format)
csv_file = "Code/User.csv"
df.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"User data has been saved to {csv_file}")