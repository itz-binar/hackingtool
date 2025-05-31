#!/usr/bin/env python3
"""
Saphyra-DDoS Patch Script
This script fixes indentation issues in the Saphyra-DDoS tool by converting
all indentation to spaces to maintain consistency.
"""

import os
import sys
import re
import shutil
from pathlib import Path

def backup_file(file_path):
    """Create a backup of the original file"""
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)
    print(f"Created backup: {backup_path}")
    return backup_path

def fix_indentation(file_path):
    """Fix indentation by converting tabs to spaces"""
    print(f"Fixing indentation in {file_path}...")
    
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # First, let's normalize line endings
    content = content.replace('\r\n', '\n')
    
    # Split into lines for processing
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Count leading tabs and spaces
        leading_tabs = len(line) - len(line.lstrip('\t'))
        
        # Replace tabs with 4 spaces
        if leading_tabs > 0:
            fixed_line = ' ' * (4 * leading_tabs) + line.lstrip('\t')
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)
    
    # Join lines back together
    fixed_content = '\n'.join(fixed_lines)
    
    # Write the fixed content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"Fixed indentation in {file_path}")

def main():
    saphyra_dir = Path(os.path.expanduser("~/hackingtool/Saphyra-DDoS"))
    if not saphyra_dir.exists():
        print(f"Saphyra-DDoS directory not found at: {saphyra_dir}")
        return 1
    
    saphyra_file = saphyra_dir / "saphyra.py"
    if not saphyra_file.exists():
        print(f"Saphyra-DDoS main file not found at: {saphyra_file}")
        return 1
    
    try:
        backup_path = backup_file(saphyra_file)
        fix_indentation(saphyra_file)
        print(f"Saphyra-DDoS patched successfully!")
        print(f"Original file backed up to: {backup_path}")
    except Exception as e:
        print(f"Error patching Saphyra-DDoS: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 