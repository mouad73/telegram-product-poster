"""
Telegram Product Poster - YouTube Edition
A simplified application that reads products from Excel and posts to Telegram channels

Features:
1. Load products from Excel file
2. Configure Telegram bot token and target channels  
3. Post products to Telegram with duplicate prevention
4. Track posting status and dates
5. Simple and user-friendly interface

Created for educational and sharing purposes.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import pandas as pd
import os
import json
import threading
import logging
from datetime import datetime
import time
import requests

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('telegram_product_poster.log'),
        logging.StreamHandler()
    ]
)

class TelegramProductPoster:
    def __init__(self, root):
        self.root = root
        self.root.title("Telegram Product Poster - YouTube Edition")
        self.root.geometry("900x750")
        self.root.configure(bg='#f0f0f0')
        
        # Configure custom styles for buttons
        self.setup_custom_styles()
        
        # Variables
        self.config_file = "config.json"
        self.excel_file_path = tk.StringVar()
        self.bot_token_var = tk.StringVar()
        self.posting_active = False
        self.products_df = None
        
        # Load existing configuration
        self.load_config()
        
        # Create UI
        self.create_ui()
        
    def setup_custom_styles(self):
        """Setup custom styles for the application"""
        style = ttk.Style()
        
        # Accent button style for social media links
        style.configure('Accent.TButton', 
                       font=('Arial', 10, 'bold'))
        
        # Try to configure colors (may not work on all systems)
        try:
            style.configure('Accent.TButton',
                           foreground='white',
                           background='#0078d4')
            style.map('Accent.TButton',
                     background=[('active', '#106ebe'),
                               ('pressed', '#005a9e')])
        except Exception:
            # Fallback if custom colors aren't supported
            pass
        
    def create_ui(self):
        """Create the main user interface"""
        # Title
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill=tk.X, padx=20, pady=10)
        
        title_label = ttk.Label(title_frame, text="Telegram Product Poster", 
                               font=('Arial', 16, 'bold'))
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, text="Post Products from Excel to Telegram Channels", 
                                  font=('Arial', 10, 'italic'))
        subtitle_label.pack()
        
        # Create notebook for tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Configuration Tab
        config_frame = ttk.Frame(notebook)
        notebook.add(config_frame, text="Bot Configuration")
        self.create_config_tab(config_frame)
        
        # Excel Tab
        excel_frame = ttk.Frame(notebook)
        notebook.add(excel_frame, text="Products Excel")
        self.create_excel_tab(excel_frame)
        
        # Message Customization Tab
        message_frame = ttk.Frame(notebook)
        notebook.add(message_frame, text="Message Template")
        self.create_message_tab(message_frame)
        
        # Posting Tab
        posting_frame = ttk.Frame(notebook)
        notebook.add(posting_frame, text="Auto Posting")
        self.create_posting_tab(posting_frame)
        
        # Logs Tab
        logs_frame = ttk.Frame(notebook)
        notebook.add(logs_frame, text="Logs Status")
        self.create_logs_tab(logs_frame)
        
        # About Developer Tab
        about_frame = ttk.Frame(notebook)
        notebook.add(about_frame, text="About Developer")
        self.create_about_tab(about_frame)
        
        # Show welcome message after UI is created
        self.root.after(1000, self.show_welcome_message)
        
    def create_config_tab(self, parent):
        """Create configuration tab for Telegram bot settings"""
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Bot Configuration
        bot_frame = ttk.LabelFrame(main_frame, text="Telegram Bot Configuration", padding=15)
        bot_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Instructions
        instructions = ttk.Label(bot_frame, 
                                text="To create a Telegram Bot:\n" +
                                     "1. Open Telegram and search for @BotFather\n" +
                                     "2. Send /newbot command\n" +
                                     "3. Follow the instructions to create your bot\n" +
                                     "4. Copy the bot token provided by BotFather\n" +
                                     "5. Add your bot to the target channels as admin",
                                justify=tk.LEFT, foreground='blue')
        instructions.pack(anchor=tk.W, pady=(0, 15))
        
        # Bot Token
        ttk.Label(bot_frame, text="Bot Token:").pack(anchor=tk.W)
        self.bot_token_entry = ttk.Entry(bot_frame, textvariable=self.bot_token_var, width=60, show="*")
        self.bot_token_entry.pack(anchor=tk.W, pady=(0, 10))
        
        # Show/Hide token button
        def toggle_token_visibility():
            if self.bot_token_entry.cget('show') == '*':
                self.bot_token_entry.config(show='')
                toggle_btn.config(text="Hide Token")
            else:
                self.bot_token_entry.config(show='*')
                toggle_btn.config(text="Show Token")
                
        toggle_btn = ttk.Button(bot_frame, text="Show Token", command=toggle_token_visibility)
        toggle_btn.pack(anchor=tk.W, pady=(0, 15))
        
        # Target Channels
        ttk.Label(bot_frame, text="Target Channels (one per line, use @channel_username or chat_id):").pack(anchor=tk.W)
        self.channels_text = tk.Text(bot_frame, height=5, width=60)
        self.channels_text.pack(anchor=tk.W, pady=(0, 10))
        
        # Test Bot Button
        test_btn = ttk.Button(bot_frame, text="Test Bot Connection", 
                             command=self.test_bot_connection)
        test_btn.pack(anchor=tk.W, pady=(0, 10))
        
        # Save Configuration Button
        save_btn = ttk.Button(main_frame, text="Save Configuration", 
                             command=self.save_config, style='Accent.TButton')
        save_btn.pack(pady=20)
        
    def create_excel_tab(self, parent):
        """Create Excel upload and preview tab"""
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # File Selection
        file_frame = ttk.LabelFrame(main_frame, text="Excel File Selection", padding=15)
        file_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Instructions
        instructions = ttk.Label(file_frame,
                                text="Upload an Excel file with product information.\n" +
                                     "The app will use your EXACT column headers as template placeholders.\n" +
                                     "Example: If your Excel has 'Product Desc' column, use {Product Desc} in templates.\n" +
                                     "Tracking columns will be added automatically: 'posted_date', 'posted_status'",
                                justify=tk.LEFT, foreground='blue')
        instructions.pack(anchor=tk.W, pady=(0, 15))
        
        # File path display
        file_frame_inner = ttk.Frame(file_frame)
        file_frame_inner.pack(fill=tk.X)
        
        ttk.Label(file_frame_inner, text="Selected File:").pack(anchor=tk.W)
        file_path_entry = ttk.Entry(file_frame_inner, textvariable=self.excel_file_path, 
                                   width=60, state='readonly')
        file_path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, pady=(0, 10))
        
        # Browse button
        browse_btn = ttk.Button(file_frame_inner, text="Browse Excel File", 
                               command=self.browse_excel_file)
        browse_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Preview Frame
        preview_frame = ttk.LabelFrame(main_frame, text="Products Preview", padding=15)
        preview_frame.pack(fill=tk.BOTH, expand=True)
        
        # Preview text widget
        self.preview_text = scrolledtext.ScrolledText(preview_frame, height=15, width=70)
        self.preview_text.pack(fill=tk.BOTH, expand=True)
        
        # Control buttons
        btn_frame = ttk.Frame(preview_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        preview_btn = ttk.Button(btn_frame, text="Preview Products", 
                                command=self.preview_excel_file)
        preview_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        refresh_btn = ttk.Button(btn_frame, text="Refresh Data", 
                                command=self.refresh_excel_data)
        refresh_btn.pack(side=tk.LEFT)
        
    def create_message_tab(self, parent):
        """Create message customization tab"""
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Instructions
        instructions_frame = ttk.LabelFrame(main_frame, text="Message Template Instructions", padding=15)
        instructions_frame.pack(fill=tk.X, pady=(0, 20))
        
        instructions = ttk.Label(instructions_frame,
                                text="Customize your message template using placeholders:\n" +
                                     "Available placeholders: {product_name}, {description}, {origin_price}, {discount_price}, {discount_percentage}, {currency},\n" +
                                     "{category}, {product_url}, {image_url}, {commission_rate}, {estimated_commission}, {sales_count}, {feedback_score},\n" +
                                     "{code_start_time}, {code_end_time}, {code_value}, {code_quantity}, {code_minimum_spend}, {timestamp}\n" +
                                     "Example: 🛍️ {product_name}\\n� Discount Price: {discount_price} {currency}\\n🔗 {product_url}",
                                justify=tk.LEFT, foreground='blue')
        instructions.pack(anchor=tk.W)
        
        # Message Template
        template_frame = ttk.LabelFrame(main_frame, text="Message Template", padding=15)
        template_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        ttk.Label(template_frame, text="Enter your custom message template:").pack(anchor=tk.W, pady=(0, 5))
        
        self.message_template = tk.Text(template_frame, height=10, width=70, wrap=tk.WORD)
        self.message_template.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Set default template - only showing fields that typically have data
        default_template = """🛍️ {product_name}

