#!/usr/bin/env python3
"""
UFONet Patch Script for Python 3.11+ Compatibility
This script patches the UFONet source code to replace deprecated cgi module
with the newer urllib.parse module.
"""

import os
import re
import sys
import shutil
from pathlib import Path

def backup_file(file_path):
    """Create a backup of the original file"""
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)
    print(f"Created backup: {backup_path}")

def patch_cgi_module(file_path):
    """Replace cgi module imports and usages with urllib.parse"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace import statements
    content = re.sub(
        r'import\s+io,\s+socket,\s+ssl,\s+cgi,\s+json,\s+gzip', 
        'import io, socket, ssl, json, gzip\nfrom urllib.parse import parse_qs', 
        content
    )
    
    # Replace cgi.parse_qs with urllib.parse.parse_qs
    content = content.replace('cgi.parse_qs', 'parse_qs')
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"Patched: {file_path}")

def main():
    # Try multiple possible locations for the UFONet directory
    possible_paths = [
        Path(os.path.expanduser("~/hackingtool/ufonet")),
        Path("/home/kali/hackingtool/ufonet"),
        Path(os.getcwd()) / "ufonet",
        Path(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ufonet"))
    ]
    
    ufonet_dir = None
    for path in possible_paths:
        if path.exists():
            ufonet_dir = path
            print(f"Found UFONet directory at: {ufonet_dir}")
            break
    
    if not ufonet_dir:
        print("UFONet directory not found. Tried these locations:")
        for path in possible_paths:
            print(f"  - {path}")
        return 1
    
    main_file = ufonet_dir / "core" / "main.py"
    if not main_file.exists():
        print(f"UFONet main.py not found at: {main_file}")
        return 1
    
    try:
        backup_file(main_file)
        patch_cgi_module(main_file)
        print("UFONet patched successfully for Python 3.11+ compatibility")
        print("You can now try running UFONet again")
    except Exception as e:
        print(f"Error patching UFONet: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 