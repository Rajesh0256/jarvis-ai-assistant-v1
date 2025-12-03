# 🚀 Jarvis Backend Server Setup Guide

This guide shows you how to set up a backend server so your friends can use Jarvis WITHOUT needing their own API keys.

## 📊 Overview

**Without Server (Current):**
- Each user needs their own API keys
- Users pay for their own usage
- More setup for users

**With Server (New):**
- Users don't need API keys
- You pay for all usage (you control costs)
- Users just download and run
- Professional experience like ChatGPT

## 🎯 Quick Start (Local Testing)

### Step 1: Set Up Server

```bash
# Navigate to server folder
cd server

# Install dependencies
pip install -r requirements.txt

# Create .env file with YOUR API keys
# (Copy from root .env or create new)
```

Create `server/.env`:
```env
GROQ_API_KEY=your_groq_key_here
GOOGLE_API_KEY=your_google_key_here
```

### Step 2: Run Server

```bash
python app.py
```

Server runs at: http://localhost:5000

### Step 3: Configure Jarvis Client

Update your main `.env` file:
```env
USE_SERVER=true
SERVER_URL=http://localhost:5000
```

### Step 4: Test It

1. Keep server running in one terminal
2. Run Jarvis in another terminal
3. Jarvis now uses your server instead of direct API calls!

## 🌐 Deploy to Internet (For Friends)

### Option 1: Railway (Easiest - Free Tier)

1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your Jarvis repo
5. Set root directory to `/server`
6. Add environment variables:
   - `GROQ_API_KEY`
   - `GOOGLE_API_KEY`
7. Deploy!

You'll get a URL like: `https://jarvis-production.up.railway.app`

### Option 2: Render (Free Tier)

1. Go to https://render.com
2. Sign up
3. New → Web Service
4. Connect GitHub repo
5. Settings:
   - Root Directory: `server`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add environment variables
7. Deploy!

### Option 3: Heroku (Free Tier)

```bash
# Install Heroku CLI
# Then:
cd server
heroku create jarvis-ai-backend
heroku config:set GROQ_API_KEY=your_key
heroku config:set GOOGLE_API_KEY=your_key
git push heroku main
```

## 📱 Share with Friends

### For Users (Your Friends):

1. Download Jarvis.exe
2. Create `.env` file:
```env
USE_SERVER=true
SERVER_URL=https://your-server-url.com
Username=TheirName
Assistantname=Jarvis
InputLanguage=en
```
3. Run Jarvis.exe
4. That's it! No API keys needed!

### Distribution Package

Include these files:
- `Jarvis.exe`
- `.env.example` (rename to `.env`)
- `USER_GUIDE_FOR_FRIENDS.md`
- `QUICK_START.txt`

Update `.env.example` with your server URL:
```env
USE_SERVER=true
SERVER_URL=https://your-deployed-server.com
Username=YourName
Assistantname=Jarvis
InputLanguage=en
```

## 💰 Cost Estimation

### API Costs (You Pay):
- **Light usage** (10 users, 100 requests/day): ~$10-20/month
- **Medium usage** (50 users, 500 requests/day): ~$50-100/month
- **Heavy usage** (100+ users): $200+/month

### Hosting Costs:
- **Railway/Render Free Tier**: $0 (limited hours)
- **Railway Pro**: $5/month
- **Heroku**: $7/month
- **AWS/Azure**: $10-50/month

### Total: $15-150/month depending on usage

## 🛡️ Cost Control

### Add Rate Limiting

Edit `server/app.py`:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app,
    default_limits=["100 per day", "10 per minute"]
)

@app.route('/api/chat', methods=['POST'])
@limiter.limit("50 per hour")
def chat():
    # ... existing code
```

### Monitor Usage

Check stats: `http://your-server/api/stats`

### Set Usage Quotas

Add user authentication and limit requests per user.

## 🔄 Hybrid Mode (Best of Both)

Let users choose:

**Free Tier (Your Server):**
- 50 requests per day
- Basic features

**Unlimited (Their API Keys):**
- Set `USE_SERVER=false`
- Add their own keys
- No limits

## 🔧 Troubleshooting

### Server won't start
- Check API keys in `server/.env`
- Make sure port 5000 is available
- Install all requirements

### Client can't connect
- Check `SERVER_URL` in client `.env`
- Make sure server is running
- Check firewall settings

### Slow responses
- Server might be overloaded
- Consider upgrading hosting
- Add caching

## 📈 Next Steps

1. **Test locally** - Make sure everything works
2. **Deploy to Railway/Render** - Get public URL
3. **Update client .env.example** - Add your server URL
4. **Build new .exe** - With server configuration
5. **Share with friends** - They just need .exe + .env!

## 🎉 Benefits

✅ Users don't need API keys
✅ Professional experience
✅ You control costs
✅ Easy to share
✅ Centralized updates
✅ Usage monitoring

## ⚠️ Important Notes

- Keep your API keys secret
- Monitor usage to control costs
- Consider adding authentication for production
- Use HTTPS in production
- Back up your server configuration

---

Need help? Check `server/README.md` for more details!
