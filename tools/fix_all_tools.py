#!/usr/bin/env python3
"""
Fix All Tools Script
This script applies fixes to all tools in the hacking tools collection
"""

import os
import sys
import subprocess
import glob
from pathlib import Path

# Colors for terminal output
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_banner():
    """Print script banner"""
    banner = f"""
    {BLUE}╔═══════════════════════════════════════════════╗
    ║            Fix All Hacking Tools                 ║
    ╚═══════════════════════════════════════════════╝{RESET}
    """
    print(banner)

def get_tool_directories():
    """Get all tool directories"""
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(tools_dir)
    
    # Find all Python files in the tools directory
    python_files = glob.glob(os.path.join(tools_dir, "*.py"))
    
    # Extract tool names from Python files
    tool_names = []
    for file_path in python_files:
        if os.path.basename(file_path) not in ["__init__.py", "tool_config_helper.py", "fix_all_tools.py", "fix_tool.py"]:
            tool_name = os.path.splitext(os.path.basename(file_path))[0]
            tool_names.append(tool_name)
    
    # Add the 'others' directory
    others_dir = os.path.join(tools_dir, "others")
    if os.path.isdir(others_dir):
        for file_path in glob.glob(os.path.join(others_dir, "*.py")):
            if os.path.basename(file_path) != "__init__.py":
                tool_name = os.path.splitext(os.path.basename(file_path))[0]
                tool_names.append(f"others/{tool_name}")
    
    return tool_names

def fix_pip_commands(file_path):
    """Fix pip commands in a file to use virtual environments"""
    print(f"{BLUE}[*] Fixing pip commands in {file_path}...{RESET}")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace pip/pip3 install commands
    content = content.replace("pip install", "../pip_wrapper.sh install")
    content = content.replace("pip3 install", "../pip_wrapper.sh install")
    content = content.replace("sudo pip install", "../pip_wrapper.sh install")
    content = content.replace("sudo pip3 install", "../pip_wrapper.sh install")
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"{GREEN}[✓] Fixed pip commands in {file_path}{RESET}")

def fix_python_commands(file_path):
    """Fix python commands in a file to use virtual environments"""
    print(f"{BLUE}[*] Fixing python commands in {file_path}...{RESET}")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace direct python/python3 calls with the runner script
    content = content.replace("python ", "../run_tool.sh python ")
    content = content.replace("python3 ", "../run_tool.sh python3 ")
    content = content.replace("sudo python ", "../run_tool.sh python ")
    content = content.replace("sudo python3 ", "../run_tool.sh python3 ")
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"{GREEN}[✓] Fixed python commands in {file_path}{RESET}")

def fix_git_clone_commands(file_path):
    """Fix git clone commands to check if directory exists first"""
    print(f"{BLUE}[*] Fixing git clone commands in {file_path}...{RESET}")
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find all git clone commands
    import re
    git_clone_pattern = r'(sudo\s+)?git\s+clone\s+(https?://[^\s]+|git@[^\s]+)'
    matches = re.findall(git_clone_pattern, content)
    
    for match in matches:
        sudo_prefix = match[0]
        repo_url = match[1]
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        
        # Create a conditional clone command
        old_command = f"{sudo_prefix}git clone {repo_url}"
        new_command = f"if [ ! -d '{repo_name}' ]; then {sudo_prefix}git clone {repo_url}; else echo '{repo_name} directory already exists'; fi"
        
        content = content.replace(old_command, new_command)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"{GREEN}[✓] Fixed git clone commands in {file_path}{RESET}")

def fix_tool(tool_name):
    """Apply fixes to a specific tool"""
    print(f"{BLUE}[*] Fixing tool: {tool_name}{RESET}")
    
    # Get the tool's Python file
    if '/' in tool_name:
        # Handle tools in subdirectories
        tool_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), tool_name + ".py")
    else:
        tool_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), tool_name + ".py")
    
    if not os.path.exists(tool_file):
        print(f"{RED}[✗] Tool file not found: {tool_file}{RESET}")
        return False
    
    # Apply fixes
    fix_pip_commands(tool_file)
    fix_python_commands(tool_file)
    fix_git_clone_commands(tool_file)
    
    # Create a virtual environment for the tool
    try:
        subprocess.run(["python3", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fix_tool.py"), tool_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"{RED}[✗] Failed to create virtual environment for {tool_name}: {str(e)}{RESET}")
    
    print(f"{GREEN}[✓] Fixed tool: {tool_name}{RESET}")
    return True

def main():
    print_banner()
    
    # Check if the configuration helper has been run
    config_helper = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tool_config_helper.py")
    fix_tool_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fix_tool.py")
    
    if not os.path.exists(fix_tool_script):
        print(f"{YELLOW}[!] Please run the configuration helper first:{RESET}")
        print(f"    python3 {config_helper}")
        sys.exit(1)
    
    # Get all tool directories
    tool_names = get_tool_directories()
    print(f"{BLUE}[*] Found {len(tool_names)} tools to fix{RESET}")
    
    # Fix each tool
    fixed_count = 0
    for tool_name in tool_names:
        if fix_tool(tool_name):
            fixed_count += 1
    
    print(f"\n{GREEN}[✓] Fixed {fixed_count}/{len(tool_names)} tools{RESET}")
    print(f"\n{YELLOW}[!] To run a tool with its virtual environment, use:{RESET}")
    print(f"    ./run_tool.sh <tool_name> <command>")

if __name__ == "__main__":
    main() 