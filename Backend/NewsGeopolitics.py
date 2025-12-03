"""
News and Geopolitics Module for Jarvis AI
Fetches current news, geopolitical updates, and world events
"""

import requests
from datetime import datetime


class NewsGeopoliticsEngine:
    """Handles news and geopolitics queries"""
    
    def __init__(self):
        # Using free news APIs
        self.news_api_key = None  # User can add their NewsAPI key in .env
        self.base_urls = {
            'newsapi': 'https://newsapi.org/v2/',
            'gnews': 'https://gnews.io/api/v4/',
        }
    
    def get_top_headlines(self, category='general', country='us'):
        """Get top headlines from news sources"""
        try:
            # Try NewsAPI first (requires API key)
            if self.news_api_key:
                url = f"{self.base_urls['newsapi']}top-headlines"
                params = {
                    'apiKey': self.news_api_key,
                    'category': category,
                    'country': country,
                    'pageSize': 5
                }
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    return self._format_news(data.get('articles', []))
            
            # Fallback to RSS feeds or web scraping
            return self._get_news_fallback(category)
        
        except Exception as e:
            print(f"Error fetching news: {e}")
            return "I'm having trouble accessing news sources right now."
    
    def get_geopolitics_news(self):
        """Get geopolitical news and updates"""
        try:
            # Focus on international relations, conflicts, diplomacy
            keywords = ['geopolitics', 'international', 'diplomacy', 'conflict', 'world politics']
            return self.search_news(' OR '.join(keywords))
        except Exception as e:
            print(f"Error fetching geopolitics news: {e}")
            return "I'm having trouble accessing geopolitical news right now."
    
    def search_news(self, query):
        """Search for specific news topics"""
        try:
            if self.news_api_key:
                url = f"{self.base_urls['newsapi']}everything"
                params = {
                    'apiKey': self.news_api_key,
                    'q': query,
                    'sortBy': 'publishedAt',
                    'pageSize': 5,
                    'language': 'en'
                }
                response = requests.get(url, params=params, timeout=10)
                if response.status_code == 200:
                    data = response.json()
                    return self._format_news(data.get('articles', []))
            
            return self._get_news_fallback(query)
        
        except Exception as e:
            print(f"Error searching news: {e}")
            return f"I couldn't find news about {query} right now."
    
    def _format_news(self, articles):
        """Format news articles into readable text"""
        if not articles:
            return "No news articles found."
        
        response = f"Here are the latest updates:\n\n"
        for i, article in enumerate(articles[:5], 1):
            title = article.get('title', 'No title')
            source = article.get('source', {}).get('name', 'Unknown source')
            description = article.get('description', '')
            published = article.get('publishedAt', '')
            
            # Format date
            if published:
                try:
                    date_obj = datetime.fromisoformat(published.replace('Z', '+00:00'))
                    published = date_obj.strftime('%B %d, %Y')
                except:
                    published = ''
            
            response += f"{i}. {title}\n"
            response += f"   Source: {source}"
            if published:
                response += f" | {published}"
            response += "\n"
            if description:
                response += f"   {description[:150]}...\n"
            response += "\n"
        
        return response.strip()
    
    def _get_news_fallback(self, topic='general'):
        """Fallback method when API is not available"""
        # This provides a helpful message when API key is not configured
        return (
            f"To get real-time news about {topic}, please configure a NewsAPI key.\n\n"
            "Steps to enable news features:\n"
            "1. Get a free API key from https://newsapi.org/\n"
            "2. Add 'NEWS_API_KEY=your_key_here' to your .env file\n"
            "3. Restart Jarvis\n\n"
            "Alternatively, I can search the web for current information using my search capabilities."
        )


def GetNews(query=""):
    """Main function to get news based on query"""
    engine = NewsGeopoliticsEngine()
    
    # Load API key from environment if available
    try:
        from dotenv import dotenv_values
        env_vars = dotenv_values(".env")
        engine.news_api_key = env_vars.get("NEWS_API_KEY")
    except:
        pass
    
    query_lower = query.lower()
    
    # Determine what type of news to fetch
    if any(word in query_lower for word in ['geopolitics', 'geopolitical', 'international', 'world politics']):
        return engine.get_geopolitics_news()
    elif any(word in query_lower for word in ['business', 'economy', 'market', 'stock']):
        return engine.get_top_headlines(category='business')
    elif any(word in query_lower for word in ['technology', 'tech', 'science']):
        return engine.get_top_headlines(category='technology')
    elif any(word in query_lower for word in ['sports', 'game', 'match']):
        return engine.get_top_headlines(category='sports')
    elif any(word in query_lower for word in ['health', 'medical', 'covid', 'disease']):
        return engine.get_top_headlines(category='health')
    elif query.strip():
        # Search for specific topic
        return engine.search_news(query)
    else:
        # Get general top headlines
        return engine.get_top_headlines()


if __name__ == "__main__":
    # Test the module
    print("Testing News & Geopolitics Module\n")
    print("=" * 60)
    print(GetNews("geopolitics"))
