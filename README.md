# T4NG-REVERSE-DNS
This python code using to find domains in given mass ip ranges via nmap. You can use it without any difficulty.

<h5>Made by T4NG! v1-2024/5 xploit</h5>
<hr>

First of all download Python:


- sudo apt update

- sudo apt install python3

- sudo pip3 install -r requirements.txt

</br>

Make sure your kali is up to date and has NMAP tool:


- sudo apt update
- sudo apt upgrade -y

- sudo apt install nmap


<hr>

How to use: 
<br>

Fill all your ips to file of :  *ip_list.txt* 

<br>

Example:

<br>

10.10.10.0/24

10.11.11.0/24

10.12.12.0/24

...


</br>
<b>There should be no spaces in the text file!</b>

<hr>

Command: 

<br>

- <b>(root㉿kali)-[/home/user/reverse_dns]:</b> <i>python reverse_dns_scan_t4ng.py</i>

<br>

The result may take a while.
Scan results will be written to "hostnames.txt" file.

Make sure you delete or change the name of <i>"hostname.txt"</i> file before running a new scan.

<hr>

Use this code only if you have the necessary permission for pentests!
Don`t be evil mate :)



