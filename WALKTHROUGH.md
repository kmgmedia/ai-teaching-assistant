# 🎓 Dashboard Walkthrough - Your AI Teaching Assistant

## 🚀 Getting Started

Your dashboard is now running! Here's how to use each feature:

---

## 1️⃣ HOME PAGE - Your Command Center

### What You'll See:

```
┌────────────────────────────────────────────────────┐
│        🎓 AI Teaching Assistant                    │
├────────────────────────────────────────────────────┤
│                                                    │
│  What Can I Do?              Quick Start          │
│  • Generate Lesson Notes     1. Select a tool     │
│  • Write Student Reports     2. Fill in details   │
│  • Draft Parent Messages     3. Click Generate    │
│  • Manage Students           4. Download result   │
│                                                    │
│  📈 Quick Stats                                    │
│  Total Students: 3    Avg Score: 84.3            │
│                                                    │
└────────────────────────────────────────────────────┘
```

**Try this**: Check your student stats pulled directly from Google Sheets!

---

## 2️⃣ LESSON GENERATOR - Create Lesson Plans

### Step-by-Step:

1. **Click "📝 Lesson Generator"** in the sidebar

2. **Fill in the form**:

   - **Subject**: e.g., "Mathematics"
   - **Topic**: e.g., "Introduction to Fractions"
   - **Age Group**: e.g., "7-8 years (Grade 2)"
   - **Duration**: Use slider (15-180 minutes)
   - **Objectives**: "Students will understand halves and quarters"

3. **Click "🚀 Generate Lesson Note"**

4. **Result**:
   - Professional lesson plan appears
   - Includes: Introduction, Main Activity, Conclusion, Evaluation
   - Download button to save as text file
   - Auto-saved to `data/output/lessons/`

### ⚡ Quick Test:

```
Subject: Science
Topic: Plant Life Cycle
Age Group: 6-7 years
Duration: 45 minutes
Objectives: Students will identify 4 stages of plant growth
```

---

## 3️⃣ REPORT GENERATOR - Professional Student Reports

### The Magic Feature: Google Sheets Integration! ✨

#### Option A: Load from Google Sheets (Recommended)

1. **Click "📊 Report Generator"** in sidebar

2. **Enable checkbox**: "📊 Load student data from Google Sheets"

3. **Select student** from dropdown:

   - Emma Johnson
   - Liam Chen
   - Sophia Adeleke

4. **Data auto-fills!**:

   - Student Name: ✅ Pre-filled
   - Subject: ✅ Pre-filled
   - Performance Notes: ✅ From your sheet
   - Behavior Notes: ✅ From your sheet

5. **Edit if needed** (optional tweaks)

6. **Enable "💾 Save report back to Google Sheets"**

7. **Click "🚀 Generate Report"**

8. **Result**:
   - Professional progress report
   - Saved to Google Sheets "Reports" tab
   - Download button for text file
   - Local copy in `data/output/reports/`

#### Option B: Manual Entry

- Uncheck "Load from Google Sheets"
- Fill in all fields manually
- Generate report

### 🎯 Try This Now:

1. Go to Report Generator
2. Select "Emma Johnson"
3. Watch the form auto-fill with her data!
4. Generate a report

---

## 4️⃣ PARENT MESSAGE - Draft Communications

### Choose Your Purpose:

1. **Click "💌 Parent Message"** in sidebar

2. **Select Purpose** from dropdown:

   - **Appreciation**: Celebrate achievements
   - **Reminder**: Events, deadlines, requirements
   - **Feedback**: Progress updates
   - **Concern**: Address issues constructively

3. **Fill in details**:

   - Child's Name
   - Your Name (optional)
   - Context: What do you want to communicate?

4. **Click "🚀 Generate Message"**

5. **Result**:
   - Professional, warm parent message
   - Ready to copy/paste into email
   - Download as text file

### 📝 Example Context (Appreciation):

```
Emma showed exceptional leadership during group math
activities this week. She patiently helped two classmates
understand fractions and encouraged them when they struggled.
```

**Result**: A warm, professional message praising Emma's kindness and leadership!

---

## 5️⃣ VIEW STUDENTS - Manage Your Roster

### Features:

1. **Click "👥 View Students"** in sidebar

2. **See full student table**:

   ```
   Name            | Subject | Score | Notes              | Behavior
   Emma Johnson    | Math    | 85    | Strong addition    | Active
   Liam Chen       | Reading | 90    | Excellent          | Focused
   Sophia Adeleke  | Science | 78    | Curious plants     | Great Q's
   ```

3. **View individual student**:

   - Select from dropdown
   - See detailed view with metrics
   - Notes and behavior displayed

4. **Quick Actions**:
   - **📊 Generate Report** - Jump to report generator
   - **💌 Send Parent Message** - Jump to message writer

### 🎯 Try This:

