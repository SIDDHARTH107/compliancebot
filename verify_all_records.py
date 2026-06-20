import sqlite3

# Connect to database
conn = sqlite3.connect('compliancebot.db')
cursor = conn.cursor()

# Get all records
cursor.execute('SELECT * FROM kyc_decisions')
rows = cursor.fetchall()

print("=" * 80)
print("ALL RECORDS IN DATABASE")
print("=" * 80)
print()

if rows:
    print(f"Total records: {len(rows)}\n")
    
    for i, row in enumerate(rows, 1):
        print(f"Record {i}:")
        print(f"  ID: {row[0]}")
        print(f"  Name: {row[1]}")
        print(f"  Citizenship: {row[2]}")
        income = row[3]
        print(f"  Annual Income: ")
        print(f"  Risk Score: {row[4]}")
        print(f"  Decision: {row[5]}")
        print(f"  Saved at: {row[7]}")
        print()
else:
    print("No records found in database!")

conn.close()

print("=" * 80)
