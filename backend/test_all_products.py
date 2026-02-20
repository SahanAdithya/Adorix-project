from product_qa_engine import ProductQAEngine

engine = ProductQAEngine()

products = [
    "10-15_female",
    "10-15_male", 
    "16-29_female",
    "16-29_male",
    "30-39_female",
    "30-39_male",
    "40-49_female",
    "40-49_male",
    "50-59_female",
    "50-59_male",
    "above-60_female",
    "above-60_male"
]

print("\n" + "="*70)
print("TESTING ALL PRODUCTS")
print("="*70)

for product in products:
    answer = engine.get_answer("What is the price?", product)
    print(f"\n✓ {product}")
    print(f"  Answer: {answer[:100]}...")
