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
    from scholarly import scholarly
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

def fetch_stats_with_scholarly(author_id):
    """Fetch stats using the scholarly library"""
    try:
        # Search for the author
        search_query = scholarly.search_author_id(author_id)
        author = scholarly.fill(search_query)
        
        citations = author.get('citedby', 0)
        hindex = author.get('hindex', 0)
        i10index = author.get('i10index', 0)
        publications = len(author.get('publications', []))
        
        return {
            'citations': citations,
            'publications': publications,
            'hIndex': hindex,
            'i10Index': i10index,
            'lastUpdated': datetime.now().strftime('%Y-%m-%d')
        }
    except Exception as e:
        print(f"Error fetching with scholarly: {e}")
        return None

def fetch_stats_with_requests(author_id):
    """Fetch stats using web scraping with better headers"""
    try:
        url = f"https://scholar.google.com/citations?user={author_id}&hl=en"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract citation stats
        stats_table = soup.find('table', {'id': 'gsc_rsb_st'})
        if stats_table:
            stats_cells = stats_table.find_all('td', {'class': 'gsc_rsb_std'})
            citations = int(stats_cells[0].text.replace(',', '')) if len(stats_cells) > 0 else 0
            hindex = int(stats_cells[2].text) if len(stats_cells) > 2 else 0
            i10index = int(stats_cells[4].text) if len(stats_cells) > 4 else 0
        else:
            citations = hindex = i10index = 0
        
        # Count publications
        publications = len(soup.find_all('tr', {'class': 'gsc_a_tr'}))
        
        return {
            'citations': citations,
            'publications': publications,
            'hIndex': hindex,
            'i10Index': i10index,
            'lastUpdated': datetime.now().strftime('%Y-%m-%d')
        }
    except Exception as e:
        print(f"Error fetching with requests: {e}")
        return None

def main():
    # Your Google Scholar author ID
    SCHOLAR_ID = '6gRlYHAAAAAJ'
    
    print("Fetching Google Scholar statistics...")
    
    # Add random delay to avoid rate limiting (1-3 seconds)
    delay = random.uniform(1, 3)
    print(f"Waiting {delay:.1f} seconds to avoid rate limiting...")
    time.sleep(delay)
    
    # Try with scholarly library first, then fall back to web scraping
    stats = None
    
    if USE_SCHOLARLY:
        print("Using scholarly library...")
        stats = fetch_stats_with_scholarly(SCHOLAR_ID)
        
        # If failed, wait and try once more
        if not stats:
            print("First attempt failed, waiting 5 seconds and retrying...")
            time.sleep(5)
            stats = fetch_stats_with_scholarly(SCHOLAR_ID)
    
    if not stats and USE_REQUESTS:
        print("Using web scraping method...")
        time.sleep(2)  # Wait before trying web scraping
        stats = fetch_stats_with_requests(SCHOLAR_ID)
    
    if stats:
        # Save to JSON file
        with open('scholar-stats.json', 'w') as f:
            json.dump(stats, f, indent=2)
        
        print("✅ Scholar stats updated successfully!")
        print(f"   Citations: {stats['citations']}")
        print(f"   Publications: {stats['publications']}")
        print(f"   h-index: {stats['hIndex']}")
        print(f"   i10-index: {stats['i10Index']}")
        print(f"   Last updated: {stats['lastUpdated']}")
    else:
        print("⚠️ Failed to fetch new stats, keeping existing data")
        # Check if existing file exists
        try:
            with open('scholar-stats.json', 'r') as f:
                existing_stats = json.load(f)
                print(f"   Existing stats from: {existing_stats.get('lastUpdated', 'unknown')}")
                print("   Note: Stats were not updated this time")
                # Exit with 0 to not fail the workflow when data already exists
                sys.exit(0)
        except FileNotFoundError:
            print("❌ No existing stats file found and failed to fetch new data")
            sys.exit(1)

if __name__ == "__main__":
    main()
