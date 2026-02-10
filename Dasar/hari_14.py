# Format: { "key": value}
user_profile = {
    "username": "moyan",
    "level": "Beginner",
    "is_active": "True",
    "points": 1500
}

# 1. Mengakses data menggunakan Key
print(f"Username: {user_profile['username']}")
print(f"Status: {user_profile['is_active']}")

# 2. Menambah atau Mengubah data
user_profile["points"] = 1650
user_profile["role"] = "Backend Engineer"

# 3. Menghapus data
del user_profile["level"]
print(f"Data Terupdate: {user_profile}")