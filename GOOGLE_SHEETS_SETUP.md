# Google Sheets Setup Guide

Follow these steps to enable Google Sheets integration for the AI Teaching Assistant.

---

## Step 1: Create a Google Cloud Project

1. **Go to**: [https://console.cloud.google.com/projectcreate](https://console.cloud.google.com/projectcreate)
2. **Project Name**: Enter "AI Teaching Assistant" (or any name you prefer)
3. **Click**: "CREATE"
4. **Wait**: A few seconds for the project to be created

---

## Step 2: Enable Required APIs

### Enable Google Sheets API

1. **Go to**: [https://console.cloud.google.com/apis/library/sheets.googleapis.com](https://console.cloud.google.com/apis/library/sheets.googleapis.com)
2. **Select** your project from the dropdown at the top
3. **Click**: "ENABLE"

### Enable Google Drive API

1. **Go to**: [https://console.cloud.google.com/apis/library/drive.googleapis.com](https://console.cloud.google.com/apis/library/drive.googleapis.com)
2. **Select** your project
3. **Click**: "ENABLE"

---

## Step 3: Create a Service Account

1. **Go to**: [https://console.cloud.google.com/iam-admin/serviceaccounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
2. **Select** your project
3. **Click**: "CREATE SERVICE ACCOUNT"
4. **Service account details**:
   - Name: `teaching-assistant-bot`
   - Description: "Service account for AI Teaching Assistant to access Google Sheets"
5. **Click**: "CREATE AND CONTINUE"
6. **Grant this service account access** (optional): Skip this step, click "CONTINUE"
7. **Grant users access** (optional): Skip this step, click "DONE"

---

## Step 4: Create and Download Service Account Key

1. **Find your service account** in the list (should be `teaching-assistant-bot@...`)
2. **Click** on the service account email to open details
3. **Go to** the "KEYS" tab
4. **Click**: "ADD KEY" → "Create new key"
5. **Select**: "JSON" format
6. **Click**: "CREATE"
7. **Save** the downloaded JSON file to your project folder:
   ```
   C:\Users\DELL\Desktop\ai_assistant_for_teachers\credentials\
   ```
   Name it: `google-sheets-credentials.json`

---

## Step 5: Create Your Google Sheet

### Option A: Create New Sheet

1. **Go to**: [https://sheets.google.com](https://sheets.google.com)
2. **Click**: "Blank" to create a new sheet
3. **Name it**: "Student Data - AI Assistant"

### Option B: Use Template

I'll create a template sheet for you with the correct structure.

### Sheet Structure

**Tab 1: Students** (for student roster and data)

| Name            | Subject | Score | Notes                            | Behavior              |
| --------------- | ------- | ----- | -------------------------------- | --------------------- |
| Emma Johnson    | Math    | 85    | Strong understanding of addition | Participates actively |
| Liam Chen       | Reading | 90    | Excellent comprehension          | Very focused          |
| Sophia Martinez | Science | 78    | Curious about plants             | Asks great questions  |

**Tab 2: Reports** (where generated reports will be saved)

| Student Name                           | Report | Timestamp |
| -------------------------------------- | ------ | --------- |
| (Empty - reports will be written here) |        |           |

---

## Step 6: Share Sheet with Service Account

**IMPORTANT**: The service account needs permission to access your sheet!

1. **Open your Google Sheet**
2. **Click**: "Share" button (top right)
3. **Copy** the service account email from your credentials JSON file:
   - Open the JSON file and find the `"client_email"` field
   - It looks like: `teaching-assistant-bot@your-project.iam.gserviceaccount.com`
4. **Paste** this email in the "Add people and groups" field
5. **Select**: "Editor" role
6. **Uncheck**: "Notify people" (no need to send email to a bot!)
7. **Click**: "Share"

---

## Step 7: Get Your Sheet ID

1. **Open your Google Sheet**
2. **Look at the URL**:
   ```
   https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID_HERE/edit
   ```
3. **Copy** the long string between `/d/` and `/edit`
4. **Example**:
   - URL: `https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit`
   - Sheet ID: `1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`

---

## Step 8: Update Your .env File

Update these two lines in your `.env` file:

```env
GOOGLE_SHEETS_CREDENTIALS=credentials/google-sheets-credentials.json
GOOGLE_SHEET_ID=YOUR_SHEET_ID_FROM_STEP_7
```

---

## Step 9: Test the Connection

Run this command to test if everything works:

```powershell
python integrations\google_sheets.py
```

You should see:

```
Testing Google Sheets connection...
✅ Connection successful!
✅ Found X student records
```

---

## Troubleshooting

### Error: "Credentials file not found"

- Check the path in `.env` matches where you saved the JSON file
- Use forward slashes: `credentials/google-sheets-credentials.json`

### Error: "Permission denied" or "Requested entity was not found"

- Make sure you shared the sheet with the service account email
- Double-check the Sheet ID in `.env`
- Verify both APIs are enabled (Sheets + Drive)

### Error: "The caller does not have permission"

- The service account email must be added as an Editor to your sheet
- Check the "Share" settings on your Google Sheet

---

## Quick Reference

**Service Account Email Format**:

```
teaching-assistant-bot@your-project-id.iam.gserviceaccount.com
```

**Sheet ID Location**:

```
https://docs.google.com/spreadsheets/d/[SHEET_ID_HERE]/edit
```

**Credentials File Location**:

```
ai_assistant_for_teachers/credentials/google-sheets-credentials.json
```

---

## Next Steps

After setup is complete:

1. Test the connection
2. Populate your sheet with student data
3. Generate your first automated report!

---

**Need Help?** If you get stuck at any step, let me know which step number and I'll help troubleshoot!
