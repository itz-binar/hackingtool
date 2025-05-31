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

# Create the path file if it doesn't exist
PATHFILE=~/hackingtoolpath.txt
if [ ! -f "$PATHFILE" ] || [ ! -s "$PATHFILE" ]; then
    # Define a default tools installation path
    TOOLSPATH="/home/kali/hackingtool"
    echo "$TOOLSPATH" > "$PATHFILE"
    echo "Created path file at $PATHFILE with default path: $TOOLSPATH"
fi

# Run the tool
python3 hackingtool.py 