📝 {description}

💰 Sale Price: {discount_price} {currency}
🏷️ Regular Price: {origin_price} {currency}
🔥 Save {discount_percentage}%

� Buy Now: {product_url}

📅 Posted: {timestamp}"""
        
        self.message_template.insert(1.0, default_template)
        
        # Image Settings - prominent section
        image_frame = ttk.LabelFrame(main_frame, text="📸 Image Settings", padding=15)
        image_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Image inclusion setting
        image_row1 = ttk.Frame(image_frame)
        image_row1.pack(fill=tk.X, pady=(0, 10))
        
        self.include_image_var = tk.BooleanVar(value=False)
        image_checkbox = ttk.Checkbutton(image_row1, text="📷 Include images in posts", 
                                        variable=self.include_image_var, 
                                        command=self.toggle_image_settings)
        image_checkbox.pack(side=tk.LEFT)
        
        # Image column setting
        image_row2 = ttk.Frame(image_frame)
        image_row2.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(image_row2, text="Image column name in Excel:").pack(side=tk.LEFT)
        self.image_column_var = tk.StringVar(value="Image Url")
        self.image_column_entry = ttk.Entry(image_row2, textvariable=self.image_column_var, width=25)
        self.image_column_entry.pack(side=tk.LEFT, padx=(10, 0))
        
        # Help text for image settings
        image_help = ttk.Label(image_frame, 
                              text="💡 Tip: Enter the exact column name from your Excel file that contains image URLs.\n" +
                                   "Common names: 'Image Url', 'Photo', 'ImageLink', 'Picture'", 
                              foreground='gray', font=('Arial', 9))
        image_help.pack(anchor=tk.W, pady=(5, 0))
        
        # Initially disable image column entry if not checked
        self.root.after(10, self.toggle_image_settings)
        
        # Column Selection - now dynamic based on Excel file
        columns_frame = ttk.LabelFrame(main_frame, text="Available Excel Columns", padding=15)
        columns_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(columns_frame, text="Available column placeholders from your Excel file:").pack(anchor=tk.W, pady=(0, 10))
        
        # Create a text widget to show available columns
        self.columns_display = tk.Text(columns_frame, height=4, width=70, wrap=tk.WORD, state=tk.DISABLED)
        self.columns_display.pack(fill=tk.X, pady=(0, 10))
        
        # Control buttons
        btn_frame = ttk.Frame(template_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        preview_template_btn = ttk.Button(btn_frame, text="Preview Template", 
                                         command=self.preview_message_template)
        preview_template_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        reset_template_btn = ttk.Button(btn_frame, text="Reset to Default", 
                                       command=self.reset_message_template)
        reset_template_btn.pack(side=tk.LEFT)
        
        # Add helper button for building template
        help_template_btn = ttk.Button(btn_frame, text="Show Excel Columns", 
                                      command=self.show_column_helper)
        help_template_btn.pack(side=tk.LEFT, padx=(10, 0))
    
    def toggle_image_settings(self):
        """Enable/disable image column entry based on checkbox"""
        if hasattr(self, 'image_column_entry'):
            if self.include_image_var.get():
                self.image_column_entry.config(state='normal')
            else:
                self.image_column_entry.config(state='disabled')
    
    def show_column_helper(self):
        """Show available Excel columns and how to use them in templates"""
        try:
            if self.products_df is None or self.products_df.empty:
                messagebox.showwarning("Warning", "Please load an Excel file first to see available columns.")
                return
            
            # Get actual column names from Excel (exactly as they appear in the header row)
            columns = [col for col in self.products_df.columns if col not in ['posted_date', 'posted_status']]
            
            # Create helper window
            helper_window = tk.Toplevel(self.root)
            helper_window.title("Excel Columns Helper")
            helper_window.geometry("600x500")
            
            # Title
            ttk.Label(helper_window, text="Your Excel File Column Headers", 
                     font=('Arial', 14, 'bold')).pack(pady=10)
            
            # Instructions
            instructions_text = f"""These are the EXACT column headers from your Excel file.
