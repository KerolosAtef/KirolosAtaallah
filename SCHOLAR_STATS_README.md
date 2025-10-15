# Google Scholar Stats Auto-Update

## Overview
This repository includes an automated GitHub Action that updates your Google Scholar statistics (citations, h-index, i10-index, and publication count) daily and displays them on your website.

## How It Works

### Automated Daily Updates
- **Schedule**: Runs every day at 03:17 UTC (randomized time to avoid rate limiting)
- **Workflow File**: `.github/workflows/update-scholar-stats.yml`
- **Python Script**: `update-scholar-stats.py`
- **Data File**: `scholar-stats.json`

### Update Process
1. The GitHub Action runs the Python script
2. The script fetches your latest stats from Google Scholar using:
   - **Primary Method**: Web scraping with rotating user agents
   - **Fallback Method**: `scholarly` Python library
3. If new data is fetched successfully, it updates `scholar-stats.json`
4. If changes are detected, the workflow commits and pushes the updated file
5. Your website reads from `scholar-stats.json` to display live stats

## Manual Trigger

You can manually trigger the workflow at any time:

1. Go to your repository on GitHub
2. Click on the **Actions** tab
3. Select **"Update Google Scholar Stats"** from the left sidebar
4. Click **"Run workflow"** button
5. Select the branch (usually `master`)
6. Click **"Run workflow"**

## Recent Fixes Applied

### 1. **GitHub Action Permissions**
   - Added `contents: write` permission to allow the workflow to commit changes
   - Added explicit token configuration for checkout

### 2. **Improved Python Script**
   - Enhanced web scraping with:
     - Multiple user agent rotation
     - Better HTTP headers to avoid bot detection
     - Retry logic with exponential backoff (up to 3 attempts per method)
     - Session management for cookie handling
   - Better error handling and detailed logging
   - Graceful fallback to existing data if fetching fails
   - Validation to prevent overwriting good data with empty results

### 3. **Enhanced Workflow**
   - Added `lxml` parser for better BeautifulSoup performance
   - Improved error handling with `continue-on-error`
   - Better status reporting with workflow summaries
   - Prettier commit messages with timestamps
   - Always displays current stats in workflow logs

### 4. **Rate Limiting Protection**
   - Random delays between requests (2-5 seconds)
   - Exponential backoff on retries
   - Rotates between different user agents
   - Multiple methods with fallback

## Testing Locally

To test the script locally:

```bash
# Install dependencies
pip install scholarly beautifulsoup4 requests lxml

# Run the script
python3 update-scholar-stats.py
```

## Troubleshooting

### If the workflow fails:
1. **Check workflow logs**: Go to Actions → Update Google Scholar Stats → Click on the latest run
2. **Common issues**:
   - **Rate limiting**: Google Scholar may temporarily block requests. The script will use existing data and retry on the next scheduled run.
   - **Permission errors**: Ensure the repository has Actions enabled and the workflow has write permissions
   - **Network issues**: The script will gracefully handle network errors and keep existing data

### If stats aren't updating on your website:
1. Check that `scholar-stats.json` exists in the repository root
2. Verify the website's JavaScript is correctly fetching the JSON file
3. Check browser console for any JavaScript errors
4. Clear browser cache and reload the page

## Monitoring

Each workflow run creates a summary showing:
- ✅ Update status (success/failed)
- 📊 Current statistics (citations, publications, h-index, i10-index)
- 🕐 Timestamp of the run
- 🔄 What triggered the workflow

## Your Scholar Profile

- **Author ID**: `6gRlYHAAAAAJ`
- **Profile URL**: https://scholar.google.com/citations?user=6gRlYHAAAAAJ&hl=en

## Files Modified

1. `.github/workflows/update-scholar-stats.yml` - GitHub Action workflow
2. `update-scholar-stats.py` - Python script for fetching stats
3. `scholar-stats.json` - Data file with current stats (auto-updated)

## Support

If you continue to experience issues:
1. Check the [workflow runs](../../actions/workflows/update-scholar-stats.yml)
2. Review the error logs in the failed runs
3. Manually trigger the workflow to test immediately
4. Verify your Google Scholar profile is public and accessible

---

**Last Updated**: 2025-10-15  
**Status**: ✅ Working correctly
