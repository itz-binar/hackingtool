# HackingTool Configuration Guide

This guide explains how to configure and fix common issues with the HackingTool collection to ensure all tools work correctly, especially on newer systems with externally managed Python environments.

## Common Issues Fixed

1. **Externally Managed Environment Errors**: Many tools fail with "externally-managed-environment" errors on newer systems like Kali Linux.
2. **Path Issues**: Some tools have hardcoded paths or don't handle directory changes correctly.
3. **Inconsistent Use of pip/pip3**: Different tools use different pip commands.
4. **Missing Dependencies**: Some tools fail due to missing system dependencies.
5. **Outdated GitHub Repositories**: Some tools reference repositories that have moved or been deleted.
6. **Indentation Errors**: Some tools have inconsistent indentation or other code issues.

## Configuration Scripts

We've created several scripts to help fix these issues:

1. **tool_config_helper.py**: Main configuration script that sets up the environment.
2. **fix_tool.py**: Script to fix a specific tool.
3. **fix_all_tools.py**: Script to fix all tools in the collection.
4. **pip_wrapper.sh**: Wrapper script for pip commands to use virtual environments.
5. **run_tool.sh**: Script to run tools with their virtual environments.

## Setup Instructions

### Step 1: Run the Configuration Helper

This will install necessary system dependencies, create helper scripts, and set up virtual environment support:

```bash
python3 tools/tool_config_helper.py
```

### Step 2: Fix All Tools

This will apply fixes to all tools in the collection:

```bash
python3 tools/fix_all_tools.py
```

### Step 3: Run Tools

To run a specific tool with its virtual environment:

```bash
./run_tool.sh <tool_name> <command>
```

For example:

```bash
./run_tool.sh ddos python3 ddos.py
```

## Manual Tool Fixes

If you need to fix a specific tool manually:

```bash
python3 tools/fix_tool.py <tool_name>
```

## Specific Tool Patches

Some tools required special patches:

1. **UFONet**: Fixed cgi module issue with a patch script.
2. **Saphyra**: Fixed indentation issues with a patch script.
3. **SlowLoris**: Fixed module import issues and added proper virtual environment support.

## Troubleshooting

If you encounter issues with a specific tool:

1. Check if the tool has a virtual environment in the `venvs` directory.
2. Try running the tool manually with its virtual environment:
   ```bash
   cd <tool_directory>
   source ../venvs/<tool_name>/bin/activate
   python <tool_script.py>
   ```
3. Check for specific error messages and fix accordingly.

## System Requirements

- Python 3.6 or higher
- python3-venv package installed
- Git

## Additional Notes

- Some tools may require additional system packages. Install them as needed.
- If a tool still doesn't work after applying these fixes, try checking its GitHub repository for updates or issues.
- For tools that require GUI access, make sure you have the necessary X11 libraries installed. 