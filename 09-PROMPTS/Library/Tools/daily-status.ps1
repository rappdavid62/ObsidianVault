# daily-status.ps1
# Opens a pre-filled daily status block for David to fill in and paste into any AI session.
# Place this in the vault Tools folder or create a Desktop shortcut to run it.
# Usage: Right-click > Run with PowerShell, or call from Antigravity.

$date = Get-Date -Format "yyyy-MM-dd"
$day  = Get-Date -Format "dddd"

$template = @"
CURRENT STATUS — $date ($day)

Location: Cincinnati, Ohio
Energy: [collapse / low / medium / high]
Brain fog: [none / mild / heavy]
Sleep last night: [hours / quality]
Money runway: [weeks / tight / stable]
Job status: [applications sent / interviews / nothing]
Main job target today:
Top active project: [SNF / job search / Obsidian / other]
Device status: [phone / tablet / laptop ok or broken]
Biggest constraint today:
One non-negotiable today:
What I need from AI right now:
What should be ignored for now:

--- COPY EVERYTHING ABOVE THIS LINE ---
"@

# Write to a temp file and open it
$tmpFile = "$env:TEMP\david_status_$date.txt"
$template | Out-File -FilePath $tmpFile -Encoding UTF8

# Try to copy to clipboard
try {
    $template | Set-Clipboard
    Write-Host "STATUS BLOCK COPIED TO CLIPBOARD." -ForegroundColor Green
} catch {
    Write-Host "Clipboard not available — open the file below." -ForegroundColor Yellow
}

# Open in notepad for editing
Start-Process notepad.exe $tmpFile

Write-Host ""
Write-Host "File saved to: $tmpFile" -ForegroundColor Cyan
Write-Host "Fill it in, then paste it into Antigravity or any AI session."
Write-Host ""
Write-Host "Quick vault health check..."
python "C:\ROOT_OBSIDIAN\DOV\09-PROMPTS\Library\Tools\vault-health-check.py" 2>$null | Select-Object -First 20