1. Go to View Students
2. Select a student
3. Click "Generate Report for This Student"
4. Watch it auto-fill in the Report Generator!

---

## 💡 Pro Tips & Tricks

### Tip 1: Keep Google Sheets Updated

Your dashboard reads from Google Sheets in real-time. Update your sheet, refresh the dashboard page (press R), and see new data!

### Tip 2: Keyboard Shortcuts

- **R**: Rerun/Refresh the dashboard
- **C**: Clear cache
- **Ctrl + Shift + R**: Hard refresh

### Tip 3: Download Everything

Every generated item has a download button. Save your favorites for reuse!

### Tip 4: Batch Process Reports

1. Go to View Students
2. Select first student
3. Generate report with "Save to Sheets" enabled
4. Go back, select next student
5. Repeat!

### Tip 5: Customize Prompts

Edit files in `core/prompts/` to change the tone and structure of generated content:

- `lesson_prompt.txt` - Lesson style
- `report_prompt.txt` - Report format
- `parent_prompt.txt` - Message tone

---

## 🔍 What Each Button Does

### Main Buttons:

- **🚀 Generate X** - Create AI content based on your inputs
- **⬇️ Download** - Save as text file to your computer
- **📊 Load from Sheets** - Pull data from Google Sheets
- **💾 Save to Sheets** - Write generated report back to Google Sheets

### Status Messages:

- **✅ Green**: Success! Operation completed
- **❌ Red**: Error - check your OpenAI billing or inputs
- **⚠️ Yellow**: Warning or information
- **ℹ️ Blue**: Helpful tips

---

## 📊 Real-Time Features

### Auto-Sync with Google Sheets:

- Student count updates automatically
- Average scores calculated live
- New students appear in dropdowns
- Reports saved to "Reports" tab instantly

### Smart Forms:

- Required fields marked with \*
- Validation before generation
- Helpful placeholder text
- Character count for text areas

---

## 🎬 Complete Workflow Example

### Scenario: Weekly Report Generation

**Monday Morning:**

1. **Update Google Sheet** with latest scores/notes
2. **Open Dashboard** (http://localhost:8501)
3. **Go to "👥 View Students"**
4. **Verify** all 3 students show up

**Generate Reports:**

For each student:

1. **Go to "📊 Report Generator"**
2. **Select student** from dropdown
3. **Review** auto-filled data
4. **Add** any additional notes
5. **Enable** "Save to Google Sheets"
6. **Click** "Generate Report"
7. **Download** for your records

**Result**:

- ✅ 3 professional reports in 5 minutes
- ✅ All saved to Google Sheets "Reports" tab
- ✅ Local copies in `data/output/reports/`
- ✅ Ready to share with parents!

---

## 🔧 Troubleshooting in Dashboard

### If you see "Unable to load students":

1. Check Google Sheets is properly shared with service account
2. Verify Sheet ID in `.env` file
3. Refresh the page (press R)

### If generation fails:

1. **Check OpenAI billing** - Add payment method
2. View error message in red box
3. Check `logs/app.log` for details

### If dashboard won't load:

```powershell
# Restart the dashboard
Ctrl+C  # Stop current server
streamlit run dashboard.py
```

---

## 🎯 Your Next Steps

### Immediate Actions:

1. ✅ **Test each page** - Click through all 5 sections
2. ✅ **Generate a test report** - Use Emma Johnson
3. ✅ **Check Google Sheets** - See if report appears in "Reports" tab
4. ✅ **Try a lesson plan** - Pick any subject

### Once OpenAI Billing is Fixed:

1. 🚀 Generate reports for all students
2. 🚀 Create week's lesson plans
3. 🚀 Draft appreciation messages
4. 🚀 Set up weekly workflow

### Advanced:

1. 📝 Customize prompts in `core/prompts/`
2. 📊 Add more students to Google Sheets
3. 🔄 Create automation scripts (use the API)
4. 🎨 Adjust dashboard theme in Streamlit settings

---

## 📞 Quick Reference

### Dashboard URL:

```
http://localhost:8501
```

### Launch Command:

```powershell
streamlit run dashboard.py
```

### Stop Dashboard:

```
Press Ctrl+C in the terminal
```

### Restart Dashboard:

```powershell
# If changes made to code
streamlit run dashboard.py
```

---

## 🎉 You're Ready to Go!

Your AI Teaching Assistant dashboard is fully operational! Start by:

1. **Opening** http://localhost:8501
2. **Clicking** "👥 View Students"
3. **Selecting** Emma Johnson
4. **Clicking** "Generate Report for This Student"
5. **Watching** the magic happen! ✨

**Questions?** Check:

- `DASHBOARD_GUIDE.md` - This file
- `API_USAGE_GUIDE.md` - API reference
- `README.md` - Complete documentation

---

**Happy Teaching! 🎓✨**

_Your AI assistant is ready to save you hours of work!_
