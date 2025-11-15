#!/usr/bin/env python3

import socket
import subprocess

def run_cmd(cmd):
    """Komut çıktısını alır ve hem döndürür hem yazdırır"""
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.DEVNULL)
        text = output.decode()
        print(text)
        return text
    except subprocess.CalledProcessError:
        return ""

def scanall():
    print("""
	    ...   ::::::::::::   ...      .::::::. ::::::.    :::.::::::::::::
 .;;;;;;;.;;;;;;;;''''.;;;;;;;.  ;;;`    ` ;;;`;;;;,  `;;;;;;;;;;;''''
,[[     \\[[,   [[    ,[[     \\[[,'[==/[[[[,[[[  [[[[[. '[[     [[
$$$,     $$$   $$    $$$,     $$$  '''    $$$$  $$$ "Y$c$$     $$
"888,_ _,88P   88,   "888,_ _,88P 88b    dP888  888    Y88     88,
  "YMMMMMP"    MMM     "YMMMMMP"   "YMmMY" MMM  MMM     YM     MMM
	
	T-H-E--V-0-1-D--H-A-C-K--T-E-A-M
	
	""")
    
    target = input("Enter Target Domain: ")
    filename = f"{target}_osint.txt"
    
    try:
        ip = socket.gethostbyname(target)
        print(f"\n[+] IP --> {ip}")
    except socket.gaierror:
        print(f"[-] {target} cannot resolve")
        return
    
    all_output = f"[+] IP --> {ip}\n\n"

    # IPInfo
    all_output += "------IPINFO------\n"
    ipinfo = run_cmd(f"curl -s https://ipinfo.io/{ip}/json")
    all_output += ipinfo + "\n"

    # WHOIS
    all_output += "\n------WHOIS------\n"
    whois_out = run_cmd(f"whois {ip}")
    all_output += whois_out + "\n"

    # DNS
    all_output += "\n------DNS------\n"
    ns_target = run_cmd(f"nslookup {target}")
    ns_ip = run_cmd(f"nslookup {ip}")
    dig_ip = run_cmd(f"dig {ip}")
    all_output += ns_target + "\n" + ns_ip + "\n" + dig_ip + "\n"

    # Reverse DNS
    all_output += "\n------REV DNS------\n"
    revdns = run_cmd(f"curl -s https://api.hackertarget.com/reversedns/?q={ip}")
    all_output += revdns + "\n"

    # Subdomains
    all_output += "\n------SUBFINDER------\n"
    subd = run_cmd(f"curl -s https://api.hackertarget.com/hostsearch/?q={target}")
    all_output += subd + "\n"

    # TXT dosyaya kaydet
    with open(filename, "w") as f:
        f.write(all_output)

    print(f"\n[+] Tüm bilgiler {filename} dosyasına kaydedildi.")

scanall()