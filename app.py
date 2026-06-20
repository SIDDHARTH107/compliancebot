import streamlit as st
import json
from agents import ComplianceBotAgents
import sqlite3

st.set_page_config(page_title="ComplianceBot", page_icon="shield", layout="wide")

@st.cache_resource
def load_agents():
    return ComplianceBotAgents()

agents = load_agents()

if 'current_result' not in st.session_state:
    st.session_state.current_result = None

def store_decision(data):
    try:
        conn = sqlite3.connect('compliancebot.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO kyc_decisions 
            (customer_name, citizenship, annual_income, risk_score, decision, reasoning)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            data["customer_data"]["name"],
            data["customer_data"]["citizenship"],
            data["customer_data"]["annual_income"],
            data["risk_score"],
            data["decision"],
            json.dumps(data["reasoning"])
        ))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Database error: {e}")
        return False

st.title("ComplianceBot - KYC System")
st.subheader("AI-Powered Compliance")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", value="John Smith")
    citizenship = st.selectbox("Citizenship", ["USA", "Canada", "UK", "Germany", "China", "India", "Syria"])
with col2:
    annual_income = st.number_input("Annual Income", value=250000, min_value=0)
    age = st.number_input("Age", value=35, min_value=18, max_value=120)

if st.button("Process KYC", use_container_width=True):
    process_data = {"name": name, "citizenship": citizenship, "annual_income": annual_income, "age": age}
    with st.spinner("Processing..."):
        result = agents.process_kyc(process_data)
    st.session_state.current_result = result

if st.session_state.current_result:
    result = st.session_state.current_result
    st.divider()
    
    if result["success"]:
        st.success("Success! Processing Complete")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Risk Score", f"{result['risk_score']:.2f}")
        with col2:
            st.metric("Decision", result["decision"])
        with col3:
            st.metric("Customer", result["customer_data"]["name"])
        
        st.subheader("Customer Details")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(f"Citizenship: {result['customer_data']['citizenship']}")
        with col2:
            income = result['customer_data']['annual_income']
            st.write(f"Annual Income: {income:,.0f}")
        with col3:
            st.write(f"Age: {result['customer_data']['age']} years")
        
        st.subheader("Agent Reasoning")
        for reason in result["reasoning"]:
            st.write(f"- {reason}")
        
        if st.button("Save to Database", use_container_width=True):
            with st.spinner("Saving..."):
                if store_decision(result):
                    st.success("SAVED! Decision stored in database")
                    st.balloons()
                    st.session_state.current_result = None
                else:
                    st.error("Failed to save")
    else:
        st.error(f"Error: {result['error']}")

st.divider()
st.caption("ComplianceBot 2024 | AI-Powered KYC System")
