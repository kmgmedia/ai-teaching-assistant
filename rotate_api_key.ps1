# 🔐 API Key Rotation Script
# Run this script when you need to rotate your OpenAI API key for production

Write-Host "`n🔒 API Key Rotation Helper`n" -ForegroundColor Cyan
Write-Host "This script will guide you through rotating your OpenAI API key safely.`n"

# Step 1: Verify .env is not tracked
Write-Host "Step 1: Checking if .env is properly gitignored..." -ForegroundColor Yellow
$gitStatus = git status --short .env 2>&1
if ($gitStatus -like "*fatal*" -or $gitStatus -eq "") {
    Write-Host "✅ .env is NOT tracked by Git (secure)`n" -ForegroundColor Green
} else {
    Write-Host "⚠️  WARNING: .env appears in git status!" -ForegroundColor Red
    Write-Host "Run: git rm --cached .env`n" -ForegroundColor Red
    exit 1
}

# Step 2: Backup current .env
Write-Host "Step 2: Creating backup of current .env..." -ForegroundColor Yellow
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
Copy-Item .env ".env.backup.$timestamp"
Write-Host "✅ Backup created: .env.backup.$timestamp`n" -ForegroundColor Green

# Step 3: Instructions for getting new key
Write-Host "Step 3: Get your new OpenAI API key" -ForegroundColor Yellow
Write-Host "1. Open: https://platform.openai.com/api-keys" -ForegroundColor White
Write-Host "2. Click 'Create new secret key'" -ForegroundColor White
Write-Host "3. Name it: 'AI Teaching Assistant - Production'" -ForegroundColor White
Write-Host "4. Copy the new key (starts with sk-proj-...)" -ForegroundColor White
Write-Host ""

# Step 4: Prompt for new key
$newKey = Read-Host "Paste your NEW OpenAI API key here (or press Enter to skip)"

if ($newKey -eq "") {
    Write-Host "`n⚠️  Skipping key rotation. Remember to update manually!`n" -ForegroundColor Yellow
    exit 0
}

# Step 5: Validate key format
if ($newKey -notmatch "^sk-proj-[a-zA-Z0-9_-]+$") {
    Write-Host "`n❌ Invalid key format! OpenAI keys should start with 'sk-proj-'`n" -ForegroundColor Red
    exit 1
}

# Step 6: Update .env file
Write-Host "`nStep 4: Updating .env file..." -ForegroundColor Yellow
$envContent = Get-Content .env
$envContent = $envContent -replace 'OPENAI_API_KEY=sk-proj-[a-zA-Z0-9_-]+', "OPENAI_API_KEY=$newKey"
$envContent | Set-Content .env
Write-Host "✅ .env updated with new API key`n" -ForegroundColor Green

# Step 7: Verify no key in git
Write-Host "Step 5: Verifying key is not in git..." -ForegroundColor Yellow
$gitGrep = git grep "sk-proj-" 2>&1
if ($gitGrep -like "*fatal*" -or $gitGrep -eq "") {
    Write-Host "✅ No API keys found in git-tracked files`n" -ForegroundColor Green
} else {
    Write-Host "⚠️  WARNING: Found API key in tracked files:" -ForegroundColor Red
    Write-Host $gitGrep -ForegroundColor Red
    Write-Host "`nPlease remove hardcoded keys before deploying!`n" -ForegroundColor Red
}

# Step 8: Test new key
Write-Host "Step 6: Testing new API key..." -ForegroundColor Yellow
Write-Host "Run this command to test:" -ForegroundColor White
Write-Host "  venv\Scripts\python.exe -c `"import openai; openai.api_key='$newKey'; print('✅ Key is valid')`"`n" -ForegroundColor Cyan

# Step 9: Reminders
Write-Host "📋 Next Steps:" -ForegroundColor Cyan
Write-Host "1. ✅ Test the new API key locally" -ForegroundColor White
Write-Host "2. ⚠️  REVOKE the old key at https://platform.openai.com/api-keys" -ForegroundColor White
Write-Host "3. 🚀 Update production environment variables:" -ForegroundColor White
Write-Host "   - Streamlit Cloud: Settings → Secrets" -ForegroundColor Gray
Write-Host "   - Heroku: heroku config:set OPENAI_API_KEY=$newKey" -ForegroundColor Gray
Write-Host "   - Railway/Render: Dashboard → Environment Variables`n" -ForegroundColor Gray

Write-Host "🔒 Security complete! Your API key has been rotated.`n" -ForegroundColor Green
