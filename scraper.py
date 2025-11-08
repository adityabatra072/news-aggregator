import requests
from bs4 import BeautifulSoup
import feedparser
from datetime import datetime
from dateutil import parser as date_parser
import time
import re

class NewsScraper:
    def __init__(self, db, Article):
        self.db = db
        self.Article = Article
        
        # RSS feeds from various news sources
        self.rss_feeds = {
            'BBC News': 'http://feeds.bbci.co.uk/news/rss.xml',
            'CNN': 'http://rss.cnn.com/rss/cnn_topstories.rss',
            'Reuters': 'https://www.reutersagency.com/feed/',
            'The Guardian': 'https://www.theguardian.com/world/rss',
            'TechCrunch': 'https://techcrunch.com/feed/',
            'Ars Technica': 'http://feeds.arstechnica.com/arstechnica/index',
            'The Verge': 'https://www.theverge.com/rss/index.xml',
            'Hacker News': 'https://hnrss.org/frontpage',
        }
        
        # Category mapping based on source
        self.category_map = {
            'TechCrunch': 'Technology',
            'Ars Technica': 'Technology',
            'The Verge': 'Technology',
            'Hacker News': 'Technology',
            'BBC News': 'General',
            'CNN': 'General',
            'Reuters': 'General',
            'The Guardian': 'World',
        }
    
    def clean_html(self, html_text):
        """Remove HTML tags and clean text"""
        if not html_text:
            return ""
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.get_text().strip()
    
    def parse_date(self, date_string):
        """Parse various date formats"""
        if not date_string:
            return datetime.utcnow()
        
        try:
            # Try parsing the date
            return date_parser.parse(date_string)
        except:
            return datetime.utcnow()
    
    def extract_summary(self, content, max_length=300):
        """Extract a summary from content"""
        if not content:
            return ""
        
        # Clean HTML
        clean_content = self.clean_html(content)
        
        # Get first paragraph or truncate
        paragraphs = clean_content.split('\n')
        first_para = next((p for p in paragraphs if len(p) > 50), clean_content)
        
        if len(first_para) > max_length:
            return first_para[:max_length].rsplit(' ', 1)[0] + '...'
        return first_para
    
    def scrape_rss_feed(self, source_name, feed_url):
        """Scrape articles from an RSS feed"""
        articles_added = 0
        
        try:
            print(f"Scraping {source_name}...")
            feed = feedparser.parse(feed_url)
            
            for entry in feed.entries[:10]:  # Limit to 10 articles per source
                try:
                    # Check if article already exists
                    existing = self.Article.query.filter_by(url=entry.link).first()
                    if existing:
                        continue
                    
                    # Extract article data
                    title = entry.get('title', 'No Title')
                    url = entry.get('link', '')
                    
                    # Get summary/description
                    summary = entry.get('summary', entry.get('description', ''))
                    summary = self.extract_summary(summary)
                    
                    # Get full content if available
                    content = entry.get('content', [{}])[0].get('value', '') if 'content' in entry else summary
                    content = self.clean_html(content)
                    
                    # Get publication date
                    pub_date = self.parse_date(entry.get('published', entry.get('updated', '')))
                    
                    # Get author
                    author = entry.get('author', 'Unknown')
                    
                    # Get category
                    category = self.category_map.get(source_name, 'General')
                    if 'tags' in entry and entry.tags:
                        category = entry.tags[0].get('term', category)
                    
                    # Get image URL
                    image_url = None
                    if 'media_content' in entry:
                        image_url = entry.media_content[0].get('url')
                    elif 'media_thumbnail' in entry:
                        image_url = entry.media_thumbnail[0].get('url')
                    
                    # Create article
                    article = self.Article(
                        title=title,
                        url=url,
                        summary=summary,
                        content=content,
                        source=source_name,
                        category=category,
                        author=author,
                        publication_date=pub_date,
                        image_url=image_url
                    )
                    
                    self.db.session.add(article)
                    articles_added += 1
                    
                except Exception as e:
                    print(f"Error processing entry from {source_name}: {str(e)}")
                    continue
            
            self.db.session.commit()
            print(f"Added {articles_added} articles from {source_name}")
            
        except Exception as e:
            print(f"Error scraping {source_name}: {str(e)}")
            self.db.session.rollback()
        
        return articles_added
    
    def scrape_all_sources(self):
        """Scrape all configured news sources"""
        total_articles = 0
        
        for source_name, feed_url in self.rss_feeds.items():
            count = self.scrape_rss_feed(source_name, feed_url)
            total_articles += count
            time.sleep(1)  # Be polite, wait between requests
        
        return total_articles
    
    def scrape_bbc_custom(self):
        """Custom scraper for BBC News (example of web scraping)"""
        try:
            url = "https://www.bbc.com/news"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles_added = 0
            
            # Find article links (BBC structure may vary)
            article_links = soup.find_all('a', class_='gs-c-promo-heading')
            
            for link in article_links[:5]:  # Limit to 5 articles
                try:
                    title = link.get_text().strip()
                    article_url = link.get('href')
                    
                    if not article_url.startswith('http'):
                        article_url = 'https://www.bbc.com' + article_url
                    
                    # Check if exists
                    existing = self.Article.query.filter_by(url=article_url).first()
                    if existing:
                        continue
                    
                    article = self.Article(
                        title=title,
                        url=article_url,
                        summary="",
                        content="",
                        source="BBC News",
                        category="General",
                        publication_date=datetime.utcnow()
                    )
                    
                    self.db.session.add(article)
                    articles_added += 1
                    
                except Exception as e:
                    continue
            
            self.db.session.commit()
            return articles_added
            
        except Exception as e:
            print(f"Error in custom BBC scraper: {str(e)}")
            return 0
