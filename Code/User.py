import csv
import bcrypt
import random
import string
import pandas as pd

# Function to generate a random username
def generate_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

# Function to generate a secure random password
def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=10))

# Function to hash password using bcrypt
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

# Tạo dữ liệu cho từng loại trang
def generate_page_data(num_users):
    users = []
    for i in range (1, num_users + 1):
        user = {
            "Username": generate_username(),
            "Password": hash_password(generate_password()),
        }
        users.append(user)
    return users

# Generate user data
num_users = 10  # Number of users to generate

# Chuyển thành DataFrame
df = pd.DataFrame(generate_page_data(num_users))

# Xuất ra file CSV (MySQL-friendly format)
csv_file = "User.csv"
df.to_csv(csv_file, index=False, encoding="utf-8-sig")

print(f"Data has been saved to {csv_file}")