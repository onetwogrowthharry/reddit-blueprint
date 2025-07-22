import praw
import csv
from datetime import datetime
import time

# ===== REDDIT API COMPLIANCE NOTES =====
# This script follows Reddit's Terms of Service by:
# 1. Using official Reddit API (via PRAW) - NOT web scraping
# 2. Respecting rate limits (PRAW handles this automatically)
# 3. Research/academic use (non-commercial analysis)
# 4. One-time data collection (not ongoing monitoring)
# 5. Collecting public posts only (no private data)

def setup_reddit(client_id, client_secret):
    """
    Connect to Reddit API using official authentication
    COMPLIANCE: Uses OAuth2 authentication as required by Reddit
    """
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent="blueprint_research_analysis 1.0",  # Descriptive user agent as required
        requestor_kwargs={'session': None}  # Ensures fresh session
    )
    return reddit

def scrape_subreddit_responsibly(subreddit_name, client_id, client_secret, limit=None):
    """
    Responsibly scrape posts from a subreddit
    COMPLIANCE: 
    - Respects Reddit's rate limits (100 requests/minute for free tier)
    - Uses official API endpoints only
    - Adds delays to be extra respectful of server load
    """
    print(f"🔗 Connecting to Reddit API...")
    reddit = setup_reddit(client_id, client_secret)
    
    # Test connection first
    try:
        test_sub = reddit.subreddit(subreddit_name)
        print(f"✅ Connected to r/{subreddit_name}")
        print(f"📊 Subreddit has {test_sub.subscribers:,} subscribers")
    except Exception as e:
        print(f"❌ Error connecting: {e}")
        return []
    
    print(f"📥 Collecting posts from r/{subreddit_name}...")
    print(f"⏱️  Using respectful delays to avoid overloading Reddit's servers")
    
    posts = []
    count = 0
    
    try:
        # COMPLIANCE: Only collecting public posts that are already visible
        for post in test_sub.new(limit=limit):
            posts.append({
                'title': post.title,
                'url': post.url,
                'score': post.score,
                'created_date': datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
                'id': post.id,
                'num_comments': post.num_comments,
                'is_self': post.is_self,  # Text post vs link
                'subreddit': str(post.subreddit)  # For data tracking
            })
            
            count += 1
            
            # Progress updates and respectful delays
            if count % 50 == 0:
                print(f"📈 Collected {count} posts...")
                # COMPLIANCE: Extra delay every 50 requests to be respectful
                time.sleep(1)  # 1 second pause to be extra courteous
            
            # COMPLIANCE: Built-in protection against runaway scripts
            if count >= 10000:  # Safety limit
                print(f"⚠️  Reached safety limit of 10,000 posts")
                break
                
    except Exception as e:
        print(f"❌ Error during collection: {e}")
        print(f"✅ Collected {count} posts before error")
    
    print(f"🎉 Finished! Collected {len(posts)} total posts")
    return posts

def save_to_csv_with_metadata(posts, filename):
    """
    Save posts to CSV with compliance metadata
    COMPLIANCE: Includes data collection timestamp for retention tracking
    """
    if not posts:
        print("❌ No posts to save")
        return
    
    # Add metadata header with compliance info
    collection_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        # Write compliance header
        file.write(f"# Reddit Data Collection Report\n")
        file.write(f"# Collection Time: {collection_time}\n")
        file.write(f"# Data Source: Reddit API (official)\n")
        file.write(f"# Purpose: Research/Analysis (non-commercial)\n")
        file.write(f"# Compliance: Reddit ToS compliant collection\n")
        file.write(f"# Retention: Delete within 48 hours per Reddit guidelines\n")
        file.write(f"# Total Posts: {len(posts)}\n\n")
        
        # Write actual CSV data
        writer = csv.DictWriter(file, fieldnames=posts[0].keys())
        writer.writeheader()
        writer.writerows(posts)
    
    print(f"💾 Saved {len(posts)} posts to {filename}")
    print(f"⚠️  IMPORTANT: Delete this data within 48 hours per Reddit's guidelines")

def print_compliance_reminder():
    """Print important compliance reminders"""
    print("\n" + "="*60)
    print("🔒 REDDIT API COMPLIANCE REMINDER")
    print("="*60)
    print("✅ This data was collected using Reddit's official API")
    print("✅ Collection respects rate limits and ToS")
    print("⚠️  FOR RESEARCH/ANALYSIS USE ONLY (non-commercial)")
    print("⚠️  DELETE THIS DATA WITHIN 48 HOURS")
    print("⚠️  Do not redistribute raw Reddit data")
    print("✅ Use insights/patterns, not raw posts, in any reports")
    print("="*60)

if __name__ == "__main__":
    print("🚀 Reddit Data Collection - ToS Compliant Version")
    print("📋 Collecting data for research/analysis purposes only\n")
    
    # ===== REPLACE WITH YOUR ACTUAL CREDENTIALS =====
    CLIENT_ID = "PUT_YOUR_CLIENT_ID_HERE"
    CLIENT_SECRET = "PUT_YOUR_CLIENT_SECRET_HERE"
    
    # Validate credentials are set
    if "PUT_YOUR" in CLIENT_ID or "PUT_YOUR" in CLIENT_SECRET:
        print("❌ Please add your Reddit API credentials first!")
        print("   Update CLIENT_ID and CLIENT_SECRET in the script")
        exit(1)
    
    # COMPLIANCE: Clear about what we're doing and why
    print("🎯 Target: r/blueprint_")
    print("📊 Purpose: Analyzing post patterns and content themes")
    print("⚖️  Compliance: Using official Reddit API, research use only")
    print("⏱️  Method: Respectful rate-limited collection\n")
    
    # Collect data responsibly
    posts = scrape_subreddit_responsibly('blueprint_', CLIENT_ID, CLIENT_SECRET)
    
    if posts:
        # Save with compliance metadata
        filename = f'blueprint_posts_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        save_to_csv_with_metadata(posts, filename)
        
        # Show compliance reminder
        print_compliance_reminder()
        
        print(f"\n📁 Data saved to: {filename}")
        print(f"📊 Ready for analysis - focus on insights, not raw content!")
        
    else:
        print("❌ No data collected. Check your credentials and subreddit name.")
