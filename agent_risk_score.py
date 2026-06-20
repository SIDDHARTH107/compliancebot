class RiskScoreAgent:
    def __init__(self):
        print("Risk Score Agent initialized\n")
    
    def calculate_risk(self, customer_data):
        """
        Calculate risk score based on customer data
        Returns: risk_score (0.0-1.0), decision, reasoning
        """
        
        risk_score = 0.5  # Starting at medium
        reasoning = []
        
        # Factor 1: Income level
        if customer_data["annual_income"] > 500000:
            risk_score -= 0.2
            reasoning.append("High income: Lower risk (-0.2)")
        elif customer_data["annual_income"] > 100000:
            risk_score -= 0.1
            reasoning.append("Moderate income: Lower risk (-0.1)")
        else:
            risk_score += 0.1
            reasoning.append("Low income: Higher risk (+0.1)")
        
        # Factor 2: Citizenship (high-risk countries)
        high_risk_countries = ["Syria", "North Korea", "Iran", "Cuba"]
        if customer_data["citizenship"] in high_risk_countries:
            risk_score += 0.4
            reasoning.append(f"High-risk country ({customer_data['citizenship']}): Higher risk (+0.4)")
        elif customer_data["citizenship"] in ["USA", "Canada", "UK", "Germany"]:
            risk_score -= 0.1
            reasoning.append(f"Low-risk country ({customer_data['citizenship']}): Lower risk (-0.1)")
        else:
            reasoning.append(f"Medium-risk country ({customer_data['citizenship']}): Neutral")
        
        # Factor 3: Age
        if customer_data["age"] < 25:
            risk_score += 0.1
            reasoning.append("Young age: Slightly higher risk (+0.1)")
        elif customer_data["age"] > 70:
            risk_score += 0.05
            reasoning.append("Advanced age: Slightly higher risk (+0.05)")
        
        # Clamp between 0.0 and 1.0
        risk_score = max(0.0, min(1.0, risk_score))
        
        # Determining decision
        if risk_score < 0.3:
            decision = "APPROVE"
        elif risk_score < 0.7:
            decision = "REVIEW"
        else:
            decision = "REJECT"
        
        return {
            "risk_score": round(risk_score, 2),
            "decision": decision,
            "reasoning": reasoning
        }

# Testing it
if __name__ == "__main__":
    agent = RiskScoreAgent()
    
    test_customer = {
        "name": "John Smith",
        "citizenship": "USA",
        "annual_income": 250000,
        "age": 35
    }
    
    result = agent.calculate_risk(test_customer)
    print("Risk Result:")
    print(f"  Score: {result['risk_score']}")
    print(f"  Decision: {result['decision']}")
    print(f"  Reasoning:")
    for reason in result['reasoning']:
        print(f"    - {reason}")
