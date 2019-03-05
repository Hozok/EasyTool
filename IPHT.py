#coding:utf-8
import os
import socket, threading
import time

def clsa():
	linux = 'clear'
	windows = 'cls'
	os.system([linux, windows][os.name == 'nt'])

clsa()
print("")
print("		###########################################")
print("				Easy Tool 0.1")
print("		###########################################")
print("")

def gen():
	print("")
	print("		[1] --> IP of a Host Checker")
	print("") 
	print("			----------")
	print("")
gen()
cmd = input("		(*) Choose your cmd require : ")

print("			Your choice is been update.")
if cmd == "1":
	hostaddress = input("		(*) Write the Host TARGET : ")
	ipaddress = socket.gethostbyname(hostaddress)
	print("			-- Scanning the host . --")
	time.sleep(0.5)
	print("			-- Scanning the host .. --")
	time.sleep(0.5)
	print("			-- Scanning the host ... --")
	time.sleep(0.5)
	
	print("")
	print("		[*] TARGET --> " +hostaddress)
	print("")
	print("		[*] IP of the TARGET --> " +ipaddress)

elif cmd == "quit":
	quit()
else:
	print("			CMD inconnue.")
	quit()

