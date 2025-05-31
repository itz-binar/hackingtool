# PowerShell script to backup and prepare for updating the hackingtool images
$ErrorActionPreference = "Stop"

# Make sure the images directory exists
if (-not (Test-Path -Path "images")) {
    Write-Host "Images directory not found. Creating it now..."
    New-Item -ItemType Directory -Path "images"
}

# Create a backup directory
$backupDir = "images/backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')"
New-Item -ItemType Directory -Path $backupDir -Force | Out-Null

# Backup existing images
Write-Host "Backing up existing images..."
if (Test-Path -Path "images/A00.png") { Copy-Item -Path "images/A00.png" -Destination "$backupDir/A00.png" -Force }
if (Test-Path -Path "images/A0.png") { Copy-Item -Path "images/A0.png" -Destination "$backupDir/A0.png" -Force }
if (Test-Path -Path "images/A1.png") { Copy-Item -Path "images/A1.png" -Destination "$backupDir/A1.png" -Force }
if (Test-Path -Path "images/A2.png") { Copy-Item -Path "images/A2.png" -Destination "$backupDir/A2.png" -Force }
if (Test-Path -Path "images/A4.png") { Copy-Item -Path "images/A4.png" -Destination "$backupDir/A4.png" -Force }

Write-Host "Original images backed up to $backupDir"
Write-Host ""
Write-Host "=============== INSTRUCTIONS ==============="
Write-Host "To update the images:"
Write-Host ""
Write-Host "1. Take screenshots of each menu in hackingtool"
Write-Host "2. Save them with the following names in the 'images' folder:"
Write-Host "   - A00.png: Anonymously Hiding Tool menu"
Write-Host "   - A0.png: Main Menu"
Write-Host "   - A1.png: Information Gathering Tools menu"
Write-Host "   - A2.png: Wireless Attack Tools menu"
Write-Host "   - A4.png: Anonsurf Tool"
Write-Host ""
Write-Host "If you need to restore the original images, they are in: $backupDir"
Write-Host "=============================================" 