import pandas as pd

# Create a sample Excel template for users
sample_data = {
    "ProductId": ["PROD001", "PROD002", "PROD003"],
    "Product Name": ["Wireless Bluetooth Headphones", "Gaming Mechanical Keyboard", "USB-C Fast Charger"],
    "Description": [
        "High-quality wireless headphones with noise cancellation",
        "RGB backlit mechanical keyboard perfect for gaming",
        "Fast charging USB-C cable compatible with all devices"
    ],
    "Price": ["$79.99", "$129.99", "$24.99"],
    "Original Price": ["$99.99", "$149.99", "$34.99"],
    "Discount": ["20%", "13%", "29%"],
    "Category": ["Electronics", "Gaming", "Accessories"],
    "Image URL": [
        "https://example.com/headphones.jpg",
        "https://example.com/keyboard.jpg", 
        "https://example.com/charger.jpg"
    ],
    "Product URL": [
        "https://example.com/headphones",
        "https://example.com/keyboard",
        "https://example.com/charger"
    ],
    "Stock": ["In Stock", "Limited Stock", "In Stock"],
    "Rating": ["4.8/5", "4.9/5", "4.7/5"]
}

# Create DataFrame
df = pd.DataFrame(sample_data)

# Save to Excel
df.to_excel("sample_products_template.xlsx", index=False)

print("✅ Sample Excel template created!")
print(f"📁 File saved as: sample_products_template.xlsx")
print(f"📊 Columns: {list(df.columns)}")
print("\n💡 This template shows you how to structure your Excel file.")
print("   You can add, remove, or rename columns as needed.")
print("   The app will automatically detect your column structure!")
