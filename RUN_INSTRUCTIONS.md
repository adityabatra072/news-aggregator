# 🚀 HOW TO RUN THE NEWS AGGREGATOR

## Quick Start (3 Commands)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the application
python app.py

# 3. Open browser to:
http://localhost:5000
```

## Detailed Step-by-Step Guide

### Step 1: Install Dependencies

Open your terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

**Expected Output:**

```
Collecting Flask==3.0.0
  Downloading Flask-3.0.0-py3-none-any.whl
Collecting Flask-SQLAlchemy==3.1.1
  Downloading Flask_SQLAlchemy-3.1.1-py3-none-any.whl
...
Successfully installed Flask-3.0.0 Flask-SQLAlchemy-3.1.1 ...
```

**Time Required:** 1-2 minutes

---

### Step 2: Start the Flask Server

```bash
python app.py
```

**Expected Output:**

```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

**What This Means:**

- ✅ Server is running successfully
- ✅ Database is initialized (news.db created)
- ✅ Application is ready to accept requests
- ⚠️ Keep this terminal window open!

---

### Step 3: Open the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

**What You'll See:**

- Beautiful purple gradient header with "📰 News Aggregator"
- Navigation bar with Home, Statistics, Search, and Refresh News
- Main content area (initially empty or with message)
- Modern, responsive design

---

### Step 4: Fetch News Articles

**Action:** Click the green **"Refresh News"** button in the navigation bar

**What Happens:**

1. A loading spinner appears with "Scraping news articles..."
2. The application fetches articles from 8+ news sources
3. You'll see progress in the terminal:
   ```
   Scraping BBC News...
   Added 10 articles from BBC News
   Scraping CNN...
   Added 8 articles from CNN
   ...
   ```
4. After 10-30 seconds, a success message appears:
   ```
   Successfully scraped XX new articles
   ```
5. The page automatically reloads with articles displayed

---

## 📱 Application Features Tour

### Home Page (/)

**URL:** `http://localhost:5000/`

**What You See:**

- Grid of article cards (3 columns on desktop, 1 on mobile)
- Each card shows:
    - Article image (gradient placeholder if no image)
    - Source badge (blue) and Category badge (purple)
    - Article title (clickable)
    - Summary text
    - Publication date
    - "Read Full Article →" link

**Interactive Elements:**

- **Filter by Source:** Dropdown showing all available sources
- **Filter by Category:** Dropdown showing all categories
- **Pagination:** Navigate through pages (20 articles per page)
- **Hover Effects:** Cards lift up and change border color

---

### Search Page (/search)

**URL:** `http://localhost:5000/search?q=technology`

**How to Use:**

1. Enter keywords in the search bar (e.g., "technology", "politics", "AI")
2. Click "Search" button or press Enter
3. View results

**What You See:**

- Search info box: "Search Results for 'keyword'" with count
- List of matching articles (larger cards than home page)
- Results highlight showing matches
- Pagination if many results

---

### Article Detail Page (/article/:id)

**URL:** `http://localhost:5000/article/1`

**How to Access:**

- Click any article title from home or search pages

**What You See:**

- Large article title
- Source and category badges
- Author name (if available)
- Publication date and scraped date
- Featured image (if available)
- Full article summary in highlighted box
- Complete article content
- "Read Original Article →" button (opens source website)
- "← Back to Home" button

---

### Statistics Page (/stats)

**URL:** `http://localhost:5000/stats`

**What You See:**

- Large number showing total articles in database
- "📰 Articles by Source" card:
    - List of all sources with article counts
    - Color-coded badges
- "🏷️ Articles by Category" card:
    - List of all categories with counts
    - Visual statistics

---

## 🧪 Testing the Application

### Test 1: Verify Installation

```bash
python -c "import flask; print('Flask version:', flask.__version__)"
```

**Expected Output:** `Flask version: 3.0.0`

---

### Test 2: Check Database Creation

After running the app once, check for the database file:

```bash
# On Windows (PowerShell):
ls news.db

# On Windows (Command Prompt):
dir news.db

# On macOS/Linux:
ls -lh news.db
```

**Expected:** File `news.db` exists in the project directory

---

### Test 3: Verify Scraping

```bash
python -c "from scraper import NewsScraper; from app import db, Article, app; with app.app_context(): scraper = NewsScraper(db, Article); print(f'Scraped {scraper.scrape_all_sources()} articles')"
```

**Expected Output:**

```
Scraping BBC News...
Added X articles from BBC News
...
Scraped XX articles
```

---

### Test 4: Check Database Contents

```bash
python -c "from app import Article, app; with app.app_context(): print(f'Total articles: {Article.query.count()}')"
```

**Expected Output:** `Total articles: XX` (where XX > 0)

---

### Test 5: Test Search

**Manual Test:**

1. Navigate to `http://localhost:5000/search?q=test`
2. Verify search results appear
3. Check that search query is preserved in the input box

---

### Test 6: Test Filters

**Manual Test:**

1. Go to home page
2. Select a source from "Filter by Source" dropdown
3. Verify only articles from that source are shown
4. Select a category from "Filter by Category" dropdown
5. Verify filtering works

---

## 📊 Expected Terminal Output

When scraping news, you should see output like:

