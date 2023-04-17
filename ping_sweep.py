# This script performs a ping sweep on a range of IP addresses to check if the hosts are up or down.

import os
import platform
import subprocess

def ping_sweep(ip_range):
    for ip in ip_range:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = ["ping", param, "1", ip]
        response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if response == 0:
            print(f"{ip} is up")
        else:
            print(f"{ip} is down")

ip_range = [f"192.168.1.{i}" for i in range(1, 255)]
ping_sweep(ip_range)
