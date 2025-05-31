#!/usr/bin/env python3
"""
HackingTool Configuration Helper
This script helps fix common issues with the hacking tools collection
"""

import os
import sys
import subprocess
import re
import shutil
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
    ║         HackingTool Configuration Helper         ║
    ╚═══════════════════════════════════════════════╝{RESET}
    """
    print(banner)

def check_python_version():
    """Check Python version"""
    print(f"{BLUE}[*] Checking Python version...{RESET}")
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 6:
        print(f"{GREEN}[✓] Python version {python_version.major}.{python_version.minor} is compatible{RESET}")
        return True
    else:
        print(f"{RED}[✗] Python version {python_version.major}.{python_version.minor} is not compatible. Please use Python 3.6+{RESET}")
        return False

def check_pip_environment():
    """Check if pip is using an externally managed environment"""
    print(f"{BLUE}[*] Checking pip environment...{RESET}")
    try:
        result = subprocess.run(["pip3", "install", "--user", "virtualenv"], 
                               stdout=subprocess.PIPE, 
                               stderr=subprocess.PIPE, 
                               text=True, 
                               check=False)
        
        if "externally-managed-environment" in result.stderr:
            print(f"{YELLOW}[!] Pip is using an externally managed environment{RESET}")
            print(f"{YELLOW}[!] Will use virtual environments for tool installations{RESET}")
            return False
        else:
            print(f"{GREEN}[✓] Pip environment is standard{RESET}")
            return True
    except Exception as e:
        print(f"{RED}[✗] Error checking pip environment: {str(e)}{RESET}")
        return False

def setup_venv_directory():
    """Create a directory for virtual environments"""
    print(f"{BLUE}[*] Setting up virtual environment directory...{RESET}")
    venv_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "venvs")
    os.makedirs(venv_dir, exist_ok=True)
    print(f"{GREEN}[✓] Virtual environment directory created at: {venv_dir}{RESET}")
    return venv_dir

def patch_tools_with_venv():
    """Patch the core.py file to support virtual environments"""
    print(f"{BLUE}[*] Patching core.py to support virtual environments...{RESET}")
    core_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core.py")
    
    if not os.path.exists(core_path):
        print(f"{RED}[✗] core.py not found at: {core_path}{RESET}")
        return False
    
    # Backup the original file
    backup_path = f"{core_path}.bak"
    shutil.copy2(core_path, backup_path)
    print(f"{GREEN}[✓] Created backup of core.py at: {backup_path}{RESET}")
    
    with open(core_path, 'r') as f:
        content = f.read()
    
    # Add venv support to the HackingTool class
    if "def run_command" in content and "venv_activate" not in content:
        # Add venv_path attribute to HackingTool class
        content = content.replace(
            "class HackingTool(object):",
            "class HackingTool(object):\n    venv_path = None"
        )
        
        # Modify the run_command method to activate venv if available
        content = content.replace(
            "def run_command(self, command):",
            """def run_command(self, command):
        # If venv_path is set, activate it before running the command
        if self.venv_path and os.path.exists(self.venv_path):
            activate_script = os.path.join(self.venv_path, "bin", "activate")
            if os.path.exists(activate_script):
                command = f"source {activate_script} && {command}"
        """
        )
        
        # Write the modified content back to the file
        with open(core_path, 'w') as f:
            f.write(content)
        
        print(f"{GREEN}[✓] Successfully patched core.py with venv support{RESET}")
        return True
    else:
        print(f"{YELLOW}[!] core.py already patched or has unexpected structure{RESET}")
        return False

def create_tool_fix_script():
    """Create a script to fix common issues with individual tools"""
    print(f"{BLUE}[*] Creating tool fix script...{RESET}")
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fix_tool.py")
    
    script_content = """#!/usr/bin/env python3
import os
import sys
import subprocess
import argparse
import re
from pathlib import Path

# Colors for terminal output
GREEN = '\\033[92m'
YELLOW = '\\033[93m'
RED = '\\033[91m'
BLUE = '\\033[94m'
RESET = '\\033[0m'

def fix_tool(tool_name):
    """Fix common issues with a specific tool"""
    print(f"{BLUE}[*] Fixing tool: {tool_name}{RESET}")
    
    # Get the tool's directory
    tool_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), tool_name)
    if not os.path.exists(tool_dir):
        print(f"{RED}[✗] Tool directory not found: {tool_dir}{RESET}")
        return False
    
    # Create a virtual environment for the tool
    venv_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "venvs", tool_name)
    os.makedirs(os.path.dirname(venv_dir), exist_ok=True)
    
    if not os.path.exists(venv_dir):
        print(f"{BLUE}[*] Creating virtual environment for {tool_name}...{RESET}")
        try:
            subprocess.run(["python3", "-m", "venv", venv_dir], check=True)
            print(f"{GREEN}[✓] Created virtual environment at: {venv_dir}{RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{RED}[✗] Failed to create virtual environment: {str(e)}{RESET}")
            return False
    
    # Install requirements if available
    req_file = os.path.join(tool_dir, "requirements.txt")
    if os.path.exists(req_file):
        print(f"{BLUE}[*] Installing requirements for {tool_name}...{RESET}")
        try:
            pip_path = os.path.join(venv_dir, "bin", "pip")
            subprocess.run([pip_path, "install", "-r", req_file], check=True)
            print(f"{GREEN}[✓] Installed requirements for {tool_name}{RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{RED}[✗] Failed to install requirements: {str(e)}{RESET}")
    
    # Check if the tool has a setup.py file
    setup_file = os.path.join(tool_dir, "setup.py")
    if os.path.exists(setup_file):
        print(f"{BLUE}[*] Installing {tool_name} in development mode...{RESET}")
        try:
            python_path = os.path.join(venv_dir, "bin", "python")
            subprocess.run([python_path, "setup.py", "develop"], cwd=tool_dir, check=True)
            print(f"{GREEN}[✓] Installed {tool_name} in development mode{RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{RED}[✗] Failed to install in development mode: {str(e)}{RESET}")
    
    print(f"{GREEN}[✓] Fixed tool: {tool_name}{RESET}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Fix common issues with a specific tool")
    parser.add_argument("tool_name", help="Name of the tool to fix")
    args = parser.parse_args()
    
    fix_tool(args.tool_name)

