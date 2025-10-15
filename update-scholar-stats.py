#!/usr/bin/env python3
"""
Google Scholar Stats Updater
This script fetches your Google Scholar statistics and updates the scholar-stats.json file.
Run this script periodically (weekly/monthly) to keep your stats up to date.

Requirements:
    pip install scholarly
    or
    pip install beautifulsoup4 requests
"""

import json
import sys
import time
import random
from datetime import datetime

# Always import all dependencies
try:
    from scholarly import scholarly, ProxyGenerator
    USE_SCHOLARLY = True
except ImportError:
    USE_SCHOLARLY = False
    print("Warning: scholarly library not available")

try:
    import requests
    from bs4 import BeautifulSoup
    USE_REQUESTS = True
except ImportError:
    USE_REQUESTS = False
    print("Warning: requests/beautifulsoup4 not available")

# Check if we're running in GitHub Actions
import os
IS_GITHUB_ACTIONS = os.getenv('GITHUB_ACTIONS') == 'true'

def fetch_stats_with_scholarly(author_id, use_proxy=False):
    """Fetch stats using the scholarly library"""
    try:
        # scholarly library has built-in mechanisms to handle rate limiting
        print("Initializing scholarly...")
        
        # If running in GitHub Actions and use_proxy is True, try to use FreeProxy
        if use_proxy and IS_GITHUB_ACTIONS:
            try:
                print("Attempting to use free proxy to bypass rate limits...")
                pg = ProxyGenerator()
                success = pg.FreeProxies()
                if success:
                    scholarly.use_proxy(pg)
                    print("✓ Proxy configured successfully")
                else:
                    print("⚠️  Proxy setup failed, using direct connection")
            except Exception as proxy_error:
                print(f"⚠️  Could not setup proxy: {proxy_error}")
                print("   Continuing with direct connection...")
        
        # Search for the author
        print(f"Searching for author ID: {author_id}")
        search_query = scholarly.search_author_id(author_id)
        
        print("Filling author details...")
        author = scholarly.fill(search_query)
        
        citations = author.get('citedby', 0)
        hindex = author.get('hindex', 0)
        i10index = author.get('i10index', 0)
        publications = len(author.get('publications', []))
        
        print(f"Successfully fetched: citations={citations}, h-index={hindex}, i10-index={i10index}, pubs={publications}")
        
        return {
            'citations': citations,
            'publications': publications,
            'hIndex': hindex,
            'i10Index': i10index,
            'lastUpdated': datetime.now().strftime('%Y-%m-%d')
        }
    except Exception as e:
        print(f"Error fetching with scholarly: {e}")
        import traceback
        traceback.print_exc()
        return None

