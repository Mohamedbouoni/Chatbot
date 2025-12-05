# 🚀 Free Public Deployment Guide for TruthBot AI

This guide will help you deploy TruthBot AI for **FREE** on Render.com.

## 📋 Prerequisites

Before deploying, you need **two FREE API keys**:

1. **Serper API Key** - For web search
   - Sign up at: https://serper.dev
   - Free tier: 2,500 searches/month
   
2. **Hugging Face API Key** - For AI fact-checking
   - Sign up at: https://huggingface.co
   - Get token at: https://huggingface.co/settings/tokens
   - Click "New token" → Select "Read" access → Copy token

## 🌐 Option 1: Deploy to Render.com (Recommended - FREE)

### Step 1: Prepare Your Repository

1. **Push your code to GitHub**:
   ```bash
   cd "c:\Users\USER\Desktop\Nuit d'info\truthbot"
   git add .
   git commit -m "Add cloud deployment configuration"
   git push origin main
   ```

### Step 2: Deploy on Render

1. **Go to Render.com**:
   - Visit: https://render.com
   - Click "Get Started for Free"
   - Sign up with GitHub

2. **Create New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `truthbot` repository

3. **Configure the Service**:
   - **Name**: `truthbot-ai` (or any name you prefer)
   - **Region**: Frankfurt (or closest to you)
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables**:
   Click "Advanced" → "Add Environment Variable":
   
   | Key | Value |
   |-----|-------|
   | `USE_HUGGINGFACE` | `true` |
   | `HUGGINGFACE_API_KEY` | Your Hugging Face token |
   | `SERPER_API_KEY` | Your Serper API key |
   | `PYTHON_VERSION` | `3.11.0` |

5. **Deploy**:
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Your app will be live at: `https://truthbot-ai.onrender.com`

### Step 3: Test Your Deployment

Visit your deployed URL and test:
- Health check: `https://your-app.onrender.com/health`
- Upload a test document via the web interface

---

## 🐳 Option 2: Deploy to Railway.app (Alternative FREE option)

1. **Go to Railway.app**:
   - Visit: https://railway.app
   - Sign up with GitHub

2. **Create New Project**:
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your `truthbot` repository

3. **Add Environment Variables**:
   - Go to "Variables" tab
   - Add the same environment variables as Render (see above)

4. **Deploy**:
   - Railway will auto-deploy
   - Get your public URL from the "Settings" tab

---

## 🔧 Local Testing Before Deployment

Test the cloud configuration locally:

1. **Update your `.env` file**:
   ```env
   USE_HUGGINGFACE=true
   HUGGINGFACE_API_KEY=your_actual_token
   SERPER_API_KEY=your_actual_key
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python app.py
   ```

4. **Test at**: http://localhost:8000

---

## 📊 Deployment Comparison

| Platform | Free Tier | Ease | Best For |
|----------|-----------|------|----------|
| **Render** | ✅ 750 hrs/month | ⭐⭐⭐⭐⭐ | Recommended |
| **Railway** | ✅ $5 credit/month | ⭐⭐⭐⭐ | Alternative |
| **Heroku** | ❌ No free tier | ⭐⭐⭐ | Paid only |

---

## ⚠️ Important Notes

### Free Tier Limitations

1. **Render Free Tier**:
   - App sleeps after 15 minutes of inactivity
   - First request after sleep takes ~30 seconds to wake up
   - 750 hours/month (enough for continuous use)

2. **Hugging Face API**:
   - Free tier has rate limits
   - Model may take 5-10 seconds to load on first request
   - Subsequent requests are faster

3. **Serper API**:
   - 2,500 free searches/month
   - Monitor usage at: https://serper.dev/dashboard

### Image Verification

> [!WARNING]
> Image verification (OCR) is **NOT available** in cloud deployment. Only text and PDF files are supported. For image support, you need local deployment with Ollama + LLaVA.

---

## 🐛 Troubleshooting

### Issue: "Application failed to start"
**Solution**: Check Render logs for errors. Common issues:
- Missing environment variables
- Invalid API keys
- Python version mismatch

### Issue: "Model loading timeout"
**Solution**: Hugging Face models take time to load on first request. Wait 30-60 seconds and try again.

### Issue: "Serper API quota exceeded"
**Solution**: 
- Check usage at https://serper.dev/dashboard
- Upgrade to paid plan or wait for monthly reset

### Issue: "App is slow to respond"
**Solution**: 
- Free tier apps sleep after inactivity
- First request wakes the app (~30 seconds)
- Keep app active with uptime monitoring (e.g., UptimeRobot)

---

## 🔄 Switching Between Local and Cloud

You can switch deployment modes by changing `USE_HUGGINGFACE` in your `.env`:

**For Local (Ollama)**:
```env
USE_HUGGINGFACE=false
OLLAMA_MODEL=qwen:7b
OLLAMA_BASE_URL=http://localhost:11434
```

**For Cloud (Hugging Face)**:
```env
USE_HUGGINGFACE=true
HUGGINGFACE_API_KEY=your_token
```

---

## 📞 Support

If you encounter issues:
1. Check the Render deployment logs
2. Verify all environment variables are set correctly
3. Test API keys independently
4. Check the GitHub repository for updates

---

## 🎉 Success!

Once deployed, share your public URL:
- `https://your-app-name.onrender.com`

Your TruthBot AI is now publicly accessible! 🚀
