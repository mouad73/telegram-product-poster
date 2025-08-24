"""
🛍️ Telegram Product Poster - Sample Excel Template Creator
👨‍💻 Created by: Tech Mouad
📺 YouTube: https://www.youtube.com/@techmouad
📸 Instagram: https://www.instagram.com/tech_mouad/

This helper script creates a sample Excel template to help users understand
the expected format for the Telegram Product Poster application.

Usage: python create_sample_template.py
"""

import pandas as pd
import os

# Create a comprehensive sample Excel template for users
sample_data = {
    "ProductId": ["PROD001", "PROD002", "PROD003", "PROD004", "PROD005"],
    "Product Name": [
        "Wireless Bluetooth Headphones", 
        "Gaming Mechanical Keyboard", 
        "USB-C Fast Charger",
        "Smartphone Case",
        "Wireless Mouse"
    ],
    "Description": [
        "High-quality wireless headphones with noise cancellation and 30-hour battery life",
        "RGB backlit mechanical keyboard perfect for gaming with customizable keys",
        "Fast charging USB-C cable compatible with all devices - 3ft length",
        "Durable protective case with shock absorption and wireless charging support",
        "Ergonomic wireless mouse with precision tracking and long battery life"
    ],
    "Price": ["$79.99", "$129.99", "$24.99", "$34.99", "$49.99"],
    "Original Price": ["$99.99", "$149.99", "$34.99", "$44.99", "$59.99"],
    "Discount": ["20%", "13%", "29%", "23%", "17%"],
    "Currency": ["USD", "USD", "USD", "USD", "USD"],
    "Category": ["Electronics", "Gaming", "Accessories", "Phone Cases", "Computer Accessories"],
    "Image URL": [
        "https://example.com/headphones.jpg",
        "https://example.com/keyboard.jpg", 
        "https://example.com/charger.jpg",
        "https://example.com/phone-case.jpg",
        "https://example.com/mouse.jpg"
    ],
    "Product URL": [
        "https://example.com/headphones",
        "https://example.com/keyboard",
        "https://example.com/charger",
        "https://example.com/phone-case",
        "https://example.com/mouse"
    ],
    "Stock Status": ["In Stock", "Limited Stock", "In Stock", "Low Stock", "In Stock"],
    "Rating": ["4.8/5", "4.9/5", "4.7/5", "4.6/5", "4.8/5"],
    "Brand": ["AudioTech", "GamerPro", "ChargeMax", "ProtectPlus", "ClickMaster"],
    "Posted Status": ["", "", "", "", ""]  # Will be filled by the app
}

def create_template():
    """Create the sample Excel template"""
    try:
        # Create DataFrame
        df = pd.DataFrame(sample_data)
        
        # Save to Excel with formatting
        filename = "sample_products_template.xlsx"
        df.to_excel(filename, index=False)
        
        # Display success message
        print("="*60)
        print("🛍️ TELEGRAM PRODUCT POSTER - SAMPLE TEMPLATE CREATOR")
        print("👨‍💻 Created by: Tech Mouad")
        print("📺 YouTube: https://www.youtube.com/@techmouad")
        print("="*60)
        print(f"✅ Sample Excel template created successfully!")
        print(f"📁 File saved as: {filename}")
        print(f"📊 Total products: {len(df)}")
        print(f"� Columns included: {len(df.columns)}")
        print()
        print("� COLUMN STRUCTURE:")
        for i, col in enumerate(df.columns, 1):
            print(f"   {i:2d}. {col}")
        print()
        print("💡 HOW TO USE:")
        print("   1. Open the generated Excel file")
        print("   2. Replace sample data with your real products")
        print("   3. Add/remove columns as needed")
        print("   4. Load the file in Telegram Product Poster app")
        print()
        print("🎯 TIPS:")
        print("   • Keep 'Product Name' and 'Description' columns")
        print("   • Image URL should link to valid image files")
        print("   • Product URL should be your affiliate/product links")
        print("   • The app works with ANY column structure!")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating template: {e}")
        return False

if __name__ == "__main__":
    create_template()
