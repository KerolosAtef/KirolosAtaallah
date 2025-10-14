# Professional Portfolio Website

[![Update Google Scholar Stats](https://github.com/kirlos_ataallah/kirlos_ataallah.github.io/actions/workflows/update-scholar-stats.yml/badge.svg)](https://github.com/kirlos_ataallah/kirlos_ataallah.github.io/actions/workflows/update-scholar-stats.yml)

Personal website for **Kirolos Ataallah** - AI Researcher and Developer

🔗 **Live Site**: [https://kirlos-ataallah.github.io](https://kirlos-ataallah.github.io)

## Features

- 📊 **Auto-updating Google Scholar Statistics** - Citations, publications, h-index, and i10-index updated daily
- 🎨 **Modern Responsive Design** - Clean, professional layout that works on all devices
- 🔍 **SEO Optimized** - Meta tags, Open Graph, Twitter Cards, and Schema.org structured data
- 📱 **Mobile-First** - Optimized for all screen sizes
- ⚡ **Fast & Lightweight** - Pure HTML/CSS/JavaScript with no frameworks

## Automated Scholar Stats Updates

The website automatically fetches and updates Google Scholar statistics **every day at midnight UTC**.

### How It Works

1. **GitHub Actions Workflow** runs daily (`0 0 * * *` cron schedule)
2. **Python Script** fetches latest stats from Google Scholar
3. **JSON Cache** is updated with new data
4. **Changes are committed** automatically to the repository
5. **Website displays** updated stats on next visit

### Monitoring the Automation

You can verify the automation is working by:

1. **Check the badge** at the top of this README (green = passing)
2. **View workflow runs** in the [Actions tab](https://github.com/kirlos_ataallah/kirlos_ataallah.github.io/actions/workflows/update-scholar-stats.yml)
3. **Check commit history** for automated updates (look for commits with 🤖)
4. **View the stats file** at [scholar-stats.json](scholar-stats.json)

### Manual Trigger

You can also manually trigger an update:

1. Go to the [Actions tab](https://github.com/kirlos_ataallah/kirlos_ataallah.github.io/actions)
2. Click on "Update Google Scholar Stats" workflow
3. Click "Run workflow" button
4. Select the branch and click "Run workflow"

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Variables, Flexbox, Grid
- **Icons**: Font Awesome 6
- **Fonts**: Inter (Google Fonts)
- **Automation**: GitHub Actions
- **Data Fetching**: Python with `scholarly` library
- **Hosting**: GitHub Pages

## SEO Features

✅ Comprehensive meta tags  
✅ Open Graph tags for social sharing  
✅ Twitter Card support  
✅ Schema.org JSON-LD structured data  
✅ XML Sitemap  
✅ Robots.txt  
✅ Semantic HTML5 structure

## Project Structure

```
.
├── index.html                          # Main website file
├── styles.css                          # All styling
├── script.js                           # Interactive features & Scholar stats fetching
├── scholar-stats.json                  # Cached Google Scholar data
├── update-scholar-stats.py            # Python script to fetch Scholar stats
├── sitemap.xml                         # SEO sitemap
├── robots.txt                          # Crawler instructions
├── SEO_STRATEGY.md                     # SEO documentation
├── SCHOLAR_STATS_README.md            # Scholar stats system documentation
├── .github/workflows/
│   └── update-scholar-stats.yml       # Daily automation workflow
└── assets/
    ├── profile.jpg                     # Profile photo
    ├── favicon.svg                     # SVG favicon
    └── favicon.png                     # PNG favicon fallback
```

## Local Development

To work on this website locally:

```bash
# Clone the repository
git clone https://github.com/kirlos_ataallah/kirlos_ataallah.github.io.git
cd kirlos_ataallah.github.io

# Open in browser (or use a local server)
# For example with Python:
python -m http.server 8000

# Or with Node.js http-server:
npx http-server
```

Visit `http://localhost:8000` in your browser.

## Updating Scholar Stats Locally

```bash
# Install Python dependencies
pip install scholarly beautifulsoup4 requests

# Run the update script
python update-scholar-stats.py

# Commit the changes
git add scholar-stats.json
git commit -m "Update Google Scholar statistics"
git push
```

## Deployment

The website is automatically deployed via GitHub Pages when you push to the `master` branch.

1. Make your changes
2. Commit and push to GitHub
3. Wait a few minutes for GitHub Pages to rebuild
4. Visit your site to see the updates

## License

© 2024 Kirolos Ataallah. All rights reserved.

---

**Last Updated**: January 2025  
**Automated Updates**: ✅ Active (Daily at 00:00 UTC)
