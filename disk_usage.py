# this script is set to check the disk usage of a given directory 
#this script also alert if the usage exceeds a specified percentage

import os
import shutil

def check_disk_usage(directory, threshold):
    total, used, free = shutil.disk_usage(directory)
    usage_percentage = (used / total) * 100
    print(f"Disk usage: {usage_percentage:.2f}%")

    if usage_percentage > threshold:
        print(f"Alert: Disk usage exceeds {threshold}%")

check_disk_usage("/", 80)
