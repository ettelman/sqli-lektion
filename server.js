const express = require('express');
const mysql = require('mysql2');
const app = express();

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'test'
});

db.connect();

app.get('/', (req, res) => {
  res.send(`<form action="/login">
              Username: <input name="username"><br>
              Password: <input name="password"><br>
              <input type="submit">
            </form>`);
});

app.get('/login', (req, res) => {
  const username = req.query.username;
  const password = req.query.password;

  // sqli
  const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;
  // const query = "SELECT * FROM users WHERE username = ? AND password = ?";
  // db.query(query, [username, password], (err, results) => {
  db.query(query, (err, results) => {
    if (err) throw err;
    if (results.length > 0) {
      res.send(`Welcome ${results[0].username}`);
    } else {
      res.send('Login failed');
    }
  });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));

