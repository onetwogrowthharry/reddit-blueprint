# Reddit Blueprint

A Reddit API for analyzing r/blueprint_ posts. This tool collects all posts from the subreddit for research and analysis purposes while respecting Reddit's Terms of Service.

## 🔒 Compliance & Ethics

This script:
- ✅ Uses Reddit's **official API** (not web scraping)
- ✅ Respects all **rate limits** and ToS requirements  
- ✅ Designed for **research/analysis** (non-commercial use)
- ✅ Collects **public posts only**
- ✅ Includes **data retention** reminders (delete within 48 hours)

## 📋 What You'll Need

- A computer (Mac or Windows)
- 15 minutes for setup
- A Reddit account (free)

## 🚀 Step-by-Step Setup

### Step 1: Install Python

**For Mac Users:**
1. Open **Terminal** (Cmd + Space, type "Terminal")
2. Test if Python is installed: `python3 --version`
3. If you see a version number, skip to Step 2
4. If not, download Python from [python.org/downloads](https://python.org/downloads)
5. Install the downloaded `.pkg` file
6. Test again: `python3 --version`

**For Windows Users:**
1. Download Python from [python.org/downloads](https://python.org/downloads)
2. **IMPORTANT**: During installation, check "Add Python to PATH"
3. Open **Command Prompt** (Windows key + R, type "cmd")
4. Test: `python --version` or `py --version`

### Step 2: Download This Project

**Option A: Download ZIP**
1. Click the green "Code" button above
2. Select "Download ZIP"
3. Extract the ZIP file to your Desktop

**Option B: Clone with Git** (if you have Git installed)
```bash
git clone https://github.com/[YOUR-USERNAME]/reddit-blueprint-scraper.git
cd reddit-blueprint-scraper
```

### Step 3: Install Required Libraries

1. **Open Terminal/Command Prompt in the project folder**
   - **Mac**: Open Terminal, type `cd ` (with space), then drag the project folder into Terminal, press Enter
   - **Windows**: Hold Shift, right-click in the project folder, select "Open PowerShell here"

2. **Install requirements**
   ```bash
   # Mac users:
   pip3 install -r requirements.txt
   
   # Windows users:
   pip install -r requirements.txt
   ```

### Step 4: Get Reddit API Credentials

1. **Go to Reddit Apps page**
   - Visit: [reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
   - Log in to your Reddit account

2. **Create a new app**
   - Scroll down, click "Create App" or "Create Another App"
   - Fill out the form:
     - **Name**: `blueprint-research`
     - **App type**: Select **"script"**
     - **Description**: `Research analysis tool`
     - **About URL**: Leave blank
     - **Redirect URI**: `http://localhost:8080`
   - Click "Create app"

3. **Copy your credentials**
   - **Client ID**: The string under your app name (looks like `abc123xyz`)
   - **Client Secret**: Click "reveal" to see it
   - **Save these somewhere** - you'll need them next

### Step 5: Configure the Script

1. **Open the project in a code editor**
   - Use VS Code, Sublime Text, or even Notepad
   - Open the file `reddit_scraper.py`

2. **Add your Reddit credentials**
   - Find these lines near the bottom:
   ```python
   CLIENT_ID = "PUT_YOUR_CLIENT_ID_HERE"
   CLIENT_SECRET = "PUT_YOUR_CLIENT_SECRET_HERE"
   ```
   - Replace with your actual credentials (keep the quotes):
   ```python
   CLIENT_ID = "abc123xyz"  # Your actual client ID
   CLIENT_SECRET = "your_secret_here"  # Your actual secret
   ```

3. **Save the file** (Ctrl+S or Cmd+S)

### Step 6: Run the Script

1. **In your Terminal/Command Prompt**, run:
   ```bash
   # Mac users:
   python3 reddit_scraper.py
   
   # Windows users:
   python reddit_scraper.py
   ```

2. **What you'll see**:
   ```
   🚀 Reddit Data Collection - ToS Compliant Version
   📋 Collecting data for research/analysis purposes only
   
   🔗 Connecting to Reddit API...
   ✅ Connected to r/blueprint_
   📊 Subreddit has XXX subscribers
   📥 Collecting posts from r/blueprint_...
   📈 Collected 50 posts...
   📈 Collected 100 posts...
   🎉 Finished! Collected XXX total posts
   ```

3. **Check your results**
   - A new CSV file will be created: `blueprint_posts_YYYYMMDD_HHMMSS.csv`
   - Open it in Excel/Google Sheets to see the data

## 📊 Understanding Your Data

The CSV file contains these columns:
- **title**: Post title
- **url**: Link to the post
- **score**: Upvotes minus downvotes
- **created_date**: When the post was created
- **num_comments**: Number of comments
- **is_self**: True if it's a text post, False if it's a link

## 🔒 Important Compliance Notes

**MUST READ:**
- ⚠️ **Delete the CSV data within 48 hours** (Reddit's guideline)
- ✅ This data is for **research/analysis only** (not commercial use)
- ❌ **Don't redistribute** the raw Reddit data
- ✅ **Use insights/patterns**, not raw posts, in any reports

## 🛠️ Troubleshooting

**"ModuleNotFoundError: No module named 'praw'"**
- Run the install command again: `pip3 install praw` (Mac) or `pip install praw` (Windows)

**"Invalid credentials" or API errors**
- Double-check your Client ID and Secret are correct
- Make sure they're in quotes in the script
- Verify your Reddit app is set to "script" type

**"Command not found: python"**
- Try `python3` instead of `python` (Mac)
- Try `py` instead of `python` (Windows)
- Reinstall Python and check "Add to PATH" option

**No posts collected**
- The subreddit might be private or empty
- Try testing with a larger subreddit like `'python'` first

---

**Built for research and analysis purposes. Please use responsibly and in compliance with Reddit's Terms of Service.**
