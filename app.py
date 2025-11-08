from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from scraper import NewsScraper

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)

# Database Models
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(1000), unique=True, nullable=False)
    summary = db.Column(db.Text)
    content = db.Column(db.Text)
    source = db.Column(db.String(200))
    category = db.Column(db.String(100))
    author = db.Column(db.String(200))
    publication_date = db.Column(db.DateTime)
    scraped_date = db.Column(db.DateTime, default=datetime.utcnow)
    image_url = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Article {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'url': self.url,
            'summary': self.summary,
            'content': self.content,
            'source': self.source,
            'category': self.category,
            'author': self.author,
            'publication_date': self.publication_date.strftime('%Y-%m-%d %H:%M') if self.publication_date else None,
            'scraped_date': self.scraped_date.strftime('%Y-%m-%d %H:%M'),
            'image_url': self.image_url
        }

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Home page displaying all articles"""
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    # Get filter parameters
    category = request.args.get('category', '')
    source = request.args.get('source', '')
    
    query = Article.query
    
    if category:
        query = query.filter(Article.category.ilike(f'%{category}%'))
    if source:
        query = query.filter(Article.source.ilike(f'%{source}%'))
    
    articles = query.order_by(Article.publication_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    # Get unique categories and sources for filters
    categories = db.session.query(Article.category).distinct().filter(Article.category.isnot(None)).all()
    sources = db.session.query(Article.source).distinct().filter(Article.source.isnot(None)).all()
    
    return render_template('index.html', 
                         articles=articles,
                         categories=[c[0] for c in categories if c[0]],
                         sources=[s[0] for s in sources if s[0]],
                         current_category=category,
                         current_source=source)

@app.route('/search')
def search():
    """Search articles by keyword"""
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    per_page = 20
    
    if query:
        articles = Article.query.filter(
            db.or_(
                Article.title.ilike(f'%{query}%'),
                Article.summary.ilike(f'%{query}%'),
                Article.content.ilike(f'%{query}%')
            )
        ).order_by(Article.publication_date.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
    else:
        articles = Article.query.order_by(Article.publication_date.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    return render_template('search.html', articles=articles, query=query)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    """Display full article details"""
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', article=article)

@app.route('/scrape', methods=['POST'])
def scrape_news():
    """Trigger news scraping"""
    try:
        scraper = NewsScraper(db, Article)
        count = scraper.scrape_all_sources()
        return jsonify({'success': True, 'message': f'Successfully scraped {count} new articles'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@app.route('/api/articles')
def api_articles():
    """API endpoint for articles"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    
    articles = Article.query.order_by(Article.publication_date.desc()).paginate(
        page=page, per_page=per_page, error_out=False
    )
    
    return jsonify({
        'articles': [article.to_dict() for article in articles.items],
        'total': articles.total,
        'pages': articles.pages,
        'current_page': page
    })

@app.route('/stats')
def stats():
    """Display statistics about the articles"""
    total_articles = Article.query.count()
    sources = db.session.query(Article.source, db.func.count(Article.id)).group_by(Article.source).all()
    categories = db.session.query(Article.category, db.func.count(Article.id)).group_by(Article.category).all()
    
    return render_template('stats.html', 
                         total_articles=total_articles,
                         sources=sources,
                         categories=categories)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
