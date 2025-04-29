import os
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, request, render_template, url_for
import praw
import pandas as pd
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
os.makedirs('static/plots', exist_ok=True)
os.makedirs('templates', exist_ok=True)

reddit = praw.Reddit(
    client_id='redit_CLIENT_ID',
    client_secret='redit_client_secret',
    user_agent='BrandSentio'
)
news_api_key = 'NEWS_API_KEY'
analyzer = SentimentIntensityAnalyzer()
def fetch_reddit_posts(subreddit, keyword, limit=90):
    """Fetch and analyze Reddit posts with error handling"""
    try:
        posts = []
        for post in reddit.subreddit(subreddit).search(keyword, limit=limit):
            upvotes = max(post.score, 0)
            downvotes = int((1 - post.upvote_ratio) * (upvotes + abs(post.score))) if post.score < 0 else 0 
            posts.append({
                "title": post.title,
                "upvotes": upvotes,
                "downvotes": downvotes })
        df = pd.DataFrame(posts)
        if df.empty:
            return pd.DataFrame(columns=['title', 'sentiment', 'unique_score']), 0, 0   
        total_upvotes = df['upvotes'].sum()
        total_downvotes = df['downvotes'].sum()
        
        df['sentiment'] = df['title'].apply(lambda x: analyzer.polarity_scores(x)['compound'])
        df['normalized_sentiment'] = (df['sentiment'] + 1) / 2
        df['unique_score'] = (
            0.5 * (df['upvotes']/total_upvotes if total_upvotes > 0 else 0) +
            -0.3 * (df['downvotes']/total_downvotes if total_downvotes > 0 else 0) +
            0.2 * df['normalized_sentiment']
        )
        return df, total_upvotes, total_downvotes   
    except Exception as e:
        print(f"Reddit API Error: {str(e)}")
        return pd.DataFrame(columns=['title', 'sentiment', 'unique_score']), 0, 0
    
def fetch_news_articles(keyword, limit=50):
    """Fetch and analyze news articles with error handling"""
    try:
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={news_api_key}&pageSize={limit}'
        response = requests.get(url)
        response.raise_for_status()
        articles = response.json().get('articles', [])
        
        posts = []
        for article in articles:
            text = f"{article.get('title', '')} {article.get('description', '')}"
            sentiment = analyzer.polarity_scores(text)['compound']
            posts.append({
                "title": article.get('title', 'No Title'),
                "sentiment": sentiment,
                "unique_score": 0.2 * ((sentiment + 1) / 2)
            })

        return pd.DataFrame(posts)
        
    except Exception as e:
        print(f"News API Error: {str(e)}")
        return pd.DataFrame(columns=['title', 'sentiment', 'unique_score'])

def generate_visualizations(reddit_df, news_df, combined_df):
    """Generate all visualizations"""
    try:
        # Combined sentiment
        plt.figure(figsize=(10, 6))
        sns.histplot(combined_df['sentiment'], bins=20, kde=True, color='blue')
        plt.title('Combined Sentiment Distribution')
        plt.savefig('static/plots/sentiment_distribution.png', bbox_inches='tight')
        plt.close()
        
        # Reddit engagement
        if not reddit_df.empty:
            plt.figure(figsize=(8, 8))
            plt.pie(
                [reddit_df['upvotes'].sum(), reddit_df['downvotes'].sum()],
                labels=['Upvotes', 'Downvotes'],
                autopct='%1.1f%%'
            )
            plt.title('Reddit Engagement')
            plt.savefig('static/plots/engagement_distribution.png', bbox_inches='tight')
            plt.close()
        
        # News sentiment
        if not news_df.empty:
            plt.figure(figsize=(10, 6))
            sns.histplot(news_df['sentiment'], bins=20, kde=True, color='green')
            plt.title('News Sentiment Distribution')
            plt.savefig('static/plots/news_sentiment.png', bbox_inches='tight')
            plt.close()
            
        return True
    except Exception as e:
        print(f"Visualization Error: {str(e)}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_brand():
    try:
        brand = request.form.get('brand', '').strip()
        if not brand:
            return render_template('error.html', error="Brand name is required"), 400
        
        reddit_df, upvotes, downvotes = fetch_reddit_posts('technology', brand, 50)
        news_df = fetch_news_articles(brand, 50)
        
        combined_df = pd.concat([
            reddit_df[['title', 'sentiment', 'unique_score']],
            news_df[['title', 'sentiment', 'unique_score']]
        ])
        
        avg_sentiment = float(combined_df['sentiment'].mean()) if not combined_df.empty else 0.0
        performance_score = float((upvotes - downvotes)/(upvotes + downvotes) + ((avg_sentiment + 1) / 2)) if (upvotes + downvotes) > 0 else 0.0
        
        if not generate_visualizations(reddit_df, news_df, combined_df):
            raise Exception("Visualization generation failed")
        # Determine performance message
        if performance_score < 1:
            performance = "Negative sentiment/low engagement"
        elif 1 <= performance_score < 1.5:
            performance = "Neutral sentiment/moderate engagement"
        else:
            performance = "Positive sentiment/strong engagement"
        
        return render_template(
            'results.html',
            brand=brand.title(),
            total_upvotes=upvotes,
            total_downvotes=downvotes,
            average_sentiment=avg_sentiment,  # Already a float
            brand_performance_score=performance_score,  # Already a float
             performance=performance,
            has_reddit_data=not reddit_df.empty,
            has_news_data=not news_df.empty
        )
        
    except Exception as e:
        print(f"Analysis Error: {str(e)}")
        return render_template('error.html', error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)