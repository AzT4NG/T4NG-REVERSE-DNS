import subprocess
import re
from tqdm import tqdm
from colorama import Fore, Style

def print_banner():
    print(r"""

████████╗░░██╗██╗███╗░░██╗░██████╗░
╚══██╔══╝░██╔╝██║████╗░██║██╔════╝░
░░░██║░░░██╔╝░██║██╔██╗██║██║░░██╗░
░░░██║░░░███████║██║╚████║██║░░╚██╗
░░░██║░░░╚════██║██║░╚███║╚██████╔╝
░░░╚═╝░░░░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░
                        """)
#Use this code only if you have the necessary permission for pentests!
#made by T4NG

def reverse_dns_scan(ip_list_file, output_filename):
    with open(ip_list_file, 'r') as ip_file:
        ip_list = ip_file.read().splitlines()
    with open(output_filename, 'w') as output_file:
        with tqdm(total=len(ip_list), desc="Scanning:", bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)) as pbar:
            count = 0
            for ip_range in ip_list:
                process = subprocess.Popen(['nmap', '-sL', ip_range], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                if stderr:
                    print(stderr.decode())
                    continue
                lines = stdout.decode().split('\n')
                for line in lines:
                    match = re.search(r'Nmap scan report for (.+) \((\d+\.\d+\.\d+\.\d+)\)', line)
                    if match:
                        hostname = match.group(1)
                        ip = match.group(2)
                        output_file.write(f"{count + 1}. {hostname} - {ip}\n")
                        count += 1
                pbar.update(1)
                pbar.set_postfix_str(f"Scanned: {count}/{len(ip_list)}")

if __name__ == "__main__":
    ip_list_file = "ip_list.txt" 
    output_filename = "hostnames.txt"
    print_banner()
    print("Script made by T4NG")
    print("Reverse DNS Starting...")
    print("It is working, don`t quit! The process can take 2-5 minute per ip/24 scope. Don`t look at 0% :)")
    reverse_dns_scan(ip_list_file, output_filename)
    print("Scan done. Results in 'hostnames.txt' file")
    print("\nHave a nice day ;)")

