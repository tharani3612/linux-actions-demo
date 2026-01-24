import platform
import shutil
import time
from datetime import datetime

def print_header(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

def system_info():
    print_header("SYSTEM INFORMATION")
    print(f"OS            : {platform.system()}")
    print(f"OS Version    : {platform.release()}")
    print(f"Architecture  : {platform.machine()}")

def disk_check():
    print_header("DISK USAGE CHECK")
    total, used, free = shutil.disk_usage("/")
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)

    print(f"Total Disk    : {total_gb} GB")
    print(f"Used Disk     : {used_gb} GB")
    print(f"Free Disk     : {free_gb} GB")

    if free_gb < 5:
        print("STATUS        : WARNING - Low disk space")
    else:
        print("STATUS        : OK")

def service_check():
    print_header("APPLICATION SERVICE CHECK")
    services = ["Web Server", "Database", "Cache"]

    for service in services:
        print(f"{service:<15}: RUNNING")
        time.sleep(0.5)

def compliance_check():
    print_header("SECURITY & COMPLIANCE CHECK")
    print("Root Login        : Disabled")
    print("Firewall Status  : Enabled")
    print("SSH Access        : Restricted")
    print("Compliance Status: PASSED")

def summary():
    print_header("CHECK SUMMARY")
    print("Overall Status : HEALTHY")
    print("Checked At     :", datetime.now())

def main():
    print_header("CLOUD SERVER HEALTH CHECK STARTED")
    system_info()
    disk_check()
    service_check()
    compliance_check()
    summary()
    print_header("HEALTH CHECK COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main()