Use them in your template exactly as shown (with curly braces):

Your Excel has {len(columns)} columns:"""
            
            ttk.Label(helper_window, text=instructions_text, 
                     justify=tk.LEFT, foreground='blue').pack(pady=(0, 10))
            
            # Columns list
            columns_frame = ttk.Frame(helper_window)
            columns_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            
            columns_text = scrolledtext.ScrolledText(columns_frame, height=15, width=70)
            columns_text.pack(fill=tk.BOTH, expand=True)
            
            # Add columns exactly as they are in Excel
            for i, col in enumerate(columns, 1):
                columns_text.insert(tk.END, f"{i}. Excel Header: '{col}'\n")
                columns_text.insert(tk.END, f"   Template Usage: {{{col}}}\n\n")
            
            # Add example template using actual headers
            columns_text.insert(tk.END, "\n" + "="*60 + "\n")
            columns_text.insert(tk.END, "AUTO-GENERATED TEMPLATE using YOUR headers:\n\n")
            
            # Create dynamic template based on actual column headers
            template_lines = []
            for col in columns[:6]:  # Use first 6 columns for template
                if any(keyword in col.lower() for keyword in ['name', 'title', 'product']):
                    template_lines.append(f"�️ {{{col}}}")
                elif any(keyword in col.lower() for keyword in ['desc', 'detail', 'info']):
                    template_lines.append(f"📝 {{{col}}}")
                elif any(keyword in col.lower() for keyword in ['price', 'cost', 'amount']):
                    template_lines.append(f"💰 Price: {{{col}}}")
                elif any(keyword in col.lower() for keyword in ['url', 'link', 'website']):
                    template_lines.append(f"🔗 Link: {{{col}}}")
                elif any(keyword in col.lower() for keyword in ['image', 'photo', 'pic']):
                    template_lines.append(f"📸 Image: {{{col}}}")
                else:
                    template_lines.append(f"📄 {col}: {{{col}}}")
            
            template_lines.append("📅 Posted: {timestamp}")
            example_template = "\n\n".join(template_lines)
            
            columns_text.insert(tk.END, example_template)
            
            # Buttons
            btn_frame = ttk.Frame(helper_window)
            btn_frame.pack(pady=10)
            
            ttk.Button(btn_frame, text="Use This Template", 
                      command=lambda: self.copy_example_template(example_template)).pack(side=tk.LEFT, padx=(0, 10))
            ttk.Button(btn_frame, text="Close", 
                      command=helper_window.destroy).pack(side=tk.LEFT)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to show column helper: {e}")
    
    def copy_example_template(self, template):
        """Copy example template to the message template field"""
        self.message_template.delete(1.0, tk.END)
        self.message_template.insert(1.0, template)
        messagebox.showinfo("Success", "Example template copied! You can now customize it with your preferred text and emojis.")
        
    def preview_message_template(self):
        """Preview the custom message template"""
        try:
            if self.products_df is None or self.products_df.empty:
                messagebox.showwarning("Warning", "Please load an Excel file first to preview the template.")
                return
            
            # Get first product for preview
            first_product = self.products_df.iloc[0]
            preview_message = self.format_custom_message(first_product)
            
            # Show preview in a new window
            preview_window = tk.Toplevel(self.root)
            preview_window.title("Message Template Preview")
            preview_window.geometry("500x400")
            
            ttk.Label(preview_window, text="Template Preview (with first product):", 
                     font=('Arial', 12, 'bold')).pack(pady=10)
            
            preview_text = scrolledtext.ScrolledText(preview_window, height=15, width=60)
            preview_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            preview_text.insert(1.0, preview_message)
            
            ttk.Button(preview_window, text="Close", 
                      command=preview_window.destroy).pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to preview template: {e}")
    
    def reset_message_template(self):
        """Reset message template to default"""
        default_template = """🛍️ {product_name}

📝 {description}

💰 Sale Price: {discount_price} {currency}
🏷️ Regular Price: {origin_price} {currency}
🔥 Save {discount_percentage}%

� Buy Now: {product_url}

📅 Posted: {timestamp}"""
        
    def reset_message_template(self):
        """Reset message template to use actual Excel column headers"""
        if hasattr(self, 'products_df') and self.products_df is not None:
            # Use actual Excel headers to create a dynamic template
            columns = [col for col in self.products_df.columns if col not in ['posted_date', 'posted_status']]
            
            if len(columns) >= 1:
                # Create template using actual column headers
                template_lines = []
                
                # Find the best columns for each section
                product_col = next((col for col in columns if any(keyword in col.lower() for keyword in ['name', 'title', 'product'])), columns[0])
                desc_col = next((col for col in columns if any(keyword in col.lower() for keyword in ['desc', 'detail', 'info'])), None)
                price_col = next((col for col in columns if any(keyword in col.lower() for keyword in ['price', 'cost', 'amount'])), None)
                url_col = next((col for col in columns if any(keyword in col.lower() for keyword in ['url', 'link', 'website'])), None)
                
                # Build template with actual headers
                template_lines.append(f"🛍️ {{{product_col}}}")
                
                if desc_col:
                    template_lines.append(f"📝 {{{desc_col}}}")
                
                if price_col:
                    template_lines.append(f"💰 Price: {{{price_col}}}")
                
                if url_col:
                    template_lines.append(f"🔗 Link: {{{url_col}}}")
                
                template_lines.append("📅 Posted: {timestamp}")
                
                default_template = "\n\n".join(template_lines)
            else:
                # Fallback template
                default_template = """🛍️ {Product Name}

📝 {Description}

💰 Price: {Price}

🔗 Link: {URL}

📅 Posted: {timestamp}"""
        else:
            # Default template when no Excel file is loaded
            default_template = """🛍️ {Product Name}

📝 {Description}

💰 Price: {Price}

🔗 Link: {URL}

