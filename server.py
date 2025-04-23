from flask import Flask, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Setup för sqlite
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")
conn.commit()

@app.route('/')
def index():
    return '''<form action="/login">
                Username: <input name="username"><br>
                Password: <input name="password"><br>
                <input type="submit">
              </form>'''

#
@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # SQLi
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    # query = "SELECT * FROM users WHERE username = ? AND password = ?"
    # result = cursor.execute(query, (username, password)).fetchone()
    result = cursor.execute(query).fetchone()

    if result:
        return f"Welcome {result[1]}!"
    return "Login failed"

if __name__ == '__main__':
    app.run(debug=True)



