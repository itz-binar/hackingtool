# Script to help replace hackingtool images with new screenshots
$ErrorActionPreference = "Stop"

# Add required assemblies for screenshot capture
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Function to capture a screenshot
function Capture-Screenshot {
    param(
        [string]$outputPath,
        [string]$imageName
    )
    
    Write-Host ""
    Write-Host "Ready to capture $imageName" -ForegroundColor Cyan
    Write-Host "Please set up your terminal to show the correct screen now."
    Write-Host "Press Enter when ready to capture the screenshot..." -ForegroundColor Yellow
    $null = Read-Host
    
    # Create a bitmap of the primary screen
    $screen = [System.Windows.Forms.Screen]::PrimaryScreen
    $bitmap = New-Object System.Drawing.Bitmap $screen.Bounds.Width, $screen.Bounds.Height
    
    # Create a graphics object from the bitmap
    $graphic = [System.Drawing.Graphics]::FromImage($bitmap)
    
    # Capture the screen
    $graphic.CopyFromScreen($screen.Bounds.X, $screen.Bounds.Y, 0, 0, $screen.Bounds.Size)
    
    # Save the screenshot
    $bitmap.Save($outputPath, [System.Drawing.Imaging.ImageFormat]::Png)
    
    # Dispose objects
    $graphic.Dispose()
    $bitmap.Dispose()
    
    Write-Host "Screenshot captured and saved as $outputPath" -ForegroundColor Green
    Write-Host ""
    
    return $true
}

# Main process
Write-Host "=== HACKINGTOOL SCREENSHOT UTILITY ===" -ForegroundColor Cyan
Write-Host "This utility will help you capture screenshots and save them to the appropriate files."
Write-Host ""

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

Write-Host ""
Write-Host "INSTRUCTIONS:" -ForegroundColor Yellow
Write-Host "1. You will be prompted to set up each screen before capturing"
Write-Host "2. For each image, navigate to the appropriate menu in hackingtool"
Write-Host "3. When the screen is ready, press Enter to capture"
Write-Host ""
Write-Host "Press Enter to begin the capture process..." -ForegroundColor Green
$null = Read-Host

# Capture the screenshots one by one
$success = $true

# A00.png - Anonymously Hiding Tool
Write-Host "====== CAPTURE 1 OF 5 ======" -ForegroundColor Cyan
Write-Host "Navigate to the Anonymously Hiding Tool menu"
Write-Host "This should show [1] Anonymously Surf, [2] Multitor options"
$success = $success -and (Capture-Screenshot -outputPath "images/A00.png" -imageName "A00.png (Anonymously Hiding Tool)")

# A0.png - Main Menu
Write-Host "====== CAPTURE 2 OF 5 ======" -ForegroundColor Cyan
Write-Host "Navigate to the main menu"
Write-Host "This should show the main menu with the orange HACKING TOOL text"
$success = $success -and (Capture-Screenshot -outputPath "images/A0.png" -imageName "A0.png (Main Menu)")

# A1.png - Information Gathering Tools
Write-Host "====== CAPTURE 3 OF 5 ======" -ForegroundColor Cyan
Write-Host "Navigate to the Information Gathering Tools menu"
Write-Host "This should show options like Nmap, Dracnmap, etc."
$success = $success -and (Capture-Screenshot -outputPath "images/A1.png" -imageName "A1.png (Information Gathering Tools)")

# A2.png - Wireless Attack Tools
Write-Host "====== CAPTURE 4 OF 5 ======" -ForegroundColor Cyan
Write-Host "Navigate to the Wireless Attack Tools menu"
Write-Host "This should show WiFi-Pumpkin, pixiewps, etc."
$success = $success -and (Capture-Screenshot -outputPath "images/A2.png" -imageName "A2.png (Wireless Attack Tools)")

# A4.png - Anonsurf Tool
Write-Host "====== CAPTURE 5 OF 5 ======" -ForegroundColor Cyan
Write-Host "Navigate to the Anonsurf Tool screen"
Write-Host "This should show the skull icon and Anonsurf options"
$success = $success -and (Capture-Screenshot -outputPath "images/A4.png" -imageName "A4.png (Anonsurf Tool)")

if ($success) {
    Write-Host ""
    Write-Host "All screenshots successfully captured and saved!" -ForegroundColor Green
    Write-Host "The original images were backed up to $backupDir" -ForegroundColor Green
    Write-Host ""
    Write-Host "When you push these changes to GitHub, the README will display the new screenshots."
} else {
    Write-Host ""
    Write-Host "Some screenshots could not be captured. Check the errors above." -ForegroundColor Red
} 