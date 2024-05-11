import subprocess
import re
from colorama import Fore, Style
import ipaddress

def print_banner():
    print("\nMade by")
    print(r"""
████████╗░░██╗██╗███╗░░██╗░██████╗░
╚══██╔══╝░██╔╝██║████╗░██║██╔════╝░
░░░██║░░░██╔╝░██║██╔██╗██║██║░░██╗░
░░░██║░░░███████║██║╚████║██║░░╚██╗
░░░██║░░░╚════██║██║░╚███║╚██████╔╝
░░░╚═╝░░░░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░
                        """)

def calculate_total_ips(ip_list):
    total_ips = 0
    for ip_range in ip_list:
        if '/' in ip_range: 
            total_ips += ipaddress.ip_network(ip_range, strict=False).num_addresses
        else:
            total_ips += 1
    return total_ips

def reverse_dns_scan(ip_list_file, output_filename):
    total_domains = 0  
    with open(ip_list_file, 'r') as ip_file:
        ip_list = ip_file.read().splitlines()
    with open(output_filename, 'w') as output_file:
        for ip_range in ip_list:
            count = 0
            print(f"Scanning {ip_range}...")
            process = subprocess.Popen(['nmap', '-sL', ip_range], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            if stderr:
                print(stderr)
                continue
            lines = stdout.split('\n')
            for line in lines:
                match = re.search(r'Nmap scan report for (.+) \((\d+\.\d+\.\d+\.\d+)\)', line)
                if match:
                    hostname = match.group(1)
                    ip = match.group(2)
                    output_file.write(f"{ip} - {hostname}\n")
                    count += 1
            total_domains += count 
            print(f" DONE: {ip_range} | Available Domains: {count}\n")

    return total_domains

if __name__ == "__main__":
    ip_list_file = "ip_list.txt" 
    output_filename = "hostnames.txt"
    print_banner()
    
    with open(ip_list_file, 'r') as ip_file:
        ip_list = ip_file.read().splitlines()
    total_ips = calculate_total_ips(ip_list)
    print(f"\nTotal IPs in the list of scope: {total_ips}\n")
    
    total_domains = reverse_dns_scan(ip_list_file, output_filename)
    print(f"\nScan done. Total {total_domains} domain found and saved to `{output_filename}` file.")
