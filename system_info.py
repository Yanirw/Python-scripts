# This script retrieves some system information 

import platform
import psutil

def generate_system_report():
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")

generate_system_report()
