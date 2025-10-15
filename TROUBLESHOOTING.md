# Troubleshooting Guide for Scholar Stats Updates

## Understanding the "403 Forbidden" Error

### What's Happening

When you see this in the GitHub Actions log:
```
Error fetching with requests: 403 Client Error: Forbidden
⚠️ Failed to fetch new stats, keeping existing data
```

**This is NOT a critical error!** Here's why:

### Why Google Scholar Blocks Automated Requests

1. **Anti-Bot Protection**: Google Scholar actively blocks automated scraping to prevent abuse
2. **Rate Limiting**: Making too many requests in a short time triggers blocking
3. **GitHub Actions IP Ranges**: GitHub's runner IPs are well-known and often blocked

### How the System Handles This

✅ **Your website still works!** The system has multiple safety layers:

1. **Primary Method**: Tries to fetch fresh data using `scholarly` library
2. **Fallback #1**: Retries once after a 5-second delay
3. **Fallback #2**: Tries web scraping with better headers
4. **Fallback #3**: Keeps your existing cached data from `scholar-stats.json`
5. **Workflow Passes**: The GitHub Action doesn't fail, so you don't get error emails

### Current Status

- ✅ **Workflow runs daily at 03:17 UTC**
- ✅ **Stats are cached** in `scholar-stats.json` (last updated: 2025-10-15)
- ✅ **Website displays stats** from the cached file
- ✅ **No errors visible to visitors**
- ⚠️ **Updates may be blocked** by Google's anti-bot measures (but that's okay!)

## Solutions & Workarounds

### Option 1: Accept the Current Behavior (Recommended)

**Best for most users**: Your website works perfectly, showing cached stats. Google Scholar stats don't change frequently enough to worry about daily updates being blocked.

**Pros**:
- No maintenance required
- No cost
- Website always shows data
- Workflow doesn't fail

**Cons**:
- Stats might be a few days/weeks old during blocking periods
- Eventually will update when blocks lift

### Option 2: Manual Updates

When you notice stats are outdated, manually trigger an update:

1. Go to your GitHub repository
2. Click on **Actions** tab
3. Click on **"Update Google Scholar Stats"** workflow
4. Click **"Run workflow"** button
5. Select branch and click **"Run workflow"**

Sometimes manual runs from different times/IPs succeed when automated ones don't.

### Option 3: Use ScraperAPI (Paid Service)

For guaranteed daily updates, use a professional scraping API:

**Cost**: ~$29/month for 100,000 requests (you only need ~30/month)

**Implementation**:
1. Sign up at [ScraperAPI](https://www.scraperapi.com/)
2. Get your API key
3. Add it as a GitHub Secret: `SCRAPER_API_KEY`
4. Update the script to use ScraperAPI proxy

I can help implement this if you want guaranteed updates.

### Option 4: Reduce Update Frequency

Change from daily to weekly or monthly updates to reduce blocking:

**For Weekly** (every Monday):
```yaml
cron: '17 3 * * 1'
```

**For Monthly** (1st of each month):
```yaml
cron: '17 3 1 * *'
```

This reduces the chance of being blocked.

## Monitoring Your Stats

### Check if Stats Are Up to Date

1. **Look at the date** on your website (shown in the stats section)
2. **Check the JSON file**: View `scholar-stats.json` on GitHub
3. **View commit history**: Look for automated commits with 🤖

### Check Workflow Status

1. Go to your repository
2. Click **Actions** tab
3. Look for green checkmarks ✅ (success) or red X's ❌ (failure)
4. Click on any run to see detailed logs

### What Success Looks Like

When the update **succeeds**, you'll see:
```
✅ Scholar stats updated successfully!
   Citations: 154
   Publications: 4
   h-index: 4
   i10-index: 3
```

When it's **blocked but handled gracefully**, you'll see:
```
⚠️ Failed to fetch new stats, keeping existing data
   Existing stats from: 2025-10-15
   Note: Stats were not updated this time
```

Both scenarios result in a ✅ passing workflow!

## When to Worry

You should only investigate if:

❌ The workflow is actually **failing** (red X in Actions)  
❌ The `scholar-stats.json` file is **missing or corrupt**  
❌ Your website shows **"0" for all stats**  
❌ Stats haven't updated in **several months**

## Technical Details

### Current Configuration

- **Schedule**: Daily at 03:17 UTC (less predictable timing)
- **Retry Logic**: Attempts fetch twice with 5-second delay
- **Rate Limiting**: Random 1-3 second delay before first attempt
- **Timeout**: 10 seconds per request
- **Fallback**: Keeps cached data if fetch fails

### Files Involved

- `.github/workflows/update-scholar-stats.yml` - Automation workflow
- `update-scholar-stats.py` - Fetching script
- `scholar-stats.json` - Cached data file
- `script.js` - Website display logic

## Getting Help

If you need assistance or want to implement Option 3 (ScraperAPI), let me know!

---

**Last Updated**: October 15, 2025  
**System Status**: ✅ Operational (with expected Google blocking)
