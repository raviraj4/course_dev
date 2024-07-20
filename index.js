const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
const port = 5000;

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: '1000xdev',
  password: 'pg123',
  port: 5432,
});

app.use(cors());

app.get('/colleges', async (req, res) => {
  try {
    const { rows } = await pool.query('SELECT * FROM colleges');
    res.json(rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
