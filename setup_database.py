import sqlite3
import os

# Create database
conn = sqlite3.connect('compliancebot.db')
cursor = conn.cursor()

# Create decisions table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS kyc_decisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        citizenship TEXT,
        annual_income REAL,
        risk_score REAL,
        decision TEXT,
        reasoning TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

print("✅ SQLite database created: compliancebot.db")
