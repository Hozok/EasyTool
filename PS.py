import os
import socket, threading
import time

print("")
print("		###########################################")
print("				Easy Tool 0.1")
print("		###########################################")
print("")

host = input("			=> Enter an IP for PortScanner : ")
if host == "/quit":
	quit() 

ip = socket.gethostbyname(host)
threads = []
open_ports = {}

def try_port(ip, port, delay, open_ports):

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.settimeout(delay)
	result = sock.connect_ex((ip, port))

# Simple condition : 

	if result == 0:
		open_ports[port] = 'open'
		return True
	else:
		open_ports[port] = 'false'
		return None

# On va effectué plusieurs boucle for dans la fonction 'scan_ports' : 

def scan_ports(ip, delay):

	for port in range(0, 1023): 
		thread = threading.Thread(target=try_port, args=(ip, port, delay, open_ports))
		threads.append(thread)

	for i in range(0, 1023):
		threads[i].start()

	for i in range(0, 1023):
		threads[i].join()

	for i in range(0, 1023):
		if open_ports[i] == 'open':
			print("")
			print(' 	--> [#] Voici les ports OPEN : ' + str(i))
		if i == 1022:
			print("")
			print(' 	--> [*] Scanning Complete !')

if __name__ == "__main__":
	scan_ports(ip, 3) # 3 est donc le délais.

"""
Ce qui est utile à savoir :

Ports les plus connus :

	Port 80 : Pour le HTTP,
	Port 21 : Pour le FTP,
	Port 443 : Pour le HTTPS,
	Port 22 : Pour le SSH,
	Port 110 : Pour le service POP.

"""
