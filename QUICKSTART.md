# 🚀 Quick Start - Deploy TruthBot AI for FREE

## ✅ What's Ready

Your TruthBot AI is now configured for **free public deployment**! All configuration files have been created.

## 📝 Files Created

- ✅ `render.yaml` - Render.com deployment config
- ✅ `DEPLOYMENT.md` - Complete deployment guide
- ✅ `app/services/verifier_cloud.py` - Cloud-compatible AI verifier
- ✅ `.env.example` - Environment template
- ✅ Updated `app.py` - Supports both local & cloud modes
- ✅ Updated `requirements.txt` - Added cloud dependencies

## 🎯 Deploy in 3 Steps

### 1️⃣ Get FREE API Keys

**Serper API** (for web search):
- Go to: https://serper.dev
- Sign up → Copy API key
- Free: 2,500 searches/month

**Hugging Face** (for AI):
- Go to: https://huggingface.co/settings/tokens
- Click "New token" → Select "Read" → Copy token
- Free: Unlimited usage

### 2️⃣ Update Your .env File

Open your `.env` file and paste this (replace with your actual keys):

```env
USE_HUGGINGFACE=true
HUGGINGFACE_API_KEY=paste_your_huggingface_token_here
SERPER_API_KEY=paste_your_serper_key_here
```

### 3️⃣ Deploy to Render.com

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy on Render**:
   - Go to: https://render.com
   - Sign up with GitHub
   - Click "New +" → "Web Service"
   - Select your repository
   - Add environment variables (same as .env above)
   - Click "Create Web Service"

3. **Done!** Your app will be live in 5-10 minutes at:
   `https://your-app-name.onrender.com`

## 📖 Need More Help?

Read the complete guide: [`DEPLOYMENT.md`](file:///c:/Users/USER/Desktop/Nuit%20d'info/truthbot/DEPLOYMENT.md)

## ⚡ Test Locally First (Optional)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# Visit: http://localhost:8000
```

---

**That's it!** Your fact-checking AI will be publicly accessible for free! 🎉
