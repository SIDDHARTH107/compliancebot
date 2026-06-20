class DocumentIntakeAgent:
    def __init__(self):
        print("Document Intake Agent initialized\n")
    
    def process(self, form_data):
        """
        Extract key information from KYC form
        Input: dict with customer data
        Output: cleaned data
        """
        
        # Simple extraction
        extracted = {
            "name": form_data.get("name", "Unknown"),
            "citizenship": form_data.get("citizenship", "Unknown"),
            "annual_income": float(form_data.get("annual_income", 0)),
            "age": int(form_data.get("age", 0))
        }
        
        return extracted
    
    def validate(self, extracted_data):
        """Validate extracted data"""
        errors = []
        
        if not extracted_data["name"] or extracted_data["name"] == "Unknown":
            errors.append("Name is required")
        
        if not extracted_data["citizenship"] or extracted_data["citizenship"] == "Unknown":
            errors.append("Citizenship is required")
        
        if extracted_data["annual_income"] <= 0:
            errors.append("Annual income must be positive")
        
        return len(errors) == 0, errors

# Testing it
if __name__ == "__main__":
    agent = DocumentIntakeAgent()
    
    test_form = {
        "name": "John Smith",
        "citizenship": "USA",
        "annual_income": 250000,
        "age": 35
    }
    
    result = agent.process(test_form)
    print("Extracted:", result)
    
    valid, errors = agent.validate(result)
    print(f"Valid: {valid}")
    if errors:
        print(f"Errors: {errors}")
