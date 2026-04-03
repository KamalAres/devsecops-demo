import os
import subprocess
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 1. Command Injection
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    result = os.system("ping -c 1 " + ip)  # ❌ vulnerable
    return str(result)

# 2. SQL Injection
@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE id = " + user_id  # ❌ vulnerable
    cursor.execute(query)
    
    return str(cursor.fetchall())

# 3. Hardcoded Secret
SECRET_KEY = "supersecretpassword"  # ❌ vulnerable

# 4. Insecure Deserialization
import pickle

@app.route('/load')
def load_data():
    data = request.args.get('data')
    obj = pickle.loads(data.encode())  # ❌ vulnerable
    return str(obj)

# 5. Path Traversal
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    with open("/var/www/files/" + filename, "r") as f:  # ❌ vulnerable
        return f.read()

# 6. Unsafe subprocess usage
@app.route('/run')
def run_cmd():
    cmd = request.args.get('cmd')
    output = subprocess.check_output(cmd, shell=True)  # ❌ vulnerable
    return output

if __name__ == '__main__':
    app.run(debug=True)  # ❌ debug mode enabled