📅 Posted: {timestamp}"""
        
        self.message_template.delete(1.0, tk.END)
        self.message_template.insert(1.0, default_template)

    def format_custom_message(self, product_row):
        """Format product information using custom template with original Excel headers"""
        try:
            # Get the template
            template = self.message_template.get(1.0, tk.END).strip()
            
            # Create a dictionary with all actual Excel column values
            values = {}
            
            # Use actual column headers from the Excel file
            if hasattr(self, 'products_df') and self.products_df is not None:
                for col in self.products_df.columns:
                    if col in product_row and pd.notna(product_row[col]):
                        value = str(product_row[col]).strip()
                        # Don't show empty values or just whitespace
                        if value and value != 'nan' and value != 'NaN':
                            values[col] = value
                        else:
                            values[col] = ""
                    else:
                        values[col] = ""  # Empty if no data
            
            # Add timestamp
            values['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M')
            
            # Add social media signature
            values['youtube_channel'] = "📺 YouTube: https://www.youtube.com/@techmouad"
            values['instagram'] = "📸 Instagram: https://www.instagram.com/tech_mouad/"
            values['signature'] = f"📺 YouTube: https://www.youtube.com/@techmouad\n📸 Instagram: https://www.instagram.com/tech_mouad/"
            
            # Replace placeholders in template
            try:
                formatted_message = template.format(**values)
            except KeyError as e:
                # If a placeholder is missing, try to substitute with empty string for missing keys
                missing_key = str(e).strip("'\"")
                logging.warning(f"Missing placeholder in template: {missing_key}")
                
                # Create a new values dict with empty strings for missing keys
                import re
                placeholders = re.findall(r'\{([^}]+)\}', template)
                for placeholder in placeholders:
                    if placeholder not in values:
                        values[placeholder] = f"[Missing: {placeholder}]"
                
                try:
                    formatted_message = template.format(**values)
                except Exception:
                    # If still failing, return template as is
                    formatted_message = template
            
            # Clean up the message - remove lines that only contain labels without values
            lines = formatted_message.split('\n')
            cleaned_lines = []
            
            for line in lines:
                # Skip lines that have patterns like "💰 Price:  " (emoji + label + empty value)
                # But keep lines that have actual content
                stripped_line = line.strip()
                if stripped_line and not self._is_empty_line(stripped_line):
                    cleaned_lines.append(line)
            
            return '\n'.join(cleaned_lines)
            
        except Exception as e:
            logging.error(f"Error formatting custom message: {e}")
            return f"Error formatting message: {e}"
    
    def _is_empty_line(self, line):
        """Check if a line only contains emojis and labels but no actual values"""
        # Remove emojis and common labels
        import re
        clean_line = re.sub(r'[^\w\s:]', '', line)  # Remove emojis and special chars
        clean_line = re.sub(r'(Sale Price|Regular Price|Save|Buy Now|Posted):', '', clean_line)
        return not clean_line.strip()
        
    def create_posting_tab(self, parent):
        """Create auto posting tab"""
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Posting Settings
        settings_frame = ttk.LabelFrame(main_frame, text="Posting Settings", padding=15)
        settings_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Posting mode
        ttk.Label(settings_frame, text="Posting Mode:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.posting_mode_var = tk.StringVar(value="unposted_only")
        
        mode_frame = ttk.Frame(settings_frame)
        mode_frame.grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        
        ttk.Radiobutton(mode_frame, text="Only unposted products", 
                       variable=self.posting_mode_var, value="unposted_only").pack(anchor=tk.W)
        ttk.Radiobutton(mode_frame, text="All products (ignore status)", 
                       variable=self.posting_mode_var, value="all_products").pack(anchor=tk.W)
        
        # Delay between posts
        ttk.Label(settings_frame, text="Delay between posts (seconds):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.delay_var = tk.IntVar(value=30)
        delay_spin = ttk.Spinbox(settings_frame, from_=5, to=300, textvariable=self.delay_var, width=10)
        delay_spin.grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        
        # Maximum posts per session
        ttk.Label(settings_frame, text="Maximum posts per session:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.max_posts_var = tk.IntVar(value=10)
        max_posts_spin = ttk.Spinbox(settings_frame, from_=1, to=100, textvariable=self.max_posts_var, width=10)
        max_posts_spin.grid(row=2, column=1, sticky=tk.W, padx=(10, 0), pady=5)
        
        # Control buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Start button
        self.start_btn = ttk.Button(control_frame, text="Start Posting Products", 
                                   command=self.start_posting, style='Accent.TButton')
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Stop button
        self.stop_btn = ttk.Button(control_frame, text="Stop Posting", 
                                  command=self.stop_posting, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Preview post button
        preview_post_btn = ttk.Button(control_frame, text="Preview Next Post", 
                                     command=self.preview_next_post)
        preview_post_btn.pack(side=tk.LEFT)
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Posting Status", padding=15)
        status_frame.pack(fill=tk.BOTH, expand=True)
        
        # Status label
        self.status_label = ttk.Label(status_frame, text="Ready to start posting", 
                                     font=('Arial', 10, 'bold'))
        self.status_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(status_frame, variable=self.progress_var, 
                                          maximum=100, length=400)
        self.progress_bar.pack(fill=tk.X, pady=(0, 10))
        
        # Statistics
        stats_frame = ttk.Frame(status_frame)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.total_products_label = ttk.Label(stats_frame, text="Total Products: 0")
        self.total_products_label.pack(side=tk.LEFT, padx=(0, 20))
        
        self.posted_products_label = ttk.Label(stats_frame, text="Posted: 0")
        self.posted_products_label.pack(side=tk.LEFT, padx=(0, 20))
        
        self.pending_products_label = ttk.Label(stats_frame, text="Pending: 0")
        self.pending_products_label.pack(side=tk.LEFT)
        
        # Current action label
        self.action_label = ttk.Label(status_frame, text="", foreground='blue')
        self.action_label.pack(anchor=tk.W)
        
    def create_logs_tab(self, parent):
        """Create logs display tab"""
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Logs display
        logs_frame = ttk.LabelFrame(main_frame, text="Application Logs", padding=15)
        logs_frame.pack(fill=tk.BOTH, expand=True)
        
        self.logs_text = scrolledtext.ScrolledText(logs_frame, height=25, width=80)
        self.logs_text.pack(fill=tk.BOTH, expand=True)
        
        # Control buttons
        btn_frame = ttk.Frame(logs_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        refresh_btn = ttk.Button(btn_frame, text="Refresh Logs", command=self.refresh_logs)
        refresh_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        clear_btn = ttk.Button(btn_frame, text="Clear Logs", command=self.clear_logs)
        clear_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        export_btn = ttk.Button(btn_frame, text="Export Logs", command=self.export_logs)
        export_btn.pack(side=tk.LEFT)
        
    def create_about_tab(self, parent):
        """Create about developer tab with social media links"""
        main_frame = ttk.Frame(parent)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_frame = ttk.Frame(main_frame)
        title_frame.pack(pady=(0, 30))
        
        title_label = ttk.Label(title_frame, text="Telegram Product Poster", 
                               font=('Arial', 20, 'bold'), foreground='#0078d4')
        title_label.pack()
        
        subtitle_label = ttk.Label(title_frame, text="Developed by Tech Mouad", 
                                  font=('Arial', 14, 'italic'), foreground='#666')
        subtitle_label.pack(pady=(5, 0))
        
        # App Info
        info_frame = ttk.LabelFrame(main_frame, text="📱 App Information", padding=20)
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        app_info = """🚀 Version: 2.0 - YouTube Edition
        
