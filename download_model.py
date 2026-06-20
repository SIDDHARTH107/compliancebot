from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("Downloading GPT-2 model (simpler, compatible)...")

model_id = "gpt2"

try:
    print("Downloading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    print("✅ Tokenizer downloaded\n")
    
    print("Downloading model...")
    model = AutoModelForCausalLM.from_pretrained(model_id)
    print("✅ Model downloaded\n")
    
    print("=" * 50)
    print("✅ SUCCESS! Model ready to use")
    print("=" * 50)
    
except Exception as e:
    print(f"❌ ERROR: {e}")
