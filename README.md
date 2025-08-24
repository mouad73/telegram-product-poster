# 🤖 Telegram Product Poster - Automate Your Product Posts!

![Pyt## 🔧 STEP 3: Install App Requirements

1. **Open Command Prompt** (Windows+R, type `cmd`) or **Terminal** (Mac)
2. **Go to app folder:**
   ```
   cd Desktop/telegram-product-poster-main
   ```
3. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
   *Wait 2-3 minutes for installation*

### 🧪 Test Your Installation (Recommended!)

Before proceeding, verify everything is working:
```
python test_installation.py
```

This will check:
- ✅ Python version is correct
- ✅ All required packages are installed  
- ✅ All necessary files are present
- ✅ System compatibility

**If you see "🎉 SUCCESS!" - you're ready to go!**  
**If you see "❌ ISSUES FOUND" - follow the suggestions to fix them.**

---mg.shields.io/badge/Python-3.7%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![Beginner Friendly](https://img.shields.io/badge/Beginner-Friendly-green)

**🎯 Automatically post your products from Excel to Telegram channels - No programming knowledge required!**

---

## 📱 Follow Tech Mouad

**👨‍💻 Created by: Tech Mouad**
- 📺 **YouTube**: [https://www.youtube.com/@techmouad](https://www.youtube.com/@techmouad)
- 📸 **Instagram**: [https://www.instagram.com/tech_mouad/](https://www.instagram.com/tech_mouad/)

*Subscribe for more amazing automation tools! 🚀*

---

## 🌟 What This App Does

Transform hours of manual work into 5 minutes of automated posting!

**Before:** ❌ Copy & paste each product manually = Hours of work  
**After:** ✅ Load Excel file + Click start = Automatic posting while you relax! ☕

### ✨ Key Features
- 🔄 **Works with ANY Excel format** - No need to change your existing files!
- 🤖 **Smart Telegram Bot** - Posts to multiple channels automatically
- 🛡️ **No Duplicates** - Remembers what you've posted before
- 🖼️ **Images Included** - Automatically posts product images
- 📊 **Live Progress** - Watch your products being posted in real-time
- 💾 **Saves Settings** - Remembers everything for next time

---

## 🛠️ STEP 1: Install Python (One-time setup)

### Windows Users:
1. Go to [python.org/downloads](https://python.org/downloads)
2. Click "Download Python" (big yellow button)
3. Run the installer
4. ⚠️ **IMPORTANT**: Check "Add Python to PATH" box
5. Click "Install Now"

### Mac Users:
1. Go to [python.org/downloads](https://python.org/downloads)
2. Download Mac installer
3. Run and follow instructions

**Test it worked:**
- Press Windows+R, type `cmd`, press Enter (Windows)
- Type `python --version` and press Enter
- You should see "Python 3.x.x"

---

## 📥 STEP 2: Download This App

1. **Click the green "Code" button above**
2. **Click "Download ZIP"**
3. **Extract to your Desktop**

---

## � STEP 3: Install App Requirements

1. **Open Command Prompt** (Windows+R, type `cmd`) or **Terminal** (Mac)
2. **Go to app folder:**
   ```
   cd Desktop/telegram-product-poster-main
   ```
3. **Install requirements:**
   ```
   pip install -r requirements.txt
   ```
   *Wait 2-3 minutes for installation*

---

## 🤖 STEP 4: Create Your Telegram Bot

### Create the Bot:
1. **Open Telegram**, search for `@BotFather`
2. **Send:** `/newbot`
3. **Bot name:** `My Product Poster`
4. **Username:** `yourname_productbot` (must end with 'bot')
5. **Save the token** BotFather gives you (looks like: `123456789:ABC-DEF...`)

### Add Bot to Your Channel:
1. **Go to your Telegram channel**
2. **Channel Settings → Administrators → Add Admin**
3. **Search for your bot** and add it
4. **Give permission** to "Post Messages"

---

## 📊 STEP 5: Prepare Your Excel File

**Good news:** Your Excel file can have ANY format! The app adapts to your columns.

### Example formats that work:
```
| Product | Price | Description | Link | Image |
| Name | Cost | Details | URL | Photo |
| Item | Amount | Info | Website | Picture |
```

**Any column names work!** The app automatically detects your structure.

### Sample Excel structure:
```
| Product Name | Description | Price | Image URL | Buy Link |
| Gaming Mouse | Wireless RGB mouse | $25.99 | https://... | https://... |
| Keyboard | Mechanical keyboard | $89.99 | https://... | https://... |
```

---

## 🚀 STEP 6: Run the App

**In Command Prompt/Terminal, type:**
```
python telegram_product_poster.py
```

A window will open - don't worry if it looks technical, we'll guide you! 😊

---

## ⚙️ STEP 7: Set Up the App (Easy!)

### Tab 1: "Bot Configuration"
1. **Paste your bot token** (from BotFather)
2. **Add your channel** (like `@yourchannel`)
3. **Click "Test Bot Connection"** - should say "Success!"
4. **Click "Save Configuration"**

### Tab 2: "Products Excel"  
1. **Click "Browse"** and select your Excel file
2. **Click "Load Excel Data"**
3. **Click "Show Column Helper"** to see your columns

### Tab 3: "Message Template"
Create your post template using your Excel column names:
```
🛍️ {Product Name}

📝 {Description}

💰 Price: {Price}
🛒 {Buy Link}

#products #deals
```

### Tab 4: "Auto Posting"
1. **Set delay:** 60 seconds (recommended)
2. **Click "Start Posting"**
3. **Watch the magic happen!** ✨

---

## ❓ Common Issues & Quick Fixes

### "Python not found"
**Fix:** Reinstall Python with "Add to PATH" checked

### "Bot can't post"  
**Fix:** Make sure bot is admin in your channel

### "Invalid token"
**Fix:** Get a fresh token from @BotFather

### Excel won't load
**Fix:** Save as .xlsx format, make sure first row has column names

---

## 🎯 Pro Tips for Success

1. **Start small** - Test with 2-3 products first
2. **Good images** - Make sure image URLs work
3. **Don't rush** - Keep 30-60 second delays
4. **Check posts** - Monitor your channel quality
5. **Save time** - Let the app work while you focus on other things!

---

## 📁 What You'll Have

After setup, your folder contains:
```
📁 telegram-product-poster/
├── telegram_product_poster.py  ← Main app (double-click to run)
├── test_installation.py        ← Test if everything works
├── config.json                 ← Your settings (auto-created)
├── requirements.txt             ← App dependencies  
└── README.md                   ← This guide
```

**That's it!** Simple and clean - only 5 files needed! 🎉

---

## 🔒 Important Notes

- **Keep your bot token private** (like a password)
- **Respect Telegram limits** (don't post too fast)
- **Test before bulk posting** (start with few products)
- **Your Excel stays private** (app works offline)

---

## 🎬 Video Tutorial

**Watch the complete setup on [@techmouad](https://www.youtube.com/@techmouad) YouTube channel!**

🔔 Subscribe and turn on notifications for more automation tools!

---

## 💪 Why This Saves You Time

**Manual posting 100 products:**
- ⏰ Time: 3-4 hours
- 😴 Boring: Copy, paste, copy, paste...
- 😰 Errors: Easy to make mistakes

**With this app:**
- ⏰ Time: 5 minutes setup + automatic posting
- 😎 Easy: Load Excel, click start, done!
- ✅ Perfect: No human errors

**Your time is valuable - let automation do the work!** 🚀

---

## 📞 Need Help?

1. **Watch Tech Mouad's videos** for visual guides
2. **Check your setup** step by step
3. **Follow on social media** for tips and updates

---

**Made with ❤️ by Tech Mouad**

📺 [YouTube @techmouad](https://www.youtube.com/@techmouad) | 📸 [Instagram @tech_mouad](https://www.instagram.com/tech_mouad/)

*Your success is my goal! 🎯*

## ✨ Features

- 🔄 **Universal Excel Support** - Works with any Excel file structure using original column headers
- 🤖 **Telegram Bot Integration** - Post to multiple channels simultaneously
- 🛡️ **Duplicate Prevention** - Smart tracking prevents reposting same products
- 🖼️ **Image Support** - Automatic image posting from URLs
- 📊 **Progress Tracking** - Real-time posting status and comprehensive logging
- 🎨 **Professional UI** - Modern tabbed interface with intuitive design
- 📝 **Custom Templates** - Dynamic message templates using your Excel column names
- 📤 **Batch Processing** - Post multiple products with configurable delays
- 💾 **Configuration Saving** - Remembers your settings between sessions

## 🚀 Quick Start

### Option 1: Download from GitHub

1. **Download the Project**
   ```bash
   git clone https://github.com/yourusername/telegram-product-poster.git
   cd telegram-product-poster
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python telegram_product_poster.py
   ```

### Option 2: Direct Download

1. Download the ZIP file from GitHub
2. Extract to your desired folder
3. Open terminal/command prompt in the folder
4. Install requirements: `pip install -r requirements.txt`
5. Run: `python telegram_product_poster.py`

## 📋 Requirements

- **Python 3.7+** (Download from [python.org](https://python.org))
- **Required Packages** (automatically installed):
  - pandas>=2.0.0
  - requests>=2.31.0
  - openpyxl>=3.0.0

## 🛠️ Setup Instructions

### Step 1: Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow instructions to create your bot
4. Copy the bot token (looks like: `123456789:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)
5. **Important**: Add your bot to target channels as an **administrator**

### Step 2: Get Channel Information

**For Public Channels:**
- Use channel username (e.g., `@yourchannel`)

**For Private Channels:**
1. Forward a message from the channel to `@userinfobot`
2. Copy the channel ID (e.g., `-1001234567890`)

### Step 3: Prepare Your Excel File

Your Excel file can have **any structure**! The app adapts to your column headers. Example:

| ProductId | Product Desc | Price | Image Url | Category |
|-----------|--------------|-------|-----------|----------|
| 12345 | Gaming Mouse | $29.99 | https://... | Electronics |
| 67890 | Wireless Headphones | $79.99 | https://... | Audio |

#### 📝 Need a Template?

If you need a sample Excel file to get started, use the included helper tool:

```bash
python create_sample_template.py
```

This will create `sample_products_template.xlsx` with:
- ✅ **Sample Data**: 5 example products with realistic information
- ✅ **Column Examples**: Shows common column structures
- ✅ **Best Practices**: Demonstrates optimal data formatting
- ✅ **Ready to Use**: Just replace with your real data

**Generated Template Includes:**
- Product Name, Description, Pricing
- Image URLs, Product URLs
- Categories, Stock Status, Ratings
- And more useful columns!

## 📱 How to Use

### 1. Launch the Application
```bash
python telegram_product_poster.py
```

### 2. Configure Bot Settings
- Go to **"Bot Configuration"** tab
- Enter your Telegram bot token
- Add target channels (one per line)
- Click **"Save Configuration"**

### 3. Load Your Excel File
- Go to **"Products Excel"** tab
- Click **"Browse"** to select your Excel file
- Click **"Load Excel Data"**
- Use **"Show Column Helper"** to see available columns

### 4. Create Message Template
- Go to **"Message Template"** tab
- Create your template using your Excel column names as placeholders
- Example template:
```
🛍️ **{Product Desc}**

💰 Price: {Price}
🆔 ID: {ProductId}
📦 Category: {Category}

#products #deals
```

### 5. Start Posting
- Go to **"Auto Posting"** tab
- Set posting delay (recommended: 30-60 seconds)
- Click **"Start Posting"**
- Monitor progress in real-time

### 6. View Logs
- Go to **"Logs Status"** tab
- Monitor posting history
- Export logs if needed

## 🎯 Excel Column Placeholders

The app automatically detects your Excel columns and creates placeholders:

- **Column Name**: `Product Description` → **Placeholder**: `{Product Description}`
- **Column Name**: `Price` → **Placeholder**: `{Price}`
- **Column Name**: `Image URL` → **Placeholder**: `{Image URL}`

### Special Columns

- **Images**: Any column containing "image", "img", "photo", or "picture" in the name
- **Videos**: Any column containing "video", "vid", or "mp4" in the name
- **Links**: Any column containing "url", "link", or "href" in the name

## 📁 Project Structure

```
telegram-product-poster/
├── telegram_product_poster.py    # Main application file
├── requirements.txt              # Python dependencies
├── config.json                  # Configuration file (auto-created)
└── README.md                   # This file
```

## 🔧 Configuration File

The app automatically creates a `config.json` file to save your settings:

```json
{
    "bot_token": "your_bot_token_here",
    "channels": [
        "@yourchannel1",
        "-1001234567890"
    ],
    "message_template": "Your template here",
    "posting_delay": 60
}
```

### 📂 Config File Management

#### **Default Config File**
- **Location**: Same folder as the application
- **Name**: `config.json`
- **Auto-Creation**: Created automatically when you save settings

#### **Creating a New Config File**
If you need to start fresh or create multiple configurations:

1. **Delete Existing Config**: Remove `config.json` from the app folder
2. **Restart App**: The app will create a new empty config file
3. **Configure Settings**: Set up your bot token, channels, and templates
4. **Save**: Click "Save Configuration" to create the new file

#### **Changing Config File Name**
For advanced users who want custom config file names:

1. **Open the Python File**: Edit `telegram_product_poster.py`
2. **Find Config Line**: Look for `self.config_file = "config.json"`
3. **Change Name**: Replace with your desired name (e.g., `"my_config.json"`)
4. **Save and Restart**: Save the file and restart the application

```python
# Example: Change config file name
self.config_file = "my_custom_config.json"  # Change this line
```

#### **Multiple Configurations**
You can maintain multiple config files for different setups:
- `config_products.json` - For product posting
- `config_news.json` - For news posting  
- `config_promotions.json` - For promotional content

Just change the config file name in the code for each setup.
```

## ⚠️ Important Notes

### Telegram Limits
- **Rate Limit**: Don't post faster than 1 message per 30 seconds
- **Bot Permissions**: Bot must be admin in target channels
- **Message Length**: Keep messages under 4096 characters
- **Image Size**: Images should be under 10MB

### Excel File Tips
- **Supported Formats**: `.xlsx`, `.xls`, `.csv`
- **Headers**: First row should contain column headers
- **Data Types**: Text, numbers, dates all supported
- **Special Characters**: Unicode characters supported

### Security
- **Never share** your bot token publicly
- **Keep config.json** private (add to .gitignore if publishing)
- **Backup** your Excel files before processing

## 🐛 Troubleshooting

### Common Issues

**"Bot token is invalid"**
- Check token format (should contain numbers and letters)
- Ensure no extra spaces in token
- Create a new bot if token is corrupted

**"Can't post to channel"**
- Verify bot is admin in the channel
- Check channel username/ID format
- Ensure channel exists and is accessible

**"Excel file won't load"**
- Check file format (.xlsx, .xls, .csv)
- Ensure file isn't corrupted
- Close file in other applications

**"Images not posting"**
- Verify image URLs are accessible
- Check image file size (< 10MB)
- Ensure URLs start with http:// or https://

### Getting Help

1. Check the **"Logs Status"** tab for error details
2. Verify your bot token and channel settings
3. Test with a small Excel file first
4. Check Telegram bot permissions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

- **Developer**: Tech Mouad
- **YouTube**: [@techmouad](https://www.youtube.com/@techmouad)
- **Instagram**: [@tech_mouad](https://www.instagram.com/tech_mouad/)

For tutorials on automation tools and programming, visit the YouTube channel!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Features Roadmap

- [ ] Scheduled posting
- [ ] Multi-language support
- [ ] Database integration
- [ ] API endpoint support
- [ ] Advanced filtering options

---

**Made with ❤️ by Tech Mouad**

*Don't forget to ⭐ star this repository if it helped you!*
5. Add your bot to target channels as admin

### 2. Prepare Excel File

Create an Excel file with the following columns:

**Required Columns:**
- product_name - Name of the product

**Optional Columns:**
- description - Product description
- price - Product price
- category - Product category
- image_url - URL to product image
- product_url - Link to product page

**Auto-Generated Columns:**
- posted_date - Date when product was posted
- posted_status - Status: 'pending', 'posted', or 'failed'

### 3. Run the Application

`ash
python telegram_product_poster.py
`

## Usage

1. **Configuration Tab:**
   - Enter your Telegram bot token
   - Add target channels (one per line)
   - Use channel username (@channelname) or chat ID
   - Test bot connection

2. **Products Excel Tab:**
   - Browse and select your Excel file
   - Preview products and check columns
   - Review posting statistics

3. **Auto Posting Tab:**
   - Choose posting mode (unposted only or all products)
   - Set delay between posts
   - Set maximum posts per session
   - Preview next post before posting
   - Start posting process

4. **Logs & Status Tab:**
   - View real-time logs
   - Export logs to file
   - Monitor application status

## Excel Template Example

| product_name | description | price | category | image_url | product_url | posted_date | posted_status |
|-------------|-------------|-------|----------|-----------|-------------|-------------|---------------|
| iPhone 15 Pro | Latest iPhone model |  | Electronics | https://... | https://... | | pending |
| Nike Air Max | Comfortable running shoes |  | Fashion | https://... | https://... | | pending |

## Important Notes

- Use the application responsibly
- Respect Telegram's rate limits
- Test with a small number of products first
- Keep your bot token secure
- Make sure your bot has admin rights in target channels

## Troubleshooting

1. **Bot connection fails:**
   - Check bot token is correct
   - Ensure bot is created properly with @BotFather

2. **Failed to post to channel:**
   - Check bot is admin in the channel
   - Verify channel username or chat ID
   - Check internet connection

3. **Excel file errors:**
   - Ensure file has 'product_name' column
   - Check file is not open in another application
   - Verify file format (.xlsx or .xls)

## Support

For support and updates, check the video description!

---

**Disclaimer:** This software is for educational purposes. Use responsibly and in accordance with platform terms of service.
