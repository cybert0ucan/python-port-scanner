#Idea: write a containerized port scanner that uses a different IP than the host (IP Spoofing)
#Idea: check for filtered ports
#Idea: Multi threaded socket programming
#Idea: NMAP
#Based on open ports, auto-suggest suitable nmap scripts
#Support for calling nmap thru the tool?

import socket
import re

ip_pattern1 = re.compile("^\d{1,3}(?:\.\d{1,3}){3}$") #single IP
ip_pattern2 = re.compile("^\d{1,3}(?:\.\d{1,3}){3}(?:\,\d{1,3}(?:\.\d{1,3}){3})*$") #comma separated IP
ip_pattern3 = re.compile("^\d{1,3}(?:\.\d{1,3}){3}-\d{1,3}$") #IP range 192.168.0.1-120
ip_pattern4 = re.compile("^\d{1,3}(?:\.\d{1,3}){3}\/\d{1,2}$") #IP subnet

port_pattern1 = re.compile("^\d{1,5}$") #single port
port_pattern2 = re.compile("^\d{1,5}(?:\,\d{1,5})*$") #comma separated ports
port_pattern3 = re.compile("^\d{1,5}-\d{1,5}$") #port range

min_port = 1
max_port = 65535

#IP Address format validation
tries = 3
while (tries > 0):
    ip_addr = []
    get_ip = input("Enter the target IP address: ")
    valid_ip = True
    if ip_pattern1.search(get_ip):
        ip_addr.append(get_ip)
    #elifs for other patterns come here
    for i in ip_addr:
        oct = i.split('.')
        for j in oct:
            if not((int(j) >= 0) and (int(j) <= 266)):
                valid_ip = False
                break
        if (valid_ip==False):
            if (tries==1):
                exit()
            break
    if (valid_ip==True):
        break
    tries -= 1

#Port format validation
tries = 3
while (tries > 0):
    ports = []
    get_port = input("Enter the port(s) or port range [eg: 22 or 22,80 or 22-1337]: ")
    valid_port = True
    if port_pattern1.search(get_port):
        ports.append(int(get_port))
    elif port_pattern2.search(get_port):
        ports = [int(i) for i in get_port.split(',')]
    elif port_pattern3.search(get_port):
        minP = int(get_port.split('-')[0])
        maxP = int(get_port.split('-')[1])
        ports = [i for i in range (minP, maxP+1)]
    for i in ports:
        if (i >= min_port) and (i <= max_port):
            continue
        else:
            valid_port = False
            break
    if valid_port==True:
        break
    tries -= 1

#Socket scanning
for i in ip_addr:
    print (f"Scanning {i}:")
    for p in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s. settimeout(0.5)
            s.connect((i, p))
            print (f"{p} is open")
        except:
            print (f"{p} is closed/filtered")





