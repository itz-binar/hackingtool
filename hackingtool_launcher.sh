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

# Run the tool
python3 hackingtool.py 