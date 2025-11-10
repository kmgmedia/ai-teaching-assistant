# 🎓 AI Teaching Assistant Dashboard - Quick Start Guide

## 🚀 Launching the Dashboard

### Method 1: Simple Launcher (Recommended)

```powershell
.\launch_dashboard.ps1
```

### Method 2: Manual Launch

```powershell
cd C:\Users\DELL\Desktop\ai_assistant_for_teachers
.\venv\Scripts\Activate.ps1
streamlit run dashboard.py
```

### Method 3: Direct Command

```powershell
C:/Users/DELL/Desktop/ai_assistant_for_teachers/venv/Scripts/python.exe -m streamlit run dashboard.py
```

---

## 🌐 Accessing the Dashboard

Once launched, the dashboard will be available at:

- **Local**: http://localhost:8501
- **Network**: http://10.29.18.111:8501 (accessible from other devices on your network)

The dashboard will automatically open in your default browser!

---

## 📋 Dashboard Features

### 1. 🏠 Home Page

- Overview of your teaching assistant capabilities
- Quick stats from your Google Sheets
- Getting started guide

### 2. 📝 Lesson Generator

- Create structured lesson plans
- Fill in: Subject, Topic, Age Group, Duration, Objectives
- Download generated lesson notes
- Auto-saved to `data/output/lessons/`

### 3. 📊 Report Generator

- Generate professional student progress reports
- **Load from Google Sheets**: Automatically pulls student data
- Edit and customize before generating
- Option to save back to Google Sheets
- Download as text file

### 4. 💌 Parent Message Writer

- Draft personalized parent communications
- Choose purpose: Appreciation, Reminder, Feedback, or Concern
- Fill in context and generate professional messages
- Copy to clipboard or download

### 5. 👥 View Students

- See all students from your Google Sheet
- View individual student details
- Quick actions: Generate report or send parent message
- Real-time sync with Google Sheets

---

## 💡 Usage Tips

### Loading Student Data

1. Make sure your Google Sheet has the "Students" tab
2. Required columns: Name, Subject, Score, Notes, Behavior
3. Dashboard automatically syncs on load

### Generating Reports

1. Go to "📊 Report Generator"
2. Enable "Load student data from Google Sheets"
3. Select a student from dropdown
4. Data auto-fills - edit if needed
5. Click "Generate Report"
6. Optionally save back to the "Reports" tab

### Best Practices

- ✅ Keep Google Sheet updated with latest student data
- ✅ Save generated content for your records
- ✅ Customize prompts in `core/prompts/` for your teaching style
- ✅ Check `logs/app.log` if you encounter issues

---

## 🎨 Dashboard Layout

```
┌─────────────────────────────────────────┐
│  🎓 AI Teaching Assistant               │
├─────────────────────────────────────────┤
│ Sidebar:                   │ Main Area: │
│ - 🏠 Home                  │            │
│ - 📝 Lesson Generator      │  Content   │
│ - 📊 Report Generator      │  displays  │
│ - 💌 Parent Message        │  here      │
│ - 👥 View Students         │            │
│                            │            │
│ Tips & Shortcuts           │            │
└────────────────────────────┴────────────┘
```

---

## 🔧 Troubleshooting

### Dashboard won't start

```powershell
# Check if virtual environment is activated
.\venv\Scripts\Activate.ps1

# Reinstall streamlit if needed
pip install streamlit pandas
```

### "Unable to load students" error

- Check Google Sheets credentials are in `credentials/google-sheets-credentials.json`
- Verify Sheet ID is correct in `.env`
- Ensure service account has access to your sheet

### OpenAI API errors

- Add billing to your OpenAI account
- Check API key in `.env` file
- View detailed errors in `logs/app.log`

### Port already in use

```powershell
# Run on a different port
streamlit run dashboard.py --server.port=8502
```

---

## ⚡ Keyboard Shortcuts (in browser)

- **R** - Rerun the app
- **C** - Clear cache
- **Ctrl/Cmd + Shift + R** - Hard refresh

---

## 📁 File Locations

### Generated Content

```
data/output/
├── lessons/          # Lesson notes
├── reports/          # Student reports
└── parent_messages/  # Parent communications
```

### Configuration

```
.env                  # API keys and settings
config/settings.py    # Python config
core/prompts/         # AI prompt templates
```

### Logs

```
logs/app.log          # Application logs
```

---

## 🎯 Workflow Examples

### Example 1: Generate Report for All Students

1. Go to "👥 View Students"
2. Click on first student
3. Click "Generate Report"
4. Save to Google Sheets
5. Repeat for other students

### Example 2: Create Weekly Lesson Plans

1. Go to "📝 Lesson Generator"
2. Fill in Monday's lesson details
3. Generate and download
4. Repeat for each day
5. All saved to `data/output/lessons/`

### Example 3: Send Appreciation Messages

1. Review good behavior in "👥 View Students"
2. Go to "💌 Parent Message"
3. Select purpose: "appreciation"
4. Add specific details about student's achievement
5. Generate and copy to email

---

## 🚦 Status Indicators

- 🟢 **Green Success Box**: Operation completed successfully
- 🔴 **Red Error Box**: Something went wrong - check the message
- 🟡 **Yellow Warning**: Non-critical issue or information
- 🔵 **Blue Info Box**: Helpful information or tips

---

## 📞 Need Help?

1. **Check logs**: `logs/app.log`
2. **Review documentation**:
   - `README.md` - Full project docs
   - `API_USAGE_GUIDE.md` - API reference
   - `GOOGLE_SHEETS_SETUP.md` - Google Sheets setup
3. **Common issues**: See troubleshooting section above

---

## 🎉 You're All Set!

Your AI Teaching Assistant dashboard is ready to help you:

- ✅ Save hours on lesson planning
- ✅ Write professional reports quickly
- ✅ Communicate effectively with parents
- ✅ Stay organized with Google Sheets integration

**Happy Teaching! 🎓✨**
