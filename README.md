# 📱 Telegram Product Poster - YouTube Edition

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A powerful, user-friendly desktop application that automates posting products from Excel files to Telegram channels. Features universal Excel compatibility, duplicate prevention, and professional UI design.

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
