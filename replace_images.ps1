# Script to help replace hackingtool images with new screenshots
$ErrorActionPreference = "Stop"

# Configuration - paths to your new screenshots
# Update these paths to point to where you saved your screenshots
$screenshotA00 = "path\to\your\anonymously_hiding_tools_screenshot.png"
$screenshotA0 = "path\to\your\main_menu_screenshot.png"
$screenshotA1 = "path\to\your\information_gathering_tools_screenshot.png"
$screenshotA2 = "path\to\your\wireless_attack_tools_screenshot.png"
$screenshotA4 = "path\to\your\anonsurf_screenshot.png"

# Function to copy a file with validation
function Copy-Screenshot {
    param(
        [string]$sourcePath,
        [string]$destinationPath,
        [string]$imageName
    )
    
    if (-not (Test-Path -Path $sourcePath)) {
        Write-Host "ERROR: Screenshot not found at path: $sourcePath" -ForegroundColor Red
        return $false
    }
    
    try {
        Copy-Item -Path $sourcePath -Destination $destinationPath -Force
        Write-Host "SUCCESS: Updated $imageName" -ForegroundColor Green
        return $true
    } catch {
        Write-Host "ERROR: Failed to copy $imageName. Error: $_" -ForegroundColor Red
        return $false
    }
}

# Main process
Write-Host "=== HACKINGTOOL IMAGE REPLACEMENT UTILITY ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "This script will replace the existing images with your new screenshots."
Write-Host "First, edit this script and update the paths at the top to point to your screenshot files."
Write-Host ""
Write-Host "Then run the script again to perform the replacement."
Write-Host ""

# Check if the paths have been updated
$defaultPath = "path\to\your"
if ($screenshotA00 -like "*$defaultPath*") {
    Write-Host "IMPORTANT: You need to edit this script first!" -ForegroundColor Yellow
    Write-Host "Update the screenshot path variables at the top of the script with your actual file paths." -ForegroundColor Yellow
    Write-Host "Then run the script again." -ForegroundColor Yellow
    exit
}

# Create a backup if it doesn't exist yet
$backupDir = "images/backup_before_replace"
if (-not (Test-Path -Path $backupDir)) {
    Write-Host "Creating backup of original images..." -ForegroundColor Cyan
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    
    if (Test-Path -Path "images/A00.png") { Copy-Item -Path "images/A00.png" -Destination "$backupDir/A00.png" -Force }
    if (Test-Path -Path "images/A0.png") { Copy-Item -Path "images/A0.png" -Destination "$backupDir/A0.png" -Force }
    if (Test-Path -Path "images/A1.png") { Copy-Item -Path "images/A1.png" -Destination "$backupDir/A1.png" -Force }
    if (Test-Path -Path "images/A2.png") { Copy-Item -Path "images/A2.png" -Destination "$backupDir/A2.png" -Force }
    if (Test-Path -Path "images/A4.png") { Copy-Item -Path "images/A4.png" -Destination "$backupDir/A4.png" -Force }
    
    Write-Host "Backup created in $backupDir" -ForegroundColor Green
}

# Replace the images
Write-Host "Replacing images with new screenshots..." -ForegroundColor Cyan
$success = $true

$success = $success -and (Copy-Screenshot -sourcePath $screenshotA00 -destinationPath "images/A00.png" -imageName "A00.png (Anonymously Hiding Tool)")
$success = $success -and (Copy-Screenshot -sourcePath $screenshotA0 -destinationPath "images/A0.png" -imageName "A0.png (Main Menu)")
$success = $success -and (Copy-Screenshot -sourcePath $screenshotA1 -destinationPath "images/A1.png" -imageName "A1.png (Information Gathering Tools)")
$success = $success -and (Copy-Screenshot -sourcePath $screenshotA2 -destinationPath "images/A2.png" -imageName "A2.png (Wireless Attack Tools)")
$success = $success -and (Copy-Screenshot -sourcePath $screenshotA4 -destinationPath "images/A4.png" -imageName "A4.png (Anonsurf Tool)")

if ($success) {
    Write-Host ""
    Write-Host "All images successfully replaced!" -ForegroundColor Green
    Write-Host "The original images were backed up to $backupDir" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Some images could not be replaced. Check the errors above." -ForegroundColor Red
    Write-Host "The original images were backed up to $backupDir" -ForegroundColor Green
} 