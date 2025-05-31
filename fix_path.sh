#!/bin/bash

# Fix the hackingtool path issue
echo "Fixing hackingtool path issue..."

# Define path file location and default path
PATHFILE=~/hackingtoolpath.txt
TOOLSPATH="/home/kali/hackingtool"

# Create directory if it doesn't exist
mkdir -p "$TOOLSPATH"

# Delete path file if empty or overwrite with correct content
if [ -f "$PATHFILE" ] && [ ! -s "$PATHFILE" ]; then
    echo "Empty path file found. Removing..."
    rm "$PATHFILE"
fi

# Create or overwrite path file
echo "$TOOLSPATH" > "$PATHFILE"
echo "Path file updated with: $TOOLSPATH"

# Test read the file
echo "Current path file content: $(cat $PATHFILE)"

echo "Fix complete. You can now run 'sudo hackingtool'" 