def fetch_stats_with_requests(author_id):
    """Fetch stats using web scraping with better headers"""
    try:
        url = f"https://scholar.google.com/citations?user={author_id}&hl=en"
        
        # Rotate between different user agents to avoid detection
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
        ]
        
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
        
        # Add session to maintain cookies
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        
        # Check for 403 (Forbidden) specifically
        if response.status_code == 403:
            print(f"⚠️  Got 403 Forbidden - Google Scholar is blocking automated requests")
            print("    This is common from GitHub Actions and CI environments")
            return None
        
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Debug: Print page title to confirm we got the right page
        page_title = soup.find('title')
        if page_title:
            print(f"Page title: {page_title.text}")
        
        # Extract citation stats
        stats_table = soup.find('table', {'id': 'gsc_rsb_st'})
        if stats_table:
            stats_cells = stats_table.find_all('td', {'class': 'gsc_rsb_std'})
            if len(stats_cells) >= 5:
                citations = int(stats_cells[0].text.replace(',', ''))
                hindex = int(stats_cells[2].text)
                i10index = int(stats_cells[4].text)
                print(f"Found stats: Citations={citations}, h-index={hindex}, i10-index={i10index}")
            else:
                print(f"Warning: Expected 5+ stat cells, found {len(stats_cells)}")
                citations = hindex = i10index = 0
        else:
            print("Warning: Stats table not found on page")
            citations = hindex = i10index = 0
        
        # Count publications
        publication_rows = soup.find_all('tr', {'class': 'gsc_a_tr'})
        publications = len(publication_rows)
        print(f"Found {publications} publications")
        
        if citations > 0 or publications > 0:
            return {
                'citations': citations,
                'publications': publications,
                'hIndex': hindex,
                'i10Index': i10index,
                'lastUpdated': datetime.now().strftime('%Y-%m-%d')
            }
        else:
            print("Warning: No valid stats found")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        import traceback
        traceback.print_exc()
        return None
    except Exception as e:
        print(f"Error fetching with requests: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    # Your Google Scholar author ID
    SCHOLAR_ID = '6gRlYHAAAAAJ'
    
    print("=" * 60)
    print("Fetching Google Scholar statistics...")
    print(f"Author ID: {SCHOLAR_ID}")
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Add random delay to avoid rate limiting (2-5 seconds)
    delay = random.uniform(2, 5)
    print(f"Waiting {delay:.1f} seconds to avoid rate limiting...")
    time.sleep(delay)
    
    # Try multiple methods with retries
    stats = None
    max_retries = 2  # Reduced to 2 to avoid too many failed attempts
    
    # Method 1: Try scholarly library first (better anti-bot protection)
    if USE_SCHOLARLY and not stats:
        # First try without proxy
        print(f"\n--- Attempt 1/{max_retries} using scholarly library (direct) ---")
        stats = fetch_stats_with_scholarly(SCHOLAR_ID, use_proxy=False)
        
        if stats:
            print("✓ Successfully fetched stats via scholarly library (direct)")
        elif IS_GITHUB_ACTIONS:
            # If direct failed and we're in GitHub Actions, try with proxy
            print("✗ Direct connection failed in GitHub Actions")
            print(f"\n--- Attempt 2/{max_retries} using scholarly library (with proxy) ---")
            time.sleep(5)
            stats = fetch_stats_with_scholarly(SCHOLAR_ID, use_proxy=True)
            
            if stats:
                print("✓ Successfully fetched stats via scholarly library (with proxy)")
        else:
            # Not in GitHub Actions, try one more time without proxy
            print(f"\n--- Attempt 2/{max_retries} using scholarly library (retry) ---")
            time.sleep(5)
            stats = fetch_stats_with_scholarly(SCHOLAR_ID, use_proxy=False)
            
            if stats:
                print("✓ Successfully fetched stats via scholarly library (retry)")
    
    # Method 2: Try web scraping as fallback (less reliable from CI)
    if USE_REQUESTS and not stats:
        print("\n--- Note: Web scraping from GitHub Actions often gets blocked by Google ---")
        print("--- Trying anyway with extra precautions ---")
        for attempt in range(max_retries):
            print(f"\n--- Attempt {attempt + 1}/{max_retries} using web scraping ---")
            stats = fetch_stats_with_requests(SCHOLAR_ID)
            
            if stats:
                print("✓ Successfully fetched stats via web scraping")
                break
            else:
                if attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 5
                    print(f"✗ Failed. Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
    
    print("\n" + "=" * 60)
    
    if stats:
        # Validate stats before saving
        if stats.get('citations', 0) == 0 and stats.get('publications', 0) == 0:
            print("⚠️ Warning: Fetched stats appear to be empty (all zeros)")
            print("   Checking if existing data is available...")
            
            try:
                with open('scholar-stats.json', 'r') as f:
                    existing_stats = json.load(f)
                    if existing_stats.get('citations', 0) > 0:
                        print("   Keeping existing stats as fetched data seems invalid")
                        print(f"   Existing stats from: {existing_stats.get('lastUpdated', 'unknown')}")
                        sys.exit(0)
            except FileNotFoundError:
                pass
        
        # Save to JSON file
        with open('scholar-stats.json', 'w') as f:
            json.dump(stats, f, indent=2)
        
        print("✅ Scholar stats updated successfully!")
        print(f"   Citations: {stats['citations']}")
        print(f"   Publications: {stats['publications']}")
        print(f"   h-index: {stats['hIndex']}")
        print(f"   i10-index: {stats['i10Index']}")
        print(f"   Last updated: {stats['lastUpdated']}")
        print("=" * 60)
    else:
        print("⚠️ All methods failed to fetch new stats")
        if IS_GITHUB_ACTIONS:
            print("   💡 Google Scholar often blocks GitHub Actions IPs (403 Forbidden)")
            print("   💡 This is expected behavior and not a bug in the script")
        
        # Check if existing file exists
        try:
            with open('scholar-stats.json', 'r') as f:
                existing_stats = json.load(f)
                print(f"\n✓ Existing stats file found (from: {existing_stats.get('lastUpdated', 'unknown')})")
                print("   Citations:", existing_stats.get('citations', 'N/A'))
                print("   Publications:", existing_stats.get('publications', 'N/A'))
                print("   h-index:", existing_stats.get('hIndex', 'N/A'))
                print("   i10-index:", existing_stats.get('i10Index', 'N/A'))
                print("\n   ℹ️  Note: Using existing data (stats not updated this run)")
                print("   ℹ️  Website will continue to display the last successfully fetched data")
                print("   ℹ️  The workflow will automatically retry on the next scheduled run")
                print("=" * 60)
                # Exit with 0 to not fail the workflow when data already exists
                sys.exit(0)
        except FileNotFoundError:
            print("\n❌ No existing stats file found and failed to fetch new data")
            print("   This may be due to Google Scholar rate limiting or network issues")
            print("   The workflow will retry on the next scheduled run")
            print("=" * 60)
            sys.exit(1)

if __name__ == "__main__":
    main()
