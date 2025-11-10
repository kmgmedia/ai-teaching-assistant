# Launch AI Teaching Assistant Dashboard
Write-Host "🎓 Starting AI Teaching Assistant Dashboard..." -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
$projectDir = "C:\Users\DELL\Desktop\ai_assistant_for_teachers"
Set-Location $projectDir

# Activate virtual environment
& "$projectDir\venv\Scripts\Activate.ps1"

# Launch Streamlit
Write-Host "🚀 Opening dashboard in your browser..." -ForegroundColor Green
Write-Host ""
streamlit run dashboard.py

# Keep window open if there's an error
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ Error launching dashboard. Press any key to exit..." -ForegroundColor Red
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}