✨ Features:
• Dynamic Excel column support
• Custom message templates  
• Image posting support
• Multiple channel posting
• Progress tracking & logs
• Duplicate prevention

🎯 Perfect for:
• E-commerce product promotion
• Affiliate marketing
• Content distribution
• Automated posting"""
        
        info_text = tk.Text(info_frame, height=12, width=70, wrap=tk.WORD, 
                           relief=tk.FLAT, bg='#f8f9fa', font=('Arial', 10))
        info_text.pack(fill=tk.BOTH, expand=True)
        info_text.insert(1.0, app_info)
        info_text.config(state=tk.DISABLED)
        
        # Developer Section
        dev_frame = ttk.LabelFrame(main_frame, text="👨‍💻 Follow the Developer", padding=20)
        dev_frame.pack(fill=tk.X, pady=(0, 20))
        
        # YouTube Section
        youtube_frame = ttk.Frame(dev_frame)
        youtube_frame.pack(fill=tk.X, pady=(0, 15))
        
        youtube_icon = ttk.Label(youtube_frame, text="🎥", font=('Arial', 16))
        youtube_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        youtube_text = ttk.Label(youtube_frame, text="YouTube Channel - Tech Tutorials & Tools", 
                                font=('Arial', 12, 'bold'))
        youtube_text.pack(side=tk.LEFT)
        
        youtube_btn = ttk.Button(youtube_frame, text="🔗 Visit YouTube Channel", 
                               command=lambda: self.open_url("https://www.youtube.com/@techmouad"),
                               style='Accent.TButton')
        youtube_btn.pack(side=tk.RIGHT)
        
        # Instagram Section  
        instagram_frame = ttk.Frame(dev_frame)
        instagram_frame.pack(fill=tk.X, pady=(0, 15))
        
        instagram_icon = ttk.Label(instagram_frame, text="📸", font=('Arial', 16))
        instagram_icon.pack(side=tk.LEFT, padx=(0, 10))
        
        instagram_text = ttk.Label(instagram_frame, text="Instagram - Latest Tech Updates", 
                                  font=('Arial', 12, 'bold'))
        instagram_text.pack(side=tk.LEFT)
        
        instagram_btn = ttk.Button(instagram_frame, text="🔗 Follow on Instagram", 
                                 command=lambda: self.open_url("https://www.instagram.com/tech_mouad/"),
                                 style='Accent.TButton')
        instagram_btn.pack(side=tk.RIGHT)
        
        # Support Section
        support_frame = ttk.LabelFrame(main_frame, text="💝 Support the Developer", padding=20)
        support_frame.pack(fill=tk.X)
        
        support_text = ttk.Label(support_frame, 
                               text="If this app helped you, please:\n" +
                                    "• Subscribe to my YouTube channel for more tools\n" +
                                    "• Follow me on Instagram for tech updates\n" +
                                    "• Share this app with your friends\n" +
                                    "• Leave feedback and suggestions",
                               font=('Arial', 11), justify=tk.LEFT)
        support_text.pack(anchor=tk.W)
        
    def open_url(self, url):
        """Open URL in default browser"""
        try:
            import webbrowser
            webbrowser.open(url)
        except Exception as e:
            # Fallback: copy to clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(url)
            messagebox.showinfo("Link Copied", f"Link copied to clipboard:\n{url}")
            
    def show_welcome_message(self):
        """Show welcome message with developer info"""
        welcome_msg = """🎉 Welcome to Telegram Product Poster - YouTube Edition!
        
This app was developed by Tech Mouad.

📺 Want to learn more about automation tools and programming?
Check out my YouTube channel for tutorials and tools like this!

Visit the 'About Developer' tab to connect with me on social media.

