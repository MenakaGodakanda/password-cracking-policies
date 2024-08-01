# password_hashes.py
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

passwords = [
    "password",
    "123456",
    "qwerty",
    "password123",
    "admin",
    "letmein",
    "welcome",
    "monkey",
    "dragon",
    "iloveyou"
]

with open('password-list.txt', 'w') as f:
    for password in passwords:
        f.write(f"{password}\n")

with open('hashed-passwords.txt', 'w') as f:
    for password in passwords:
        hashed_password = hash_password(password)
        f.write(f"{hashed_password}\n")
    print("Password hashes generated and saved to hashed-passwords.txt")
