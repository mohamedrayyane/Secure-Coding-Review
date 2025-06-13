# fixed_code.py

from flask import Flask, request, session
import sqlite3
import bcrypt

app = Flask(__name__)
app.secret_key = 'very_secret_key'

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

    return "User registered successfully."

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password, result[0]):
        session['user'] = username
        return "Welcome, {}".format(username)
    else:
        return "Invalid credentials", 401

if __name__ == "__main__":
    app.run(debug=False)
