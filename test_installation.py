#!/usr/bin/env python3
"""
🛍️ Telegram Product Poster - Installation Test Script
👨‍💻 Created by: Tech Mouad
📺 YouTube: https://www.youtube.com/@techmouad
📸 Instagram: https://www.instagram.com/tech_mouad/

Run this script to verify all dependencies are properly installed
before using the Telegram Product Poster app.

Usage: python test_installation.py
"""

import sys
import importlib
import platform

def test_python_version():
    """Test Python version compatibility"""
    version = sys.version_info
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python 3.7+ required. Please upgrade Python.")
        return False

def test_dependencies():
    """Test if all required packages are installed"""
    dependencies = {
        'pandas': 'Excel file processing',
        'requests': 'Telegram API communication', 
        'openpyxl': 'Excel file support',
        'tkinter': 'GUI interface (built-in)'
    }
    
    print("\n📦 Testing Dependencies:")
    print("-" * 40)
    
    all_good = True
    
    for package, description in dependencies.items():
        try:
            if package == 'tkinter':
                # Special case for tkinter (different import name)
                import tkinter
            else:
                importlib.import_module(package)
            print(f"✅ {package:<12} - {description}")
        except ImportError:
            print(f"❌ {package:<12} - {description} (MISSING)")
            all_good = False
    
    return all_good

def test_file_structure():
    """Test if all required files are present"""
    import os
    
    required_files = [
        'telegram_product_poster.py',
        'requirements.txt',
        'README.md',
        'LICENSE'
    ]
    
    print("\n📁 Testing File Structure:")
    print("-" * 40)
    
    all_present = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} (MISSING)")
            all_present = False
    
    return all_present

def main():
    """Run all tests"""
    print("🔍 Telegram Product Poster - Installation Test")
    print("👨‍💻 Created by: Tech Mouad")
    print("📺 YouTube: https://www.youtube.com/@techmouad")
    print("=" * 50)
    
    # System info
    print(f"💻 System: {platform.system()} {platform.release()}")
    
    # Run tests
    python_ok = test_python_version()
    deps_ok = test_dependencies()
    files_ok = test_file_structure()
    
    # Final result
    print("\n" + "=" * 50)
    
    if python_ok and deps_ok and files_ok:
        print("🎉 SUCCESS! Everything is ready to go!")
        print("\n🚀 You can now run: python telegram_product_poster.py")
        print("💡 Follow the README.md for complete setup instructions!")
    else:
        print("❌ ISSUES FOUND! Please fix the problems above.")
        
        if not deps_ok:
            print("\n💡 To install missing packages, run:")
            print("   pip install -r requirements.txt")
        
        if not files_ok:
            print("\n💡 Make sure you have all required files in the project folder.")
    
    print("\n📚 For help and tutorials:")
    print("   📺 YouTube: https://www.youtube.com/@techmouad")
    print("   📸 Instagram: https://www.instagram.com/tech_mouad/")
    print("   📖 README: Check README.md for detailed instructions")

if __name__ == "__main__":
    main()
