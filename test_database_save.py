import sqlite3
import json
from agents import ComplianceBotAgents

# Test data
test_form = {
    "name": "Test User",
    "citizenship": "USA",
    "annual_income": 250000,
    "age": 35
}

# Process through agents
agents = ComplianceBotAgents()
result = agents.process_kyc(test_form)

print("Result:", result)
print()

# Try to save to database
if result["success"]:
    try:
        conn = sqlite3.connect('compliancebot.db')
        cursor = conn.cursor()
        
        print("Inserting into database...")
        cursor.execute('''
            INSERT INTO kyc_decisions 
            (customer_name, citizenship, annual_income, risk_score, decision, reasoning)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            result["customer_data"]["name"],
            result["customer_data"]["citizenship"],
            result["customer_data"]["annual_income"],
            result["risk_score"],
            result["decision"],
            json.dumps(result["reasoning"])
        ))
        
        conn.commit()
        
        # Verify
        cursor.execute('SELECT * FROM kyc_decisions')
        rows = cursor.fetchall()
        print(f"✅ Success! Records in database: {len(rows)}")
        print(f"Latest record: {rows[-1] if rows else 'None'}")
        
        conn.close()
    except Exception as e:
        print(f"❌ Error: {e}")
