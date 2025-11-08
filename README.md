# 📰 News Aggregator Web Application

A fully-featured web application that aggregates news articles from multiple sources using web scraping techniques,
stores them in a database, and provides a user-friendly interface for browsing and searching articles.

## 🌟 Features

- **Multi-Source Scraping**: Automatically scrapes news from 8+ sources including:
    - BBC News
    - CNN
    - Reuters
    - The Guardian
    - TechCrunch
    - Ars Technica
    - The Verge
    - Hacker News

- **Smart Database Storage**: SQLite database storing:
    - Article titles, URLs, summaries, and full content
    - Publication dates and scraped dates
    - Source information and categories
    - Author information
    - Article images

- **Advanced Search**: Full-text search across titles, summaries, and content

- **Filtering Options**: Filter articles by:
    - Source
    - Category
    - Keywords

- **Modern UI**: Beautiful, responsive design with:
    - Grid and list layouts
    - Gradient backgrounds
    - Smooth animations
    - Mobile-friendly interface

- **Statistics Dashboard**: View aggregated statistics about:
    - Total articles in database
    - Articles by source
    - Articles by category

- **Pagination**: Efficient browsing with 20 articles per page

## 🏗️ Architecture

### Backend

- **Framework**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Scraping**: BeautifulSoup4, feedparser, requests
- **RSS Feed Parsing**: Multiple news sources via RSS feeds

### Frontend

- **Template Engine**: Jinja2
- **Styling**: Pure CSS with modern design patterns
- **JavaScript**: Vanilla JS for dynamic features

## 📋 Requirements

- Python 3.7 or higher
- pip (Python package manager)
- Internet connection (for scraping news)

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project

If you're reading this, you already have the files. Ensure you're in the project directory:

```bash
cd "C:\Users\ADITYA\Desktop\pbls 7th sem\Web Mining"
```

### Step 2: Create a Virtual Environment (Recommended)

Create a virtual environment to isolate project dependencies:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
venv\Scripts\activate.bat

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:

- Flask (web framework)
- Flask-SQLAlchemy (database ORM)
- requests (HTTP library)
- beautifulsoup4 (HTML parsing)
- newspaper3k (article extraction)
- python-dateutil (date parsing)
- feedparser (RSS feed parsing)
- lxml (XML/HTML parser)

### Step 4: Initialize the Database

The database will be automatically created when you first run the application, but you can verify it by running:

```bash
python app.py
```

This creates a `news.db` file in your project directory.

## 🎯 Running the Application

### Start the Server

Run the Flask application:

```bash
python app.py
```

You should see output like:

```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
```

### Access the Application

Open your web browser and navigate to:

```
http://localhost:5000
```

Or:

```
http://127.0.0.1:5000
```

## 📖 Usage Guide

### 1. First-Time Setup: Scrape News Articles

When you first access the application, the database will be empty. Click the **"Refresh News"** button in the navigation
bar to scrape articles from all configured sources.

- The scraping process may take 10-30 seconds
- You'll see a loading spinner while scraping
- A success message will appear showing how many articles were scraped
- The page will automatically reload with the new articles

### 2. Browse Articles

**Home Page** (`/`):

- View all articles in a beautiful grid layout
- Each card shows:
    - Article image (if available)
    - Source and category badges
    - Title
    - Summary
    - Publication date
    - Link to full article

**Filter Options**:

- Use the dropdown filters to view articles from specific sources or categories
- Filters update automatically when changed

**Pagination**:

- Navigate through pages using the pagination controls at the bottom
- 20 articles per page

### 3. Search Articles

**Search Bar**:

- Enter keywords in the search bar in the navigation
- Searches across article titles, summaries, and content
- Shows total number of matching articles
- Results are displayed in list format with pagination

**Search Tips**:

- Use specific keywords for better results
- Search is case-insensitive
- Partial word matches are supported

### 4. View Article Details

Click on any article title to view the full article page:

- Complete article metadata (source, category, author, dates)
- Article image (if available)
- Full summary
- Complete content
- Button to read the original article on the source website
- Back button to return to home page

### 5. View Statistics

Click **"Statistics"** in the navigation to see:

- Total number of articles in the database
- Breakdown of articles by source
- Breakdown of articles by category
- Visual counts for each category

### 6. Refresh News

Click **"Refresh News"** anytime to:

- Fetch the latest articles from all sources
- Add new articles to the database
- Duplicate articles are automatically prevented
- The system scrapes up to 10 articles per source

## 🗂️ Project Structure

```
Web Mining/
├── app.py                  # Main Flask application
├── scraper.py             # News scraping logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── news.db               # SQLite database (created on first run)
├── templates/            # HTML templates
│   ├── base.html        # Base template (not used, standalone templates instead)
│   ├── index.html       # Home page
│   ├── search.html      # Search results page
│   ├── article.html     # Article detail page
│   └── stats.html       # Statistics page
└── static/              # Static files (not used, inline CSS/JS)
```

