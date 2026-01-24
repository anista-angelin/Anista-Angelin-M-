import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Database setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    hashed = generate_password_hash(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, hashed)
        )
        conn.commit()
        print("✅ Registration successful\n")
    except:
        print("❌ Username already exists\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username,)
    )
    result = cursor.fetchone()

    if result and check_password_hash(result[0], password):
        print("✅ Login successful\n")
    else:
        print("❌ Invalid credentials\n")

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose option: ")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Invalid choice\n")
