# AI Teaching Assistant API Guide

## 🚀 Server is Running!

**Base URL**: `http://127.0.0.1:5000`

---

## 📡 Available Endpoints

### 1. Health Check

**GET** `/`

Test if the server is running.

```bash
# Browser
http://127.0.0.1:5000

# PowerShell
Invoke-RestMethod -Uri "http://127.0.0.1:5000" -Method Get
```

---

### 2. Generate Lesson Note

**POST** `/generate/lesson`

Create a structured lesson plan.

**PowerShell Example:**

```powershell
$body = @{
    subject = "Mathematics"
    topic = "Introduction to Fractions"
    age_group = "7-8 years (Grade 2)"
    objectives = "Students will understand what fractions are and identify halves and quarters"
    duration = 45
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/generate/lesson" -Method Post -Body $body -ContentType "application/json"
```

**Required Fields:**

- `subject`: Subject name (e.g., "Math", "Science")
- `topic`: Specific topic
- `age_group`: Target age group
- `objectives`: Learning objectives
- `duration`: Lesson duration in minutes (optional, default: 60)

---

### 3. Generate Student Report

**POST** `/generate/report`

Create a professional progress report.

**PowerShell Example:**

```powershell
$body = @{
    student_name = "Emma Johnson"
    period = "Term 1 (September-December 2025)"
    subject = "Overall Progress"
    performance_notes = "Strong understanding of addition. Excellent reading comprehension."
    behavior_notes = "Participates actively in class. Works well with peers."
    save_to_sheets = $true
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/generate/report" -Method Post -Body $body -ContentType "application/json"
```

**Required Fields:**

- `student_name`: Student's full name
- `period`: Reporting period
- `subject`: Subject or "Overall Progress"
- `performance_notes`: Academic observations
- `behavior_notes`: Behavioral observations
- `save_to_sheets`: Boolean - save to Google Sheets? (optional)

---

### 4. Generate Parent Message

**POST** `/generate/parent-message`

Draft a message for parents.

**PowerShell Example:**

```powershell
$body = @{
    purpose = "appreciation"
    child_name = "Emma Johnson"
    context = "Emma showed exceptional kindness by helping a new student feel welcome during lunch break."
    teacher_name = "Ms. Sarah Thompson"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/generate/parent-message" -Method Post -Body $body -ContentType "application/json"
```

**Required Fields:**

- `purpose`: "reminder", "feedback", "appreciation", or "concern"
- `child_name`: Student's name
- `context`: Details about the message
- `teacher_name`: Your name (optional)

---

### 5. Get All Students

**GET** `/students`

Retrieve all students from your Google Sheet.

**PowerShell Example:**

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/students" -Method Get
```

---

### 6. Get Specific Student

**GET** `/students/<name>`

Get data for a specific student.

**PowerShell Example:**

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/students/Emma Johnson" -Method Get
```

---

## 🧪 Quick Test Commands

### Test 1: Check Server

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000" -Method Get
```

### Test 2: Get Students from Sheet

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/students" -Method Get
```

### Test 3: Get Specific Student

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/students/Emma Johnson" -Method Get
```

### Test 4: Generate a Lesson Note (Quick)

```powershell
$lesson = @{
    subject = "Math"
    topic = "Counting to 10"
    age_group = "4-5 years"
    objectives = "Students will count from 1 to 10"
    duration = 30
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://127.0.0.1:5000/generate/lesson" -Method Post -Body $lesson -ContentType "application/json"
```

---

## 💡 Tips

### Viewing Generated Files

All generated content is saved to:

```
C:\Users\DELL\Desktop\ai_assistant_for_teachers\data\output\
```

Subfolders:

- `lessons/` - Lesson notes
- `reports/` - Student reports
- `parent_messages/` - Parent communications

### Checking Logs

```
C:\Users\DELL\Desktop\ai_assistant_for_teachers\logs\app.log
```

### Stopping the Server

Press **CTRL+C** in the terminal where the server is running.

---

## 🔥 Complete Example: Generate Report from Google Sheets

This pulls Emma's data from your sheet and generates a report:

```powershell
# 1. Get Emma's data
$student = Invoke-RestMethod -Uri "http://127.0.0.1:5000/students/Emma Johnson" -Method Get

# 2. Generate report with her data
$reportBody = @{
    student_name = $student.student.Name
    period = "Term 1 (2025)"
    subject = $student.student.Subject
    performance_notes = $student.student.Notes
    behavior_notes = $student.student.Behavior
    save_to_sheets = $true
} | ConvertTo-Json

$report = Invoke-RestMethod -Uri "http://127.0.0.1:5000/generate/report" -Method Post -Body $reportBody -ContentType "application/json"

# 3. View the report
$report.report
```

---

## 🎯 Next Steps

1. **Try the test commands above** to see the API in action
2. **Add more students** to your Google Sheet
3. **Generate reports** for all your students
4. **Create lesson notes** for your upcoming classes
5. **Send parent messages** with one API call

---

## 🆘 Troubleshooting

**Server not responding?**

- Check if it's still running in the terminal
- Restart with: `python main.py`

**API errors?**

- Check your OpenAI API key and billing
- View logs: `logs\app.log`

**Google Sheets not working?**

- Verify service account has access to the sheet
- Check Sheet ID in `.env`

---

**Happy teaching! 🎓✨**