## 🔧 Configuration

### Adding More News Sources

Edit `scraper.py` and add new RSS feeds to the `rss_feeds` dictionary:

```python
self.rss_feeds = {
    'Source Name': 'https://example.com/rss/feed',
    # Add more sources here
}
```

Also update the `category_map` if needed:

```python
self.category_map = {
    'Source Name': 'Category',
    # Add more mappings here
}
```

### Changing Articles Per Page

Edit `app.py` and modify the `per_page` variable in routes:

```python
per_page = 20  # Change to desired number
```

### Database Location

By default, the database is created as `news.db` in the project directory. To change this, edit `app.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
```

## 🛠️ Troubleshooting

### Issue: "Module not found" errors

**Solution**: Make sure you've installed all dependencies:

```bash
pip install -r requirements.txt
```

### Issue: Scraping returns 0 articles

**Solution**:

- Check your internet connection
- Some RSS feeds may be temporarily unavailable
- Some feeds may have changed their URLs
- Try running the scraper again after a few minutes

### Issue: Port 5000 is already in use

**Solution**: Either:

1. Stop the other application using port 5000
2. Or change the port in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use a different port
```

### Issue: Database errors

**Solution**: Delete `news.db` and restart the application to create a fresh database:

```bash
# On Windows:
del news.db
# On macOS/Linux:
rm news.db

# Then restart the application
python app.py
```

### Issue: SSL Certificate errors during scraping

**Solution**: This can occur with some news sources. The application handles these gracefully and continues with other
sources.

## 🧪 Testing the Application

### Test Scraping

```bash
python -c "from scraper import NewsScraper; from app import db, Article, app; 
with app.app_context(): 
    scraper = NewsScraper(db, Article); 
    print(f'Scraped {scraper.scrape_all_sources()} articles')"
```

### Check Database Contents

```bash
python -c "from app import Article, app; 
with app.app_context(): 
    print(f'Total articles: {Article.query.count()}')"
```

## 📊 API Endpoints

The application also provides a REST API:

### GET /api/articles

Returns articles in JSON format with pagination.

**Parameters**:

- `page` (optional): Page number (default: 1)
- `per_page` (optional): Articles per page (default: 20)

**Example**:

```
http://localhost:5000/api/articles?page=1&per_page=10
```

**Response**:

```json
{
  "articles": [...],
  "total": 150,
  "pages": 15,
  "current_page": 1
}
```

### POST /scrape

Triggers news scraping (returns JSON response).

## 🔐 Security Notes

- This is a development application with `debug=True` enabled
- For production deployment:
    - Set `debug=False`
    - Change the `SECRET_KEY` to a secure random value
    - Use a production WSGI server like Gunicorn
    - Add proper error handling and logging
    - Implement rate limiting for scraping
    - Add user authentication if needed

## 📝 Database Schema

### Article Table

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Primary key |
| title | String(500) | Article title |
| url | String(1000) | Article URL (unique) |
| summary | Text | Article summary/excerpt |
| content | Text | Full article content |
| source | String(200) | News source name |
| category | String(100) | Article category |
| author | String(200) | Article author |
| publication_date | DateTime | Original publication date |
| scraped_date | DateTime | When article was scraped |
| image_url | String(1000) | Article image URL |

## 🚀 Future Enhancements

Potential improvements for the application:

1. **User Features**:
    - User accounts and authentication
    - Bookmarking/favorite articles
    - Reading history
    - Personalized recommendations

2. **Advanced Scraping**:
    - Scheduled automatic scraping (cron jobs)
    - Real-time news updates
    - More news sources
    - Custom source addition via UI

3. **Enhanced Search**:
    - Full-text search with ranking
    - Advanced filters (date range, source combination)
    - Search suggestions/autocomplete

4. **Analytics**:
    - Trending topics
    - Sentiment analysis
    - Topic clustering
    - Word clouds

5. **Export Features**:
    - Export search results to CSV/JSON
    - RSS feed generation
    - Email newsletters

6. **Performance**:
    - Redis caching
    - Elasticsearch for search
    - PostgreSQL for production
    - CDN for static assets

## 📄 License

This project is created for educational purposes as part of the Web Mining course.

## 👥 Credits

- Built with Flask, SQLAlchemy, BeautifulSoup4, and other amazing open-source libraries
- RSS feeds provided by various news organizations
- Modern UI inspired by contemporary web design principles

## 📧 Support

For issues or questions:

1. Check the Troubleshooting section above
2. Review the error messages in the terminal
3. Ensure all dependencies are properly installed
4. Verify your Python version is 3.7+

---

**Happy News Browsing! 📰✨**
