# git-sync.ps1
# Automates Obsidian Vault synchronization with GitHub
# Implements 3-Layer Sync Safety (Local Backups + Isolated Remote + Script Guardrails)
#
# Usage:
#   .\git-sync.ps1

$ErrorActionPreference = "Stop"

# Set output encoding to UTF-8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  OBSIDIAN VAULT GITHUB SYNCHRONIZATION      " -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# Ensure we are running from the script's directory
Set-Location $PSScriptRoot

# Helper to run Git commands and check exit codes
function Run-Git ($commandArgs, $errorMsg) {
    & git $commandArgs
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERROR] $errorMsg (Exit Code: $LASTEXITCODE)" -ForegroundColor Red
        Exit 1
    }
}

# ---------------------------------------------------------
# LAYER 1: AUTOMATED LOCAL SNAPSHOT (Backup)
# ---------------------------------------------------------
Write-Host "[Layer 1] Creating local vault snapshot..." -ForegroundColor Yellow

$backupDir = Join-Path $PSScriptRoot ".backups"
if (!(Test-Path $backupDir)) {
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
}

# Keep only the last 10 backups to prevent disk bloat
$oldBackups = Get-ChildItem -Path $backupDir -Filter "vault_backup_*.zip" | Sort-Object LastWriteTime
if ($oldBackups.Count -ge 10) {
    $deleteCount = $oldBackups.Count - 9
    Write-Host "Cleaning up $deleteCount old backup(s)..." -ForegroundColor Gray
    $oldBackups[0..($deleteCount - 1)] | Remove-Item -Force
}

# Generate new zip snapshot
$dateStr = Get-Date -Format "yyyyMMdd_HHmmss"
$zipPath = Join-Path $backupDir "vault_backup_$dateStr.zip"

try {
    # Gather root files and folders excluding .git, .backups, .trash, and .codex
    $itemsToCompress = Get-ChildItem -Path $PSScriptRoot | Where-Object { 
        $_.Name -ne ".git" -and 
        $_.Name -ne ".backups" -and 
        $_.Name -ne ".trash" -and 
        $_.Name -ne ".codex"
    }
    
    if ($itemsToCompress) {
        Compress-Archive -Path $itemsToCompress.FullName -DestinationPath $zipPath -Force
        Write-Host "Backup snapshot created successfully: $(Split-Path $zipPath -Leaf)" -ForegroundColor Green
    } else {
        Write-Host "No files to backup." -ForegroundColor Yellow
    }
} catch {
    Write-Host "[WARNING] Local backup failed: $_" -ForegroundColor Yellow
    Write-Host "Proceeding with caution..." -ForegroundColor Yellow
}

# ---------------------------------------------------------
# LAYER 2 & 3: ISOLATED REMOTE & GUARDED GIT SYNC
# ---------------------------------------------------------
Write-Host "[Layer 2 & 3] Verifying Git environment..." -ForegroundColor Yellow

# 1. Verify Git repo
if (!(Test-Path .git)) {
    Write-Host "[ERROR] This folder is not initialized as a Git repository." -ForegroundColor Red
    Exit 1
}

# 2. Verify we are on 'main' branch
& git branch --show-current
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to query current git branch." -ForegroundColor Red
    Exit 1
}
$currentBranch = (git branch --show-current).Trim()
if ($currentBranch -ne "main") {
    Write-Host "[ERROR] Not on the 'main' branch! Current branch is: $currentBranch" -ForegroundColor Red
    Exit 1
}

# 3. Verify remote points to production repo (Layer 2)
try {
    $remoteUrl = (git remote get-url origin).Trim()
    if ($remoteUrl -notmatch "ObsidianVault") {
        Write-Host "[ERROR] Remote URL is incorrect: $remoteUrl" -ForegroundColor Red
        Write-Host "Production remote MUST point to a repository containing 'ObsidianVault'." -ForegroundColor Red
        Exit 1
    }
    Write-Host "Safe Remote Verified: $remoteUrl" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] No remote 'origin' configured or git command failed." -ForegroundColor Red
    Exit 1
}

# 4. Pull remote changes safely (fails if repo is not found or conflicts occur)
Write-Host "Pulling changes from GitHub (main)..." -ForegroundColor Yellow
Run-Git @("pull", "origin", "main", "--no-rebase") "Pull failed or conflict detected. Aborting sync to protect local files. Your local backup is safe in .backups/"

# 5. Check status for local changes
$status = git status --porcelain
if ([string]::IsNullOrEmpty($status)) {
    Write-Host "No local changes detected. Vault matches remote." -ForegroundColor Green
    Write-Host "=============================================" -ForegroundColor Cyan
    Exit 0
}

Write-Host "Local changes detected. Staging and committing..." -ForegroundColor Yellow
Run-Git @("add", "-A") "Failed to stage local changes."

$commitDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Run-Git @("commit", "-m", "vault backup: $commitDate") "Failed to commit changes."

# 6. Push to remote main (No force-push allowed)
Write-Host "Pushing to GitHub (main)..." -ForegroundColor Yellow
Run-Git @("push", "origin", "main") "Push failed. Check your network or GitHub credentials."

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "  SYNCHRONIZATION COMPLETED SUCCESSFULLY     " -ForegroundColor Green
Write-Host "=============================================" -ForegroundColor Cyan
