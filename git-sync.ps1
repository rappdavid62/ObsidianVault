# git-sync.ps1
# Automates Obsidian Vault synchronization with GitHub (Universal Source of Truth)
#
# Usage:
#   .\git-sync.ps1

$ErrorActionPreference = "Stop"

# Set output encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  OBSIDIAN VAULT GITHUB SYNCHRONIZATION      " -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# 1. Verify Git is initialized
if (!(Test-Path .git)) {
    Write-Host "[ERROR] This folder is not a Git repository." -ForegroundColor Red
    Exit 1
}

# 2. Check for remote connectivity
Write-Host "Checking remote connection to GitHub..." -ForegroundColor Yellow
try {
    $remoteInfo = git remote -v
    if ($remoteInfo -match "origin") {
        Write-Host "Remote configured: origin" -ForegroundColor Green
    } else {
        Write-Host "[ERROR] No remote 'origin' configured." -ForegroundColor Red
        Exit 1
    }
} catch {
    Write-Host "[ERROR] Git commands failed. Check git installation." -ForegroundColor Red
    Exit 1
}

# 3. Pull latest changes from remote main
Write-Host "Pulling latest changes from remote (main)..." -ForegroundColor Yellow
try {
    # Pulling with --rebase to keep history clean and linear
    git pull origin main --rebase
    Write-Host "Pull complete. Vault is up-to-date with remote." -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Git pull failed or encountered conflicts." -ForegroundColor Yellow
    Write-Host "Attempting standard merge pull..." -ForegroundColor Yellow
    try {
        git pull origin main --no-rebase
        Write-Host "Merge pull complete." -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Pull failed. Please resolve conflicts manually." -ForegroundColor Red
        Exit 1
    }
}

# 4. Check status for local changes
$status = git status --porcelain
if ([string]::IsNullOrEmpty($status)) {
    Write-Host "No local changes detected. Vault matches remote." -ForegroundColor Green
    Write-Host "=============================================" -ForegroundColor Cyan
    Exit 0
}

Write-Host "Local changes detected:" -ForegroundColor Yellow
$status | ForEach-Object { Write-Host "  $_" -ForegroundColor Gray }

# 5. Add changes
Write-Host "Staging files..." -ForegroundColor Yellow
git add -A

# 6. Commit
$dateStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$commitMsg = "vault backup: $dateStr"
Write-Host "Committing changes with message: '$commitMsg'..." -ForegroundColor Yellow
git commit -m $commitMsg

# 7. Push to remote main
Write-Host "Pushing changes to GitHub (main)..." -ForegroundColor Yellow
try {
    git push origin main
    Write-Host "Push complete! Vault successfully synced to GitHub." -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Push failed. Check your network or credentials." -ForegroundColor Red
    Exit 1
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  SYNCHRONIZATION COMPLETED SUCCESSFULLY     " -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Cyan
