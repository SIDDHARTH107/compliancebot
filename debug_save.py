import sqlite3
import json

# Test saving directly
test_data = {
    "customer_data": {
        "name": "Debug Test",
        "citizenship": "USA",
        "annual_income": 300000
    },
    "risk_score": 0.35,
    "decision": "REVIEW",
    "reasoning": ["Test reasoning"]
}

print("Attempting to save...")

try:
    conn = sqlite3.connect('compliancebot.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO kyc_decisions 
        (customer_name, citizenship, annual_income, risk_score, decision, reasoning)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        test_data["customer_data"]["name"],
        test_data["customer_data"]["citizenship"],
        test_data["customer_data"]["annual_income"],
        test_data["risk_score"],
        test_data["decision"],
        json.dumps(test_data["reasoning"])
    ))
    
    conn.commit()
    print("✅ Save successful!")
    
    # Verify
    cursor.execute('SELECT COUNT(*) FROM kyc_decisions')
    count = cursor.fetchone()[0]
    print(f"Total records now: {count}")
    
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")
