#!/bin/bash

cd /home/kali/Desktop/itzbinar/hackingtool
# Create virtualenv if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Fix the path file issue - delete any empty file and create a new one with content
PATHFILE=~/hackingtoolpath.txt
# Check if file exists but is empty
if [ -f "$PATHFILE" ]; then
    if [ ! -s "$PATHFILE" ]; then
        echo "Path file exists but is empty. Recreating it..."
        rm "$PATHFILE"
    fi
fi

# Create the path file with content if it doesn't exist
if [ ! -f "$PATHFILE" ]; then
    # Define a default tools installation path
    TOOLSPATH="/home/kali/hackingtool"
    mkdir -p "$TOOLSPATH"
    echo "$TOOLSPATH" > "$PATHFILE"
    echo "Created path file at $PATHFILE with path: $TOOLSPATH"
fi

# Verify the file has content
if [ ! -s "$PATHFILE" ]; then
    echo "Warning: Path file is still empty after fix attempt. Setting default path."
    TOOLSPATH="/home/kali/hackingtool"
    mkdir -p "$TOOLSPATH"
    echo "$TOOLSPATH" > "$PATHFILE"
fi

# Display path info for debugging
echo "Using tools installation path: $(cat $PATHFILE)"

# Run the tool
python3 hackingtool.py 