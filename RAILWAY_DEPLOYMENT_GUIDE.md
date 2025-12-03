# 🚂 Deploy Jarvis Server to Railway

## Quick Deployment (5 Minutes)

### Step 1: Prepare Your Repository

Your server files are ready in the `server/` folder. Now commit them to GitHub:

```bash
git add server/
git commit -m "Add Jarvis backend server"
git push origin main
```

### Step 2: Sign Up for Railway

1. Go to https://railway.app
2. Click **"Login"** or **"Start a New Project"**
3. Sign up with your **GitHub account** (easiest option)
4. Authorize Railway to access your repositories

### Step 3: Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your repository: `jarvis-ai-assistant-v1`
4. Railway will detect your project automatically

### Step 4: Configure Root Directory

Since your server is in the `server/` folder:

1. Click on your deployment
2. Go to **Settings** tab
3. Find **"Root Directory"**
4. Set it to: `server`
5. Click **"Save"**

### Step 5: Add Environment Variables

1. Go to **Variables** tab
2. Click **"New Variable"**
3. Add these two variables:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

**Important**: Use YOUR actual API keys from your `.env` file!

To get your keys:
- Open your local `.env` file
- Copy the `GroqAPIKey` value → paste as `GROQ_API_KEY`
- Copy the `GeminiAPIKey` value → paste as `GOOGLE_API_KEY`

### Step 6: Deploy!

1. Railway will automatically start deploying
2. Wait 2-3 minutes for the build to complete
3. Once deployed, you'll see a **"Deployments"** section with a green checkmark

### Step 7: Get Your Public URL

1. Go to **Settings** tab
2. Scroll to **"Networking"** section
3. Click **"Generate Domain"**
4. You'll get a URL like: `https://jarvis-production.up.railway.app`
5. **Copy this URL** - you'll need it!

### Step 8: Test Your Server

Open your browser and visit:
```
https://your-railway-url.up.railway.app/health
```

You should see:
```json
{"status": "online", "message": "Jarvis server is running"}
```

✅ **Your server is live!**

---

## Update Jarvis to Use Your Server

### Option 1: For Your Own Use

Update your `.env` file:
```env
USE_SERVER=true
SERVER_URL=https://your-railway-url.up.railway.app
```

### Option 2: For Sharing with Friends

Update `.env.example`:
```env
USE_SERVER=true
SERVER_URL=https://your-railway-url.up.railway.app
Username=YourName
Assistantname=Jarvis
InputLanguage=en
```

Then build a new .exe with this configuration!

---

## Railway Free Tier

**What You Get:**
- $5 free credit per month
- ~500 hours of usage
- Perfect for testing and small user base

**Estimated Usage:**
- 10 active users: ~$3-5/month (within free tier!)
- 50 active users: ~$10-15/month
- 100+ users: Consider upgrading to Pro ($20/month)

**Monitor Usage:**
- Go to Railway dashboard
- Check "Usage" tab
- Set up billing alerts

---

## Troubleshooting

### Build Failed?
- Check that `server/requirements.txt` exists
- Make sure root directory is set to `server`
- Check deployment logs for errors

### Server Not Responding?
- Verify environment variables are set correctly
- Check that both API keys are valid
- Look at deployment logs for errors

### "Module Not Found" Error?
- Make sure `requirements.txt` has all dependencies
- Redeploy the project

### Port Issues?
Railway automatically assigns a port. The server uses `0.0.0.0` which works with Railway's port assignment.

---

## Alternative: Deploy to Render

If Railway doesn't work, try Render:

1. Go to https://render.com
2. Sign up with GitHub
3. New → Web Service
4. Connect your repo
5. Settings:
   - Root Directory: `server`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. Add environment variables
7. Deploy!

---

## Next Steps After Deployment

1. ✅ Test your server URL
2. ✅ Update Jarvis `.env` with server URL
3. ✅ Test Jarvis locally with server
4. ✅ Build new .exe with server configuration
5. ✅ Share with friends!

---

## Your Server URL

Once deployed, your server will be at:
```
https://[your-project-name].up.railway.app
```

**Save this URL** - you'll use it in Jarvis configuration!

---

## Need Help?

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Check deployment logs in Railway dashboard

---

**Ready to deploy? Follow the steps above!** 🚀
