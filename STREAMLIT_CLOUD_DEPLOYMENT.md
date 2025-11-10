# 🚀 Streamlit Cloud Deployment - Step-by-Step Guide

## ✅ Pre-Deployment Checklist (COMPLETED)

- ✅ Code updated to support Streamlit Cloud secrets
- ✅ `.streamlit/secrets.toml` created with your credentials (LOCAL ONLY)
- ✅ `.gitignore` configured to protect secrets
- ✅ Git repository initialized and first commit made
- ✅ All sensitive files excluded from Git

---

## 📝 Step 1: Create GitHub Repository

### Option A: Using GitHub Website (Recommended)

1. **Go to GitHub and create new repository:**
   - Visit: https://github.com/new
   - Repository name: `ai-teaching-assistant`
   - Description: "AI-powered teaching assistant for lesson notes, reports, and parent communication"
   - **Make it Private** (recommended for security)
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
   - Click "Create repository"

2. **Copy the repository URL** (you'll see it on the next page):
   ```
   https://github.com/YOUR_USERNAME/ai-teaching-assistant.git
   ```

### Option B: Using GitHub CLI (if you have it installed)

```powershell
gh repo create ai-teaching-assistant --private --source=. --remote=origin --push
```

---

## 📤 Step 2: Push Code to GitHub

Run these commands in your PowerShell terminal:

```powershell
# Add GitHub repository as remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/ai-teaching-assistant.git

# Push code to GitHub
git branch -M main
git push -u origin main
```

**Enter your GitHub credentials when prompted.**

---

## ☁️ Step 3: Deploy to Streamlit Cloud

### 3.1 Sign Up / Log In

1. Go to: https://share.streamlit.io
2. Click "Sign up" or "Continue with GitHub"
3. Authorize Streamlit Cloud to access your GitHub account

### 3.2 Create New App

1. Click "**New app**" button (top right)
2. You'll see a form with these fields:

**Repository:**
- Select your repository: `YOUR_USERNAME/ai-teaching-assistant`

**Branch:**
- Select: `main`

**Main file path:**
- Enter: `dashboard.py`

**App URL (optional):**
- Leave default or customize: `your-app-name.streamlit.app`

### 3.3 Configure Secrets

**CRITICAL STEP - Don't skip this!**

1. Click "**Advanced settings**" (before deploying)

2. In the "**Secrets**" section, paste this entire content from `.streamlit\secrets.toml`:

```toml
# OpenAI Configuration
OPENAI_API_KEY = "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"
OPENAI_MODEL = "gpt-3.5-turbo"

# Google Sheets Configuration
GOOGLE_SHEET_ID = "1v1Hv6Z29ezB58Cnr7NEFEvqLB3nhXik9Ax2ucSBi-8A"

# Google Cloud Service Account Credentials
[gcp_service_account]
type = "service_account"
project_id = "ai-teaching-assistant-477806"
private_key_id = "96a9cb998ffb170a70c9ab64a1fd6c36c80ca1c8"
private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDJ08k5jkTb+jAy\nADbbm646pQ4a1KWVaRxKe9cXDpNXeEHWcXAexxtX8KjVWJAnVF8E5nOJoClIK+yz\nTSwWXtENHlbAP/8VYvC3ybO2ufZmN//dEWoHshRaiUcloMszVf37dvI5kr4zbhJc\noasaevV8HErASOK4EHpzmmElGyQwqtkG76dyCFKbwOVN288JyYA1vuoN6A9Y8buq\nAa+W0sXyVvEbcnjz3qmJiuUJyW1k5tVR6PNl3GBGrZK+a9Lyo4lfwUPUPpxkfNeE\n3Bln7MhxTbUe49O5F8CtUkrfTwkT2tmgc1ekUFxJNGA789msFS/S0HlEOuYolkfc\n/y/+UffZAgMBAAECggEAAQTZYk8EJrg1JmRtJYXOfEUYmreStw5CwmlFAQvtTbha\nviqeO6NCoLwdP23TeblzmHOtonuDrIHnBnB56NmfSqOUiXhj6LYBgqjKHX6ocvUR\nrngHDNVNB4FdqJm5X5IPObCada0eL2YqtYqPjRI7rmcSTnIkU71my7gRj1IHb+x0\nTwh9loON1CbqM4H/hmnEAz0XbSSiBzMEggiDc+QCs+awZD7ideOoRdPVBXawOOAK\nsrsg1R69Ayw5KaA6ocG4+zG9oW1iQuFqwzKQuDeMQSVsZeHTyAHNjeR/axPU2dx+\nt6Wd08JSxj1OkXZSMhz9AbQi1rB3B83H4QNVb+U6ZQKBgQDl/223epqjd96AMZVw\nrTqs8xH6vYSOnvsD5cWWTKu00rsV06l2vw6WoQYOfCxDKSWk3QmhMSRLVe06VqL8\nuA5tO7RNTczgFFlXY+DzXDqODo81JvfOTrl69+RIBaWy9TMzDGNoAt8W12mZXWkK\nuboajic+Tq2pzsG9bCDeqajxzQKBgQDgpQzmwuYqWi2+XCVeMy2t8Yw6YHPpyZPo\nf8o+bb6ZAd4T8QQj2DmpntVBk6HZBsyeXMgnC3H8O1WUYlLIg/o3+eU3DlmWAxIj\nQh377TjZjFdgcUIxL2iDdH03p1n5k1awpYtRgEunzkMvDts+w2KIufG3JbrFOsKm\nXLwJSh/CPQKBgQDYL0RQvwRVfNl+Q50FAT7yy7LtrW/IovSskDAt+zk2SRGjDYXv\nYNx0hzxrJxpvsmB4228uvUMxML5AJKkkxFiDIihytRtK0LW9Z9tMxDchydugCVXJ\n7MN5K0K+09gRI1sRs6ZIYNKS5L2Uc3HFrBea2F1YupmP0BDZXKZ0xKJRTQKBgGBD\n2kd49ZDom/mbGxhG7ig//kt10bY5f3x+ZnhiJu8CcdwxyAhkPDGHsvMrBIwv8bdb\nIxo4OVxRQNcZW0g55hvepm71Y0Z5gmhBiP/QJDB1h2v4nNje6/aJEK+ss03T6a5B\nAnamd8UtCnU79I/swmi85ewJ6wNhrtADpUCF1x4xAoGBAMLQpM5TCgzWwxyqqFXx\nYPm0bKsPs1XWrWSuCNt54VVnuyguAfde5ano/HOcIJxnquN3Y+Bo+aa92bQo5bWm\nOhMzxrwMCkI/iTMlNwao/jLB/K8FTixf7NppVlfsqW7s2mLLvKa2CRz4FjTx5+Yo\nrga6Z+2rX/ZsNmTCShJ1DY0g\n-----END PRIVATE KEY-----\n"
client_email = "teaching-assistant-bot@ai-teaching-assistant-477806.iam.gserviceaccount.com"
client_id = "100472811849636405842"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/teaching-assistant-bot%40ai-teaching-assistant-477806.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

3. Click "**Save**"

### 3.4 Deploy!

1. Click "**Deploy!**" button
2. Wait 2-5 minutes for initial deployment
3. Watch the build logs in real-time

---

## ✅ Step 4: Verify Deployment

Once deployment completes, you'll see:

1. **Your app URL:** `https://your-app-name.streamlit.app`
2. **Status:** Running ✅

### Test Your App:

1. Visit your app URL
2. Navigate to "**View Students**" page
3. Click "Refresh Data" - should see Emma, Liam, and Sophia
4. Try generating a report for one student
5. Check if OpenAI API generates content

---

## 🔧 Troubleshooting

### If deployment fails:

1. **Check Build Logs:**
   - Look for errors in the Streamlit Cloud dashboard
   - Common issues: missing dependencies, Python version mismatch

2. **Verify Secrets:**
   - Go to app settings → Secrets
   - Ensure all secrets are pasted correctly
   - Check for formatting errors (TOML syntax)

3. **Check Python Version:**
   - Streamlit Cloud uses Python 3.11 by default
   - Create `.python-version` file if needed:
     ```
     3.11
     ```

### If Google Sheets connection fails:

- Verify Sheet ID in secrets matches your actual sheet
- Ensure service account email has access to sheet
- Check if private_key has `\n` characters preserved

### If OpenAI API fails:

- Verify API key in Streamlit secrets
- Check OpenAI billing: https://platform.openai.com/account/billing
- Confirm you have credits/payment method

---

## 🔄 Updating Your Deployed App

After deployment, any push to GitHub main branch auto-deploys:

```powershell
# Make changes to code
# Then:
git add .
git commit -m "Update: description of changes"
git push origin main

# Streamlit Cloud auto-deploys in ~2 minutes
```

---

## ⚙️ Managing Your App

### Access App Settings:

1. Go to: https://share.streamlit.io
2. Click your app
3. Click "⚙️ Settings" (top right)

**Available options:**
- **Secrets:** Update API keys/credentials
- **General:** Change app name, URL, or make public
- **Resources:** View usage (free tier: 1 GB RAM, shared CPU)
- **Logs:** View runtime logs for debugging
- **Reboot:** Restart app if frozen

### View Logs:

- Click "☰ Manage app" → "Logs"
- Real-time application logs
- Helpful for debugging errors

---

## 💰 Cost & Limits

**Streamlit Cloud FREE Tier:**
- ✅ 1 private app
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Community support
- ✅ Auto-deploys from GitHub

**Limitations:**
- Apps sleep after 7 days of inactivity
- Shared CPU (can be slow during peak times)
- Limited to 1 concurrent user on free tier

**Paid Plans:**
- Starter: $20/month (more resources, no sleep)
- Team: $250/month (team collaboration, priority support)

---

## 🎉 Next Steps

1. ✅ Share your app URL with colleagues
2. ✅ Test all features (lesson generator, reports, parent messages)
3. ✅ Monitor OpenAI usage to avoid unexpected costs
4. ✅ Customize dashboard branding/colors if needed
5. ✅ Add more students to Google Sheet for testing

---

## 📞 Support

**Streamlit Cloud Issues:**
- Docs: https://docs.streamlit.io/streamlit-community-cloud
- Forum: https://discuss.streamlit.io
- Status: https://www.streamlitstatus.com

**Your App Issues:**
- Check logs in Streamlit Cloud dashboard
- Review `SECURITY.md` for API key troubleshooting
- Consult `README.md` for feature documentation

---

**🚀 You're ready to deploy! Follow the steps above to get your dashboard live in ~10 minutes.**
