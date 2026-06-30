# start-vault-watcher.ps1
# Starts vault-watcher.py as a background process.
# Run at login or add to Task Scheduler.
# The watcher monitors the Library for changes and runs sync-all.py when files change.
# It also runs vault-health-check.py --fail-on-attention before any sync.

$vaultRoot  = "C:\ROOT_OBSIDIAN\DOV"
$watcherScript = "$vaultRoot\09-PROMPTS\Library\Tools\vault-watcher.py"
$logFile    = "$vaultRoot\09-PROMPTS\Library\Tools\vault-watcher.log"
$python     = "python"

# Check if already running
$existing = Get-Process python -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like "*vault-watcher*" }

if ($existing) {
    Write-Host "vault-watcher.py is already running (PID: $($existing.Id))" -ForegroundColor Yellow
    exit 0
}

if (-not (Test-Path $watcherScript)) {
    Write-Host "ERROR: vault-watcher.py not found at: $watcherScript" -ForegroundColor Red
    exit 1
}

Write-Host "Starting vault-watcher.py..." -ForegroundColor Green
Start-Process -FilePath $python `
    -ArgumentList "`"$watcherScript`"" `
    -WorkingDirectory $vaultRoot `
    -RedirectStandardOutput $logFile `
    -RedirectStandardError "$logFile.err" `
    -WindowStyle Hidden `
    -NoNewWindow:$false

Start-Sleep -Seconds 2

$proc = Get-Process python -ErrorAction SilentlyContinue |
    Where-Object { $_.CommandLine -like "*vault-watcher*" }

if ($proc) {
    Write-Host "vault-watcher.py started (PID: $($proc.Id))" -ForegroundColor Green
    Write-Host "Log: $logFile"
} else {
    Write-Host "vault-watcher.py may have failed to start. Check: $logFile" -ForegroundColor Red
}
