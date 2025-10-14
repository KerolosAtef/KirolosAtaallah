# Google Scholar Auto-Update System

This system automatically fetches and displays your Google Scholar statistics (citations, publications) on your website.

## 🎯 Features

- **Automatic Citation Count**: Displays total citations from Google Scholar
- **Publication Count**: Shows the number of published papers
- **Auto-Update**: Updates weekly via GitHub Actions
- **Fallback Support**: Uses cached values if live fetch fails
- **No Backend Required**: Works entirely on GitHub Pages

## 📊 What Gets Updated

1. **Total Citations** - Replaces "AWS Certifications" stat with live citation count
2. **Published Papers** - Automatically counts your publications
3. **Additional Info** - Includes h-index and i10-index as tooltip

## 🔧 How It Works

### Method 1: Automatic (Recommended)

The GitHub Actions workflow runs automatically every Monday at midnight:

1. Fetches your Google Scholar profile data
2. Extracts citations, publications, h-index, i10-index
3. Updates `scholar-stats.json` file
4. Commits changes to GitHub
5. Website automatically displays updated stats

### Method 2: Manual Update

Run the update script manually:

```bash
# Install dependencies
pip install scholarly beautifulsoup4 requests

# Run the update script
python update-scholar-stats.py
```

### Method 3: Live Fetch (Backup)

The website also tries to fetch live data directly when the page loads using a CORS proxy.

## 📝 Setup Instructions

### 1. Enable GitHub Actions

The workflow file is already created at `.github/workflows/update-scholar-stats.yml`

GitHub Actions should work automatically, but verify:
- Go to your repository on GitHub
- Click "Actions" tab
- You should see "Update Google Scholar Stats" workflow
- Click "Enable workflow" if needed

### 2. Manual Test

Test the workflow manually:
- Go to Actions tab
- Select "Update Google Scholar Stats"
- Click "Run workflow"
- Check if `scholar-stats.json` gets updated

### 3. Verify on Website

Visit your website and check the "About" section stats:
- "Published Papers" should show your current count
- "Total Citations" should replace "AWS Certifications"
- Hover over the citation count to see h-index and i10-index

## 🔄 Update Frequency

- **Automatic**: Every Monday at midnight UTC
- **Manual**: Run `python update-scholar-stats.py` anytime
- **Live Fetch**: Every time someone visits your website (fallback)

## 🛠️ Customization

### Change Update Schedule

Edit `.github/workflows/update-scholar-stats.yml`:

```yaml
on:
  schedule:
    - cron: '0 0 * * 1'  # Change this line
```

Examples:
- Daily: `'0 0 * * *'`
- Weekly (Wednesday): `'0 0 * * 3'`
- Monthly: `'0 0 1 * *'`

### Keep AWS Certifications Instead

If you want to keep AWS Certifications and add citations elsewhere:

1. Edit `index.html` to add a 5th stat item
2. Edit `script.js` `updateStats()` function to target the new element

## 📊 Current Stats Format

```json
{
  "citations": 150,
  "publications": 3,
  "hIndex": 3,
  "i10Index": 2,
  "lastUpdated": "2025-10-15"
}
```

## 🐛 Troubleshooting

### Stats Not Updating?

1. Check GitHub Actions logs:
   - Go to Actions tab
   - Click on the latest workflow run
   - Check for errors

2. Verify scholar-stats.json:
   - Check if file exists
   - Check lastUpdated date
   - Verify values are correct

3. Check browser console:
   - Press F12 on your website
   - Look for JavaScript errors
   - Check network tab for failed requests

### Google Scholar Blocking Requests?

Google Scholar may block automated requests. Solutions:

1. Use the GitHub Actions workflow (runs from GitHub servers)
2. Manual updates are more reliable
3. The cached JSON file ensures stats always display

## 📈 Future Enhancements

Possible improvements:
- Add graph showing citation growth over time
- Display recent publications
- Show co-author network
- Add publication impact metrics

## 🔒 Privacy & Rate Limiting

- Only public Google Scholar data is accessed
- No authentication required
- Respects Google's rate limits
- Uses caching to minimize requests

---

**Your Google Scholar ID**: `6gRlYHAAAAAJ`

**Profile URL**: https://scholar.google.com/citations?user=6gRlYHAAAAAJ
