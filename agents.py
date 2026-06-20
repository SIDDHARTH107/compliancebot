from agent_document_intake import DocumentIntakeAgent
from agent_risk_score import RiskScoreAgent

class ComplianceBotAgents:
    def __init__(self):
        print("Initializing ComplianceBot Agents...\n")
        self.document_agent = DocumentIntakeAgent()
        self.risk_agent = RiskScoreAgent()
        print("✅ All agents initialized\n")
    
    def process_kyc(self, form_data):
        """
        Process KYC through both agents
        """
        
        # Agent 1: Extracting document
        print("Agent 1: Processing document...")
        extracted = self.document_agent.process(form_data)
        is_valid, errors = self.document_agent.validate(extracted)
        
        if not is_valid:
            return {
                "success": False,
                "error": f"Validation failed: {errors}"
            }
        
        print(f"✅ Extracted: {extracted}\n")
        
        # Agent 2: Calculating the risk score
        print("Agent 2: Calculating risk...")
        risk_result = self.risk_agent.calculate_risk(extracted)
        print(f"✅ Risk calculated: {risk_result['decision']}\n")
        
        # Combining the results
        final_result = {
            "success": True,
            "customer_data": extracted,
            "risk_score": risk_result["risk_score"],
            "decision": risk_result["decision"],
            "reasoning": risk_result["reasoning"]
        }
        
        return final_result

# Testing the agents
if __name__ == "__main__":
    bot = ComplianceBotAgents()
    
    test_form = {
        "name": "Jane Doe",
        "citizenship": "Canada",
        "annual_income": 150000,
        "age": 45
    }
    
    print("=" * 50)
    print("PROCESSING KYC APPLICATION")
    print("=" * 50 + "\n")
    
    result = bot.process_kyc(test_form)
    
    print("\nFINAL RESULT:")
    print(f"Status: {'✅ SUCCESS' if result['success'] else '❌ FAILED'}")
    print(f"Decision: {result['decision']}")
    print(f"Risk Score: {result['risk_score']}")
    print(f"Reasoning:")
    for reason in result['reasoning']:
        print(f"  - {reason}")
