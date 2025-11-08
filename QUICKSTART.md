# 🚀 Quick Start Guide - News Aggregator

## Setup in 5 Minutes

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

### 3. Open in Browser

Navigate to: `http://localhost:5000`

### 4. Scrape News

Click the green **"Refresh News"** button in the navigation bar.

Wait 10-30 seconds for articles to be scraped.

### 5. Start Browsing!

- Browse articles on the home page
- Use filters to find specific sources or categories
- Search using the search bar
- Click article titles to read full details
- View statistics in the Stats page

---

## Troubleshooting

**If you get "Module not found" errors:**

```bash
pip install Flask Flask-SQLAlchemy requests beautifulsoup4 feedparser python-dateutil lxml
```

**If port 5000 is in use:**
Edit `app.py` and change the port:

```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

**To reset the database:**

```bash
# Delete the database file
del news.db    # Windows
rm news.db     # macOS/Linux

# Restart the app
python app.py
```

---

## Key Features

✅ **Multi-source scraping** - 8+ news sources  
✅ **Smart search** - Full-text search across all content  
✅ **Filtering** - By source and category  
✅ **Beautiful UI** - Modern, responsive design  
✅ **Statistics** - View aggregated data  
✅ **Pagination** - Easy navigation through articles

---

For detailed documentation, see [README.md](README.md)
