import platform
import os
import psutil
import speedtest
import socket
import wmi
from win32api import GetSystemMetrics  # pywin32 important configurations

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_installed_software():
    installed_software = []
    for app in os.popen('wmic product get name').read().split('\n')[1:]:
        if app:
            installed_software.append(app.strip())
    return installed_software

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # in Mbps
    upload_speed = st.upload() / 10**6  # in Mbps
    return download_speed, upload_speed

#++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Fetching System Information...\n")

    print("Installed Software:")
    for software in get_installed_software():
        print(f"- {software}")

    download_speed, upload_speed = get_internet_speed()
    print(f"\nInternet Speed: Download {download_speed:.2f} Mbps, Upload {upload_speed:.2f} Mbps")

    print(f"\nScreen Resolution: {get_screen_resolution()}")

    cpu_info = get_cpu_info()
    print(f"\nCPU Model: {cpu_info['model']}")
    print(f"Number of Cores: {cpu_info['cores']}")
    print(f"Number of Threads: {cpu_info['threads']}")

    print(f"\nGPU Model: {get_gpu_info()}")

    print(f"\nRAM Size: {get_ram_size():.2f} GB")

    print(f"\nScreen Size: {get_screen_size()}")

    print(f"\nEthernet Mac Address: {get_mac_address('Ethernet')}")
    print(f"Wifi Mac Address: {get_mac_address('Wi-Fi')}")

    print(f"\nPublic IP Address: {get_public_ip()}")

    print(f"\nWindows Version: {get_windows_version()}")