```
Scraping BBC News...
Added 10 articles from BBC News

Scraping CNN...
Added 7 articles from CNN

Scraping Reuters...
Added 9 articles from Reuters

Scraping The Guardian...
Added 8 articles from The Guardian

Scraping TechCrunch...
Added 10 articles from TechCrunch

Scraping Ars Technica...
Added 10 articles from Ars Technica

Scraping The Verge...
Added 10 articles from The Verge

Scraping Hacker News...
Added 10 articles from Hacker News

127.0.0.1 - - [08/Nov/2025 20:30:00] "POST /scrape HTTP/1.1" 200 -
```

---

## 🎯 Success Indicators

### ✅ Application is Running Correctly If:

1. **Server starts without errors**
    - No Python errors in terminal
    - "Running on http://0.0.0.0:5000" message appears

2. **Database is created**
    - `news.db` file exists in project directory
    - File size increases after scraping

3. **Scraping works**
    - Terminal shows "Added X articles" messages
    - Success message appears in browser
    - Articles appear on home page

4. **UI is functional**
    - Pages load without errors
    - Buttons and links work
    - Search returns results
    - Filters work correctly

5. **Navigation works**
    - Can navigate between pages
    - Back button works
    - Pagination works

---

## 🐛 Common Issues & Solutions

### Issue: Import Errors

**Error Message:**

```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**

```bash
pip install -r requirements.txt
```

---

### Issue: Port Already in Use

**Error Message:**

```
OSError: [Errno 48] Address already in use
```

**Solution:**
Option 1 - Stop other app using port 5000
Option 2 - Change port in app.py:

```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

### Issue: No Articles After Scraping

**Symptoms:**

- Scraping completes but 0 articles added
- "No Articles Found" message persists

**Solutions:**

1. Check internet connection
2. Wait a few minutes and try again (RSS feeds may be down)
3. Check terminal for specific error messages
4. Some news sources may have changed their feed URLs

---

### Issue: Database Lock Error

**Error Message:**

```
sqlite3.OperationalError: database is locked
```

**Solution:**

1. Stop the application (Ctrl+C)
2. Delete news.db
3. Restart application
4. Scrape news again

---

## 📸 Visual Guide - What You Should See

### 1. Home Page (Initial State)

```
┌─────────────────────────────────────────────┐
│ 📰 News Aggregator                          │
│ Your one-stop destination for news          │
├─────────────────────────────────────────────┤
│ Home | Statistics | [Search...] [Refresh]   │
├─────────────────────────────────────────────┤
│                                             │
│      No Articles Found                      │
│  Click "Refresh News" to fetch articles    │
│                                             │
└─────────────────────────────────────────────┘
```

### 2. Home Page (After Scraping)

```
┌─────────────────────────────────────────────┐
│ 📰 News Aggregator                          │
├─────────────────────────────────────────────┤
│ Home | Stats | [Search...] [Refresh News]   │
├─────────────────────────────────────────────┤
│ [Filter by Source ▼] [Filter by Category ▼]│
├─────────────────────────────────────────────┤
│ ┌─────┐ ┌─────┐ ┌─────┐                    │
│ │ CNN │ │ BBC │ │Guard│                    │
│ │ [●] │ │ [●] │ │ian  │                    │
│ │Title│ │Title│ │Title│                    │
│ │Sum..│ │Sum..│ │Sum..│                    │
│ └─────┘ └─────┘ └─────┘                    │
│ [1] 2 3 ... Next →                          │
└─────────────────────────────────────────────┘
```

### 3. Search Results

```
┌─────────────────────────────────────────────┐
│ Search Results for "technology"              │
│ Found 45 articles                           │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ [TechCrunch] [Technology]               │ │
│ │ Article Title About Tech Innovation     │ │
│ │ Summary of the article...              │ │
│ │ Nov 08, 2025 | Read Full Article →    │ │
│ └─────────────────────────────────────────┘ │
│ ┌─────────────────────────────────────────┐ │
│ │ [The Verge] [Technology]                │ │
│ │ Another Tech Article Title             │ │
│ │ Summary...                              │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

---

## 🎬 Complete Demo Flow

1. **Start the app** → `python app.py`
2. **Open browser** → `http://localhost:5000`
3. **Click "Refresh News"** → Wait for scraping
4. **Browse articles** → Scroll through the grid
5. **Try filters** → Select a source or category
6. **Search** → Type "technology" and search
7. **View article** → Click any article title
8. **Check stats** → Click "Statistics" in nav
9. **Refresh again** → Click "Refresh News" for updates

---

## ⏱️ Performance Expectations

- **Initial Load:** < 1 second
- **Scraping Time:** 10-30 seconds (8 sources)
- **Search Response:** < 1 second
- **Page Navigation:** < 1 second
- **Filter Application:** Instant

---

## 🎓 For Demonstration/Presentation

### Recommended Demo Order:

1. **Show empty state** (before scraping)
2. **Trigger scraping** and explain the process
3. **Show populated home page** with articles
4. **Demonstrate filters** by source and category
5. **Perform a search** and show results
6. **Open an article detail** page
7. **Show statistics** dashboard
8. **Explain technical implementation** (code walkthrough)

### Key Points to Highlight:

- Multi-source scraping (8+ sources)
- Smart duplicate prevention
- Full-text search capability
- Beautiful, modern UI
- Responsive design
- Statistics and analytics
- REST API endpoint

---

**🎉 You're all set! Enjoy your News Aggregator!**