Happy posting! 🚀"""
        
        # Create custom dialog
        welcome_window = tk.Toplevel(self.root)
        welcome_window.title("Welcome!")
        welcome_window.geometry("450x300")
        welcome_window.resizable(False, False)
        
        # Center the window
        welcome_window.transient(self.root)
        welcome_window.grab_set()
        
        # Content frame
        content_frame = ttk.Frame(welcome_window, padding=20)
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Welcome text
        welcome_text = tk.Text(content_frame, wrap=tk.WORD, height=12, width=50,
                              relief=tk.FLAT, bg='#f8f9fa', font=('Arial', 11))
        welcome_text.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        welcome_text.insert(1.0, welcome_msg)
        welcome_text.config(state=tk.DISABLED)
        
        # Buttons frame
        btn_frame = ttk.Frame(content_frame)
        btn_frame.pack(fill=tk.X)
        
        # YouTube button
        youtube_btn = ttk.Button(btn_frame, text="🎥 Visit YouTube", 
                               command=lambda: [self.open_url("https://www.youtube.com/@techmouad"), welcome_window.destroy()],
                               style='Accent.TButton')
        youtube_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Close button
        close_btn = ttk.Button(btn_frame, text="Start Using App", 
                             command=welcome_window.destroy)
        close_btn.pack(side=tk.RIGHT)
    
        
    def load_config(self):
        """Load configuration from file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.bot_token_var.set(config.get('bot_token', ''))
                    self.excel_file_path.set(config.get('excel_file_path', ''))
                    
                    # Load channels after UI is created
                    self.root.after(100, lambda: self.load_channels(config.get('target_channels', [])))
                    
                    # Load message template and column settings
                    self.root.after(200, lambda: self.load_message_settings(config))
                        
        except Exception as e:
            logging.error(f"Error loading config: {e}")
    
    def load_message_settings(self, config):
        """Load message template and column settings"""
        try:
            # Load message template
            if hasattr(self, 'message_template') and config.get('message_template'):
                self.message_template.delete(1.0, tk.END)
                self.message_template.insert(1.0, config['message_template'])
            
            # Load column settings
            if hasattr(self, 'column_vars') and config.get('column_settings'):
                for col, value in config['column_settings'].items():
                    if col in self.column_vars:
                        self.column_vars[col].set(value)
                        
        except Exception as e:
            logging.error(f"Error loading message settings: {e}")
            
    def load_channels(self, channels):
        """Load channels into text widget"""
        try:
            if hasattr(self, 'channels_text') and channels:
                self.channels_text.delete(1.0, tk.END)
                self.channels_text.insert(1.0, '\n'.join(channels))
        except Exception as e:
            logging.error(f"Error loading channels: {e}")
            
    def save_config(self):
        """Save configuration to file"""
        try:
            # Get channels from text widget
            channels_text = self.channels_text.get(1.0, tk.END).strip()
            channels = [line.strip() for line in channels_text.split('\n') if line.strip()]
            
            # Get message template and column settings
            template = ""
            column_settings = {}
            if hasattr(self, 'message_template'):
                template = self.message_template.get(1.0, tk.END).strip()
            if hasattr(self, 'column_vars'):
                column_settings = {col: var.get() for col, var in self.column_vars.items()}
            
            config = {
                'bot_token': self.bot_token_var.get(),
                'excel_file_path': self.excel_file_path.get(),
                'target_channels': channels,
                'message_template': template,
                'column_settings': column_settings
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)
                
            messagebox.showinfo("Success", "Configuration saved successfully!")
            logging.info("Configuration saved successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save configuration: {e}")
            logging.error(f"Error saving config: {e}")
            
    def browse_excel_file(self):
        """Browse and select Excel file"""
        file_path = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=[("Excel files", "*.xlsx *.xls"), ("All files", "*.*")]
        )
        
        if file_path:
            self.excel_file_path.set(file_path)
            self.log_message(f"Excel file selected: {file_path}")
            self.refresh_excel_data()
            
    def refresh_excel_data(self):
        """Refresh Excel data and update statistics - preserves EXACT original headers."""
        try:
            file_path = self.excel_file_path.get()
            if not file_path or not os.path.exists(file_path):
                return

            df = None
            if file_path.lower().endswith('.xls'):
                # Try xlrd first, then pyexcel, then raise error
                try:
                    df = pd.read_excel(file_path, header=0, engine='xlrd')
                except Exception as e1:
                    try:
                        import pyexcel as pe
                        records = pe.get_records(file_name=file_path)
                        df = pd.DataFrame(list(records))
                    except Exception as e2:
                        self.log_message(f"Error reading .xls file: {e1} | {e2}")
                        messagebox.showerror("Error", "Could not read .xls file. Please convert it to .xlsx or install the required engines (xlrd < 2.0.0, pyexcel, pyexcel-xls).\n\nError details: {} | {}".format(e1, e2))
                        return
            else:
                try:
                    df = pd.read_excel(file_path, header=0)
                except Exception as e:
                    self.log_message(f"Error reading Excel file: {e}")
                    messagebox.showerror("Error", f"Could not read Excel file: {e}")
                    return

            if df is None or not isinstance(df, pd.DataFrame) or df.empty:
                self.log_message("Error: Loaded DataFrame is empty or invalid.")
                messagebox.showerror("Error", "Loaded Excel file is empty or invalid.")
                return

            # PRESERVE EXACT ORIGINAL HEADERS - only strip whitespace, no renaming
            df.columns = [str(col).strip() for col in df.columns]
            df = df.dropna(axis=1, how='all')

            # Log the actual headers we found
            self.log_message(f"Found Excel headers: {list(df.columns)}")

            # ONLY add tracking columns if they don't exist - NO OTHER COLUMN MODIFICATIONS
            if 'posted_date' not in df.columns:
                df['posted_date'] = ''
            if 'posted_status' not in df.columns:
                df['posted_status'] = 'pending'

            # Store DataFrame WITHOUT modifying the original file
            self.products_df = df

            # Update statistics
            total = len(self.products_df)
            posted = len(self.products_df[self.products_df['posted_status'] == 'posted'])
            pending = total - posted

            if hasattr(self, 'total_products_label'):
                self.total_products_label.config(text=f"Total Products: {total}")
                self.posted_products_label.config(text=f"Posted: {posted}")
                self.pending_products_label.config(text=f"Pending: {pending}")

            # DO NOT save back to Excel file here - preserve original file
            # Only save when actually posting products

            # Update the message template tab with new columns
            self.update_column_options()

        except Exception as e:
            self.log_message(f"Error refreshing Excel data: {e}")
    
    def update_column_options(self):
        """Update available columns display when Excel file is loaded"""
        try:
            if hasattr(self, 'columns_display') and self.products_df is not None:
                # Get all column names (exact headers from Excel)
                available_columns = [col for col in self.products_df.columns if col not in ['posted_date', 'posted_status']]
                
                # Create display text with placeholders using exact Excel headers
                placeholder_text = f"Available placeholders from your Excel file ({len(available_columns)} columns):\n\n"
                for col in available_columns:
                    placeholder_text += f"• {{{col}}} (from column: '{col}')\n"
                placeholder_text += f"\n• {{timestamp}} (always available)\n\n"
                placeholder_text += "These are the EXACT headers from your Excel file.\nUse them exactly as shown above in your template."
                
                # Update the text widget
                self.columns_display.config(state=tk.NORMAL)
                self.columns_display.delete(1.0, tk.END)
                self.columns_display.insert(1.0, placeholder_text)
                self.columns_display.config(state=tk.DISABLED)
                
                # Auto-generate a template using actual Excel headers
                self.reset_message_template()
                
        except Exception as e:
            logging.error(f"Error updating column options: {e}")
            
    def preview_excel_file(self):
        """Preview the selected Excel file"""
        file_path = self.excel_file_path.get()
        
        if not file_path or not os.path.exists(file_path):
            messagebox.showerror("Error", "Please select a valid Excel file first.")
            return
            
        try:
            if self.products_df is None:
                self.refresh_excel_data()
                
            # Clear previous preview
            self.preview_text.delete(1.0, tk.END)
            
            # Display file info
            self.preview_text.insert(tk.END, f"File: {os.path.basename(file_path)}\n")
            self.preview_text.insert(tk.END, f"Total Products: {len(self.products_df)}\n")
            self.preview_text.insert(tk.END, f"Columns: {', '.join(self.products_df.columns)}\n\n")
            
            # No required columns check - accept any Excel structure
            self.preview_text.insert(tk.END, f"✅ Excel file loaded successfully with {len(self.products_df.columns)} columns\n\n")
                
            # Display first few products
            self.preview_text.insert(tk.END, "First 5 products:\n")
            self.preview_text.insert(tk.END, "=" * 50 + "\n")
            
            for i, row in self.products_df.head(5).iterrows():
                self.preview_text.insert(tk.END, f"\nProduct {i+1}:\n")
                for col in self.products_df.columns:
                    value = str(row[col])[:100]  # Limit display length
                    self.preview_text.insert(tk.END, f"  {col}: {value}\n")
                    
            # Show posting statistics
            posted_count = len(self.products_df[self.products_df['posted_status'] == 'posted'])
            pending_count = len(self.products_df[self.products_df['posted_status'] != 'posted'])
            
            self.preview_text.insert(tk.END, f"\n\nPosting Status:\n")
            self.preview_text.insert(tk.END, f"Posted: {posted_count}\n")
            self.preview_text.insert(tk.END, f"Pending: {pending_count}\n")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read Excel file: {e}")
            logging.error(f"Error reading Excel file: {e}")
            
    def test_bot_connection(self):
        """Test Telegram bot connection"""
        bot_token = self.bot_token_var.get().strip()
        
        if not bot_token:
            messagebox.showerror("Error", "Please enter bot token first.")
            return
            
        def test_connection():
            try:
                # Test bot token
                url = f"https://api.telegram.org/bot{bot_token}/getMe"
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200:
                    bot_info = response.json()
                    if bot_info['ok']:
                        bot_name = bot_info['result']['username']
                        messagebox.showinfo("Success", f"Bot connection successful!\nBot: @{bot_name}")
                        logging.info(f"Bot connection test successful: @{bot_name}")
                    else:
                        messagebox.showerror("Error", "Invalid bot token")
                else:
                    messagebox.showerror("Error", f"Failed to connect: {response.status_code}")
                    
            except Exception as e:
                messagebox.showerror("Connection Error", f"Failed to test bot connection: {e}")
                logging.error(f"Bot connection test failed: {e}")
                
        # Run in separate thread
        thread = threading.Thread(target=test_connection)
        thread.daemon = True
        thread.start()
        
    def preview_next_post(self):
        """Preview the next post that will be sent"""
        try:
            if self.products_df is None:
                messagebox.showwarning("Warning", "Please load an Excel file first.")
                return
                
            # Get next unposted product
            if self.posting_mode_var.get() == "unposted_only":
                unposted = self.products_df[self.products_df['posted_status'] != 'posted']
            else:
                unposted = self.products_df
                
            if unposted.empty:
                messagebox.showinfo("Info", "No products available for posting.")
                return
                
            next_product = unposted.iloc[0]
            post_text = self.format_product_message(next_product)
            
            # Show preview in a new window
            preview_window = tk.Toplevel(self.root)
            preview_window.title("Post Preview")
            preview_window.geometry("500x400")
            
            ttk.Label(preview_window, text="Next Post Preview:", font=('Arial', 12, 'bold')).pack(pady=10)
            
            preview_text = scrolledtext.ScrolledText(preview_window, height=15, width=60)
            preview_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
            preview_text.insert(1.0, post_text)
            
            ttk.Button(preview_window, text="Close", 
                      command=preview_window.destroy).pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to preview post: {e}")
            
    def format_product_message(self, product_row):
        """Format product information into a Telegram message"""
        try:
            # Use custom template if available
            if hasattr(self, 'message_template'):
                return self.format_custom_message(product_row)
            
            # Fallback to default format using first available columns
            message_parts = []
            
            # Get available columns (excluding tracking columns)
            available_cols = [col for col in product_row.index if col not in ['posted_date', 'posted_status']]
            
            # Use first column as product identifier
            if available_cols and pd.notna(product_row[available_cols[0]]):
                identifier = str(product_row[available_cols[0]])
                message_parts.append(f"�️ {identifier}")
            
            # Add other columns that have data
            for col in available_cols[1:4]:  # Show next 3 columns with data
                if pd.notna(product_row[col]) and str(product_row[col]).strip():
                    value = str(product_row[col])
                    message_parts.append(f"\n� {col}: {value}")
            
            # Add timestamp
            message_parts.append(f"\n\n📅 Posted: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
            
            return ''.join(message_parts)
            
        except Exception as e:
            logging.error(f"Error formatting message: {e}")
            # Use first column value as fallback
            first_col = product_row.index[0] if len(product_row.index) > 0 else 'Unknown'
            return f"Product: {str(product_row.get(first_col, 'Unknown'))}"
            
    def start_posting(self):
        """Start the auto posting process"""
        if not self.validate_config():
            return
            
        self.posting_active = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        
        # Start posting in separate thread
        thread = threading.Thread(target=self.posting_worker)
        thread.daemon = True
        thread.start()
        
    def stop_posting(self):
        """Stop the auto posting process"""
        self.posting_active = False
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.update_status("Posting stopped by user")
        
    def validate_config(self):
        """Validate configuration before starting"""
        if not self.bot_token_var.get().strip():
            messagebox.showerror("Error", "Please enter bot token.")
            return False
            
        channels_text = self.channels_text.get(1.0, tk.END).strip()
        if not channels_text:
            messagebox.showerror("Error", "Please enter at least one target channel.")
            return False
            
        if not self.excel_file_path.get() or not os.path.exists(self.excel_file_path.get()):
            messagebox.showerror("Error", "Please select a valid Excel file.")
            return False
            
        if self.products_df is None:
            messagebox.showerror("Error", "Please load the Excel file first.")
            return False
            
        return True
        
    def posting_worker(self):
        """Main posting worker function"""
        try:
            self.update_status("Starting product posting...")
            self.update_progress(0)
            
            # Get target channels
            channels_text = self.channels_text.get(1.0, tk.END).strip()
            channels = [line.strip() for line in channels_text.split('\n') if line.strip()]
            
            # Get products to post
            if not isinstance(self.products_df, pd.DataFrame) or self.products_df.empty:
                self.update_status("No valid products loaded. Please check your Excel file.")
                return
            if self.posting_mode_var.get() == "unposted_only":
                products_to_post = self.products_df[self.products_df['posted_status'] != 'posted']
            else:
                products_to_post = self.products_df.copy()
            if products_to_post.empty:
                self.update_status("No products to post")
                return
                
            # Limit posts per session
            max_posts = min(len(products_to_post), self.max_posts_var.get())
            products_to_post = products_to_post.head(max_posts)
            
            self.log_message(f"Starting to post {len(products_to_post)} products to {len(channels)} channels")
            
            # Post products
            posted_count = 0
            
            for i, (index, product) in enumerate(products_to_post.iterrows()):
                if not self.posting_active:
                    break
                    
                # Ensure product is a Series (row), not a scalar
                if not isinstance(product, pd.Series):
                    self.log_message(f"Warning: Skipping row {index} as it is not a valid product record.")
                    continue
                    
                # Get product identifier from first column for logging
                first_col = self.products_df.columns[0] if len(self.products_df.columns) > 0 else 'Unknown'
                product_identifier = str(product.get(first_col, f'Product {index}'))
                self.update_action(f"Posting: {product_identifier[:50]}...")
                # Format message
                message = self.format_product_message(product)
                # Post to all channels
                success = True
                for channel in channels:
                    if not self.posting_active:
                        break
                    if self.send_message_to_channel(channel, message, product):
                        self.log_message(f"✅ Posted '{product_identifier}' to {channel}")
                    else:
                        self.log_message(f"❌ Failed to post '{product_identifier}' to {channel}")
                        success = False
                # Update status in Excel
                if success:
                    self.products_df.loc[index, 'posted_status'] = 'posted'
                    self.products_df.loc[index, 'posted_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    posted_count += 1
                else:
                    self.products_df.loc[index, 'posted_status'] = 'failed'
                # Update progress
                progress = ((i + 1) / len(products_to_post)) * 100
                self.update_progress(progress)
                # Delay between posts
                if i < len(products_to_post) - 1 and self.posting_active:
                    delay = self.delay_var.get()
                    self.update_action(f"Waiting {delay} seconds...")
                    time.sleep(delay)
                    
            # Save updated Excel
            self.products_df.to_excel(self.excel_file_path.get(), index=False)
            self.refresh_excel_data()
            
            self.update_status(f"Posting completed! Posted {posted_count} products.")
            self.update_progress(100)
            
        except Exception as e:
            self.log_message(f"Error in posting worker: {e}")
            self.update_status(f"Error: {e}")
        finally:
            self.posting_active = False
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)
            
    def send_message_to_channel(self, channel, message, product_row):
        """Send message to a Telegram channel"""
        try:
            bot_token = self.bot_token_var.get().strip()
            
            # Check if images should be included and if there's an image URL
            image_column = self.image_column_var.get().strip()
            include_image = self.include_image_var.get()
            
            if (include_image and image_column and 
                image_column in product_row and 
                pd.notna(product_row[image_column]) and 
                str(product_row[image_column]).strip()):
                # Send as photo with caption
                url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
                data = {
                    'chat_id': channel,
                    'photo': product_row[image_column],
                    'caption': message
                }
            else:
                # Send as text message if no image or image disabled
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                data = {
                    'chat_id': channel,
                    'text': message
                }
            
            response = requests.post(url, data=data, timeout=30)
            
            if response.status_code == 200 and response.json().get('ok'):
                return True
            else:
                if response.status_code == 200:
                    error_msg = response.json().get('description', 'Unknown error')
                else:
                    try:
                        error_detail = response.json().get('description', f'HTTP {response.status_code}')
                    except:
                        error_detail = f'HTTP {response.status_code}'
                    error_msg = error_detail
                logging.error(f"Failed to send message to {channel}: {error_msg}")
                self.log_message(f"Telegram API Error for {channel}: {error_msg}")
                return False
                
        except Exception as e:
            logging.error(f"Error sending message to {channel}: {e}")
            return False
            
    def send_image_to_channel(self, channel, image_url, bot_token):
        """Send image to Telegram channel"""
        try:
            url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
            data = {
                'chat_id': channel,
                'photo': image_url
            }
            
            response = requests.post(url, data=data, timeout=30)
            return response.status_code == 200 and response.json().get('ok')
            
        except Exception as e:
            logging.error(f"Error sending image to {channel}: {e}")
            return False
            
    def update_status(self, message):
        """Update status label"""
        if hasattr(self, 'status_label'):
            self.status_label.config(text=message)
        self.log_message(message)
        
    def update_action(self, message):
        """Update current action label"""
        if hasattr(self, 'action_label'):
            self.action_label.config(text=message)
            self.root.update_idletasks()
        
    def update_progress(self, value):
        """Update progress bar"""
        if hasattr(self, 'progress_var'):
            self.progress_var.set(value)
            self.root.update_idletasks()
        
    def log_message(self, message):
        """Add message to logs"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        # Add to logs display
        if hasattr(self, 'logs_text'):
            self.logs_text.insert(tk.END, log_entry)
            self.logs_text.see(tk.END)
            self.root.update_idletasks()
        
        # Also log to file
        logging.info(message)
        
    def refresh_logs(self):
        """Refresh logs display"""
        try:
            if os.path.exists('telegram_product_poster.log'):
                with open('telegram_product_poster.log', 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.logs_text.delete(1.0, tk.END)
                    self.logs_text.insert(1.0, content)
                    self.logs_text.see(tk.END)
        except Exception as e:
            self.log_message(f"Error refreshing logs: {e}")
            
    def clear_logs(self):
        """Clear logs display"""
        if hasattr(self, 'logs_text'):
            self.logs_text.delete(1.0, tk.END)
        
    def export_logs(self):
        """Export logs to file"""
        try:
            file_path = filedialog.asksaveasfilename(
                title="Export Logs",
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.logs_text.get(1.0, tk.END))
                messagebox.showinfo("Success", f"Logs exported to {file_path}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export logs: {e}")

def main():
    root = tk.Tk()
    
    # Set theme
    style = ttk.Style()
    try:
        style.theme_use('clam')
    except:
        pass
    
    # Create custom styles
    try:
        style.configure('Accent.TButton', foreground='white', background='#0078d4')
        style.map('Accent.TButton', background=[('active', '#106ebe')])
    except:
        pass
    
    app = TelegramProductPoster(root)
    
    # Add disclaimer
    def show_disclaimer():
        disclaimer = """
TELEGRAM PRODUCT POSTER - YouTube Edition

Features:
 Load products from Excel file
 Configure Telegram bot and channels
 Post products with duplicate prevention
 Track posting status and dates
 User-friendly interface

IMPORTANT:
 Make sure your Excel file has a 'product_name' column
 Create a Telegram bot using @BotFather
 Add your bot as admin to target channels
 Use responsibly and respect platform limits

For support and updates, check the video description!
        """
        messagebox.showinfo("Welcome to Telegram Product Poster", disclaimer)
    
    # Show disclaimer on startup
    root.after(1000, show_disclaimer)
    
    root.mainloop()

if __name__ == "__main__":
    main()
