# News & Geopolitics Feature Guide

## Overview
Jarvis can now provide you with current news and geopolitical updates from around the world.

## Features

### 1. General News
Ask Jarvis about current news and headlines:
- "What's the latest news?"
- "Tell me today's news"
- "What's happening in the news?"
- "Current news"

### 2. Geopolitics
Get updates on international relations and world politics:
- "Tell me about geopolitics"
- "What's happening in world politics?"
- "Geopolitical situation"
- "International relations news"

### 3. Category-Specific News
Ask about specific news categories:
- **Business**: "Business news", "Market news", "Economy updates"
- **Technology**: "Tech news", "Technology updates", "Science news"
- **Sports**: "Sports news", "Latest sports updates"
- **Health**: "Health news", "Medical updates"

### 4. Topic-Specific News
Search for news about specific topics:
- "News about artificial intelligence"
- "Tell me news about climate change"
- "What's the news on elections?"

## Setup Instructions

### Option 1: With NewsAPI (Recommended for Real-Time News)

1. **Get a Free API Key**
   - Visit: https://newsapi.org/
   - Sign up for a free account
   - Copy your API key

2. **Add to .env File**
   - Open your `.env` file in the Jarvis directory
   - Add this line:
     ```
     NEWS_API_KEY=your_api_key_here
     ```
   - Replace `your_api_key_here` with your actual API key

3. **Restart Jarvis**
   - Close and restart Jarvis for changes to take effect

### Option 2: Without API Key (Fallback Mode)

If you don't configure an API key, Jarvis will:
- Provide instructions on how to set up the API
- Suggest using the web search feature as an alternative
- Still respond to your queries with helpful information

## Example Commands

```
You: "What's the latest news?"
Jarvis: [Provides top 5 current headlines]

You: "Tell me about geopolitics"
Jarvis: [Provides geopolitical news and international updates]

You: "News about technology"
Jarvis: [Provides latest technology news]

You: "What's happening in world politics?"
Jarvis: [Provides international political news]

You: "Business news"
Jarvis: [Provides business and economy updates]
```

## How It Works

1. **Voice Command**: Speak your news query to Jarvis
2. **Processing**: Jarvis identifies it as a news/geopolitics request
3. **Fetching**: Connects to news sources to get latest information
4. **Response**: Displays and speaks the news updates

## Features

- **Real-time Updates**: Get the latest news as it happens
- **Multiple Categories**: Business, tech, sports, health, and more
- **Geopolitical Focus**: Specialized queries for international relations
- **Source Attribution**: See which news sources provided the information
- **Date Stamps**: Know when the news was published

## Troubleshooting

### "I'm having trouble accessing news sources"
- Check your internet connection
- Verify your NEWS_API_KEY is correct in .env
- Make sure you haven't exceeded the free tier limit (500 requests/day)

### "To get real-time news, please configure a NewsAPI key"
- This means you haven't set up the API key yet
- Follow the setup instructions above
- Alternatively, use Jarvis's web search feature

### API Key Limits
- Free tier: 500 requests per day
- If you exceed the limit, wait 24 hours or upgrade your plan

## Privacy & Data

- News data is fetched from NewsAPI.org
- No personal data is sent to news services
- Your API key is stored locally in your .env file
- News queries are not logged or tracked

## Advanced Usage

### Combining with Other Features
You can combine news queries with other commands:
- "Tell me the news and then open Chrome"
- "What's the latest tech news and search for Python tutorials"

### Regular Updates
Ask Jarvis for news updates throughout your day:
- Morning: "Good morning, what's the news?"
- Afternoon: "Any breaking news?"
- Evening: "What happened today in the world?"

## Future Enhancements

Planned features:
- News summaries and briefings
- Personalized news based on interests
- News alerts and notifications
- Multi-language news support
- Local news by region

---

**Note**: This feature requires an internet connection to fetch real-time news data.
