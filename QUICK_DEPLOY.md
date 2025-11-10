# 🚀 Quick Deployment Commands

## Step 1: Create GitHub Repo

Go to: https://github.com/new

- Name: `ai-teaching-assistant`
- Privacy: **Private** (recommended)
- Click "Create repository"

## Step 2: Push to GitHub

```powershell
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/ai-teaching-assistant.git
git push -u origin main
```

## Step 3: Deploy to Streamlit Cloud

1. Go to: https://share.streamlit.io
2. Click "New app"
3. Select your repository
4. Main file: `dashboard.py`
5. **CRITICAL:** Advanced settings → Secrets
6. Copy/paste entire content from: `.streamlit\secrets.toml`
7. Click "Deploy!"

## Your Secrets (copy this into Streamlit Cloud):

Location: `.streamlit\secrets.toml`

⚠️ **DO NOT share these secrets publicly!**

---

## Troubleshooting

**Can't push to GitHub?**

```powershell
# Configure Git if this is your first time
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Wrong remote URL?**

```powershell
# Remove and re-add
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/ai-teaching-assistant.git
```

**Deployment fails?**

- Check build logs in Streamlit Cloud dashboard
- Verify secrets are correctly formatted (TOML syntax)
- Ensure Google Sheet is shared with service account

---

## After Deployment

**Your app will be live at:**
`https://YOUR-APP-NAME.streamlit.app`

**Test checklist:**

- [ ] Home page loads
- [ ] View Students shows 3 students
- [ ] Can generate a lesson note
- [ ] Can generate a student report
- [ ] Can write parent message

**To update app:**

```powershell
# Make changes, then:
git add .
git commit -m "Your change description"
git push origin main
# Auto-deploys in ~2 minutes
```

---

📖 **Full guide:** `STREAMLIT_CLOUD_DEPLOYMENT.md`