if __name__ == "__main__":
    main()
"""
    
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    os.chmod(script_path, 0o755)
    print(f"{GREEN}[✓] Created tool fix script at: {script_path}{RESET}")
    return script_path

def create_pip_wrapper():
    """Create a wrapper script for pip to handle externally managed environments"""
    print(f"{BLUE}[*] Creating pip wrapper script...{RESET}")
    script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pip_wrapper.sh")
    
    script_content = """#!/bin/bash
# Wrapper script for pip to handle externally managed environments

# Colors
GREEN='\\033[0;32m'
YELLOW='\\033[0;33m'
RED='\\033[0;31m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

# Get the tool name from the current directory
TOOL_NAME=$(basename $(pwd))
VENV_DIR="$(dirname $(dirname $(realpath $0)))/venvs/$TOOL_NAME"

# Check if virtual environment exists, create if not
if [ ! -d "$VENV_DIR" ]; then
    echo -e "${BLUE}[*] Creating virtual environment for $TOOL_NAME...${NC}"
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo -e "${RED}[✗] Failed to create virtual environment${NC}"
        exit 1
    fi
    echo -e "${GREEN}[✓] Created virtual environment at: $VENV_DIR${NC}"
fi

# Activate the virtual environment and run pip
source "$VENV_DIR/bin/activate"
pip "$@"
"""
    
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    os.chmod(script_path, 0o755)
    print(f"{GREEN}[✓] Created pip wrapper script at: {script_path}{RESET}")
    return script_path

def create_tool_runner():
    """Create a runner script for tools that handles virtual environments"""
    print(f"{BLUE}[*] Creating tool runner script...{RESET}")
    script_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "run_tool.sh")
    
    script_content = """#!/bin/bash
# Runner script for tools that handles virtual environments

# Colors
GREEN='\\033[0;32m'
YELLOW='\\033[0;33m'
RED='\\033[0;31m'
BLUE='\\033[0;34m'
NC='\\033[0m' # No Color

if [ $# -lt 2 ]; then
    echo -e "${RED}Usage: $0 <tool_name> <command>${NC}"
    exit 1
fi

TOOL_NAME="$1"
shift
COMMAND="$@"

VENV_DIR="$(dirname $(realpath $0))/venvs/$TOOL_NAME"
TOOL_DIR="$(dirname $(realpath $0))/$TOOL_NAME"

# Check if virtual environment exists
if [ -d "$VENV_DIR" ]; then
    echo -e "${BLUE}[*] Using virtual environment for $TOOL_NAME...${NC}"
    source "$VENV_DIR/bin/activate"
    cd "$TOOL_DIR"
    eval "$COMMAND"
    deactivate
else
    echo -e "${YELLOW}[!] No virtual environment found for $TOOL_NAME, running directly...${NC}"
    cd "$TOOL_DIR"
    eval "$COMMAND"
fi
"""
    
    with open(script_path, 'w') as f:
        f.write(script_content)
    
    os.chmod(script_path, 0o755)
    print(f"{GREEN}[✓] Created tool runner script at: {script_path}{RESET}")
    return script_path

def install_system_dependencies():
    """Install common system dependencies needed by most tools"""
    print(f"{BLUE}[*] Installing common system dependencies...{RESET}")
    dependencies = [
        "python3-venv",
        "python3-dev",
        "build-essential",
        "libssl-dev",
        "libffi-dev",
        "python3-setuptools",
        "python3-wheel",
        "git"
    ]
    
    try:
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y"] + dependencies, check=True)
        print(f"{GREEN}[✓] Installed system dependencies{RESET}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{RED}[✗] Failed to install system dependencies: {str(e)}{RESET}")
        return False

def main():
    print_banner()
    
    if not check_python_version():
        sys.exit(1)
    
    standard_pip = check_pip_environment()
    
    # Install system dependencies
    install_system_dependencies()
    
    # Setup virtual environment directory
    venv_dir = setup_venv_directory()
    
    # Patch core.py to support virtual environments
    patch_tools_with_venv()
    
    # Create helper scripts
    create_tool_fix_script()
    create_pip_wrapper()
    create_tool_runner()
    
    print(f"\n{GREEN}[✓] Configuration complete!{RESET}")
    print(f"\n{YELLOW}[!] To fix a specific tool, run:{RESET}")
    print(f"    python3 tools/fix_tool.py <tool_name>")
    print(f"\n{YELLOW}[!] To run a tool with its virtual environment, use:{RESET}")
    print(f"    ./run_tool.sh <tool_name> <command>")

if __name__ == "__main__":
    main() 