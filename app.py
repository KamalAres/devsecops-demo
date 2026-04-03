import os
import sqlite3

# Hardcoded secret (vulnerability)
API_KEY = "sk_test_123456789SECRET"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

if __name__ == "__main__":
    user = input("Enter username: ")
    print(get_user(user))