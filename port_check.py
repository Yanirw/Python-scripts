# this script takes a list of IP addresses as input and checks if the specified ports are open

import socket
from concurrent.futures import ThreadPoolExecutor

def check_port(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")

def check_ports(ip_addresses, ports):
    with ThreadPoolExecutor() as executor:
        for ip in ip_addresses:
            for port in ports:
                executor.submit(check_port, ip, port)

ip_addresses = ["192.168.1.1", "192.168.0.100"]
ports = [8080, 443, 22]
check_ports(ip_addresses, ports)
