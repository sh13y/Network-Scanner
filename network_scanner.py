import socket
from ipaddress import ip_address, ip_network
from colorama import Fore, Style, Back, init

# Initialize colorama
init(autoreset=True)

# ASCII Logo
logo = r"""
  _   _ _____ _______        _____  ____  _  __
 | \ | | ____|_   _\ \      / / _ \|  _ \| |/ /
 |  \| |  _|   | |  \ \ /\ / / | | | |_) | ' / 
 | |\  | |___  | |   \ V  V /| |_| |  _ <| . \ 
 |_|_\_|_____| |_|    \_/\_/_ \___/|_|_\_\_|\_\
 / ___| / ___|  / \  | \ | | \ | | ____|  _ \  
 \___ \| |     / _ \ |  \| |  \| |  _| | |_) | 
  ___) | |___ / ___ \| |\  | |\  | |___|  _ <  
 |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\ 
"""

version = "Version 1.0"
author = "by sh13y"

def is_host_active(ip, port=80):
    """
    Checks if a host is active by trying to connect to the specified port.
    
    Args:
        ip (str): IP address or hostname to check.
        port (int): Port number to connect to (default is 80).
        
    Returns:
        bool: True if the host is active, False otherwise.
    """
    try:
        with socket.create_connection((ip, port), timeout=2):
            return True
    except:
        return False

def scan_from_file(filename, port=80):
    """
    Scans a list of IPs/hosts from a file to check if they are active.
    
    Args:
        filename (str): Path to the file containing IPs/hosts.
        port (int): Port number to connect to.
    """
    try:
        with open(filename, "r") as file:
            hosts = file.read().splitlines()
        
        print(f"Scanning {len(hosts)} hosts from file...")
        for host in hosts:
            if is_host_active(host, port):
                print(f"[ACTIVE] {host} is up.")
            else:
                print(f"[INACTIVE] {host} is down.")
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def scan_ip_range(start_ip, end_ip, port=80):
    """
    Scans a range of IPs to check if they are active.
    
    Args:
        start_ip (str): Starting IP address of the range.
        end_ip (str): Ending IP address of the range.
        port (int): Port number to connect to.
    """
    try:
        start = ip_address(start_ip)
        end = ip_address(end_ip)
        print(f"Scanning IP range {start} to {end}...")
        
        current_ip = start
        while current_ip <= end:
            if is_host_active(str(current_ip), port):
                print(f"[ACTIVE] {current_ip} is up.")
            else:
                print(f"[INACTIVE] {current_ip} is down.")
            current_ip += 1
    except ValueError as e:
        print(f"Invalid IP address: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print(Fore.CYAN + Style.BRIGHT + logo)
    print(Fore.YELLOW + Style.BRIGHT + f"\n{version}")
    print(Fore.YELLOW + Style.BRIGHT + f"{author}\n")
    
    print(Fore.BLUE + Style.BRIGHT + "[ MENU OPTIONS ]")
    print(Fore.BLUE + "╔═════════════════════════════╗")
    print(Fore.BLUE + "║ 1. Scan IPs/hosts from file ║")
    print(Fore.BLUE + "║ 2. Scan a range of IPs      ║")
    print(Fore.BLUE + "╚═════════════════════════════╝\n")

    choice = input(Fore.GREEN + Style.BRIGHT + "[+] " + Fore.WHITE + "Enter your choice (1 or 2): ")
    print()
    
    port = input(Fore.GREEN + Style.BRIGHT + "[+] " + Fore.WHITE + "Enter the port to check (default is 80): ") or 80
    print()

    if choice == "1":
        filename = input(Fore.GREEN + Style.BRIGHT + "[+] " + Fore.WHITE + "Enter the file path: ")
        print(Fore.CYAN + "\n[*] Starting file scan...\n")
        scan_from_file(filename, port)
    elif choice == "2":
        start_ip = input(Fore.GREEN + Style.BRIGHT + "[+] " + Fore.WHITE + "Enter the starting IP: ")
        end_ip = input(Fore.GREEN + Style.BRIGHT + "[+] " + Fore.WHITE + "Enter the ending IP: ")
        print(Fore.CYAN + "\n[*] Starting range scan...\n")
        scan_ip_range(start_ip, end_ip, port)
    else:
        print(Fore.RED + Style.BRIGHT + "\n[!] Invalid choice. Exiting.") 