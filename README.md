# 🤖 Telegram Product Poster

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-green)

**Automatically post your products from Excel to Telegram channels!**

---

## 📱 Created by Tech Mouad

- 📺 **YouTube**: [https://www.youtube.com/@techmouad](https://www.youtube.com/@techmouad)
- 📸 **Instagram**: [https://www.instagram.com/tech_mouad/](https://www.instagram.com/tech_mouad/)

*Subscribe for more automation tools! 🚀*

---

## 🎯 What It Does

**Before:** ❌ Manual posting = Hours of work  
**After:** ✅ Load Excel + Click start = Done! ☕

### Features
- 🔄 Works with ANY Excel format
- 🤖 Posts to multiple Telegram channels  
- 🛡️ Prevents duplicate posts
- 🖼️ Includes product images
- 📊 Real-time progress tracking

---

## 🚀 Quick Setup

### 1. Install Python
- Go to [python.org](https://python.org/downloads)
- Download and install
- ⚠️ **Check "Add Python to PATH"**

### 2. Download This App
- Click green "Code" button → "Download ZIP"
- Extract to Desktop

### 3. Install Requirements
Open Command Prompt/Terminal:
```bash
cd Desktop/telegram-product-poster-main
pip install -r requirements.txt
```

### 4. Test Installation
```bash
python test_installation.py
```
**Look for "🎉 SUCCESS!" message**

---

## 🤖 Setup Telegram Bot

1. **Create Bot**: Message `@BotFather` on Telegram → `/newbot`
2. **Get Token**: Save the token BotFather gives you
3. **Add to Channel**: Make your bot admin in your channel

---

## 📊 Prepare Excel File

Any Excel format works! Example:
```
| Product Name | Price | Description | Image URL | Buy Link |
| Gaming Mouse | $25   | RGB mouse   | https://... | https://... |
```

---

## ▶️ Run the App

```bash
python telegram_product_poster.py
```

### In the App:
1. **Bot Configuration**: Enter bot token and channel
2. **Products Excel**: Load your Excel file  
3. **Message Template**: Create post format using your column names
4. **Auto Posting**: Set delay (60 seconds) and start!

### Template Example:
```
🛍️ {Product Name}
💰 {Price}
📝 {Description}
🛒 {Buy Link}
```

---

## ❓ Common Issues

**"Python not found"** → Reinstall with "Add to PATH" checked  
**"Bot can't post"** → Make sure bot is admin in channel  
**"Invalid token"** → Get fresh token from @BotFather  
**Excel won't load** → Save as .xlsx with column headers

---

## 📁 Project Files

```
telegram-product-poster/
├── telegram_product_poster.py  ← Main app
├── test_installation.py        ← Check setup
├── requirements.txt             ← Dependencies
└── README.md                   ← This guide
```

---

## 🎬 Video Tutorial

**Watch setup tutorial on [@techmouad](https://www.youtube.com/@techmouad) YouTube!**

---

## 🔒 Security

- Keep bot token private
- Don't post faster than 30 seconds
- Test with few products first

---

**Made with ❤️ by Tech Mouad**  
📺 [YouTube](https://www.youtube.com/@techmouad) | 📸 [Instagram](https://www.instagram.com/tech_mouad/)
