# Jarvis Backend Server

This server allows users to run Jarvis without needing their own API keys.

## Setup

### 1. Install Dependencies

```bash
cd server
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file in the `server` folder:

```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Run the Server

**Local Testing:**
```bash
python app.py
```

Server will run at: http://localhost:5000

**Production (with Gunicorn):**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Deployment Options

### Option 1: Heroku (Free Tier Available)
1. Create Heroku account
2. Install Heroku CLI
3. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
4. Deploy:
   ```bash
   heroku create jarvis-ai-server
   heroku config:set GROQ_API_KEY=your_key
   heroku config:set GOOGLE_API_KEY=your_key
   git push heroku main
   ```

### Option 2: Railway (Easy & Free)
1. Go to railway.app
2. Connect your GitHub repo
3. Add environment variables
4. Deploy automatically

### Option 3: Render (Free Tier)
1. Go to render.com
2. Create new Web Service
3. Connect GitHub repo
4. Add environment variables
5. Deploy

### Option 4: AWS/Azure/GCP
For production with high traffic, use cloud providers.

## API Endpoints

### Health Check
```
GET /health
```

### Chat
```
POST /api/chat
Body: {
  "message": "Hello",
  "history": []
}
```

### Vision Analysis
```
POST /api/vision
Body: {
  "image": "base64_image_data",
  "prompt": "Describe this image"
}
```

### Statistics
```
GET /api/stats
```

## Client Configuration

Users need to update their `.env` file:

```env
USE_SERVER=true
SERVER_URL=http://your-server-url.com
```

Or for local API keys:
```env
USE_SERVER=false
GROQ_API_KEY=their_own_key
GOOGLE_API_KEY=their_own_key
```

## Cost Monitoring

The server tracks:
- Total requests
- Total tokens used

Access at: `http://your-server/api/stats`

## Security Notes

- Never commit `.env` file
- Use HTTPS in production
- Add rate limiting for production
- Consider adding authentication
- Monitor API usage to control costs

## Scaling

For more users:
1. Add rate limiting
2. Implement caching
3. Use load balancer
4. Add user authentication
5. Implement usage quotas
