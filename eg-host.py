import socket
import os
import time
################
time.sleep (1)
os.system ("clear")
print ("")
print (" \033[0;32m\033[1;32m ___  __ _          | |__   ___  ___| |_")
print ("\033[0;32m\033[1;32m/  _ \/ _` |  _____  | '_ \ / _ \/ __| __|")
print ("\033[0;32m\033[1;32m|  __/ (_| | |_____| | | | | (_) \__ \ |_")
print (" \033[0;32m\033[1;32m\___|\__, |         |_| |_|\___/|___/\__|")
print ("      \033[0;32m\033[1;32m|___/")
print ("")
###############
def ip () :
	while True :
		time.sleep (0.350)
		hostname=input ("\033[0;33m\033[1;33mtarget is : ")
		ip=socket.gethostbyname(hostname)
		print ("")
		time.sleep(0.250)
		print ("\033[1;32mhostname is :" ,hostname)
		time.sleep(0.250)
		print ("\033[0;32m\033[1;32mip is :" ,ip ,"\033[0;37m")
		print ("")
		f = open("ip.txt","a")
		f.write("\nhostname is : " + hostname + "\nip is : " + ip)
		f.close()
def portscanner () :
	while True :
		host = input("\033[0;33m\033[1;33mplease enter the ip : ")
		for port in range(1,6553):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((host,port))
			if result == 0:
				print ("")
				print ("\033[1;31mthe open ports :")
				print("\033[0;32m\033[1;32m[{}]   open".format(port))
                        else :
                                print ("all ports is close")

def dns () :
	dns = input ("\033[0;33m\033[1;33mEnter dns : ")
	name = socket.getfqdn (dns)
	print ("")
	print ("\033[0;32m\033[1;32mresult :",name)
	print ("")
def main () :
    time.sleep(0.500)
    print ("")
    print ("\033[0;31m╔═════════════════════════════╗╔═════════════════════════════╗")
    print ("\033[0;31m║                             ║║                             ║")
    print ("\033[0;31m║    [\033[0;32m1\033[0;31m] \033[0;34mIp                   \033[0;31m║║   [\033[0;32m2\033[0;31m] \033[0;34mPortScanner           \033[0;31m║")
    print ("\033[0;31m║                             ║║                             ║")
    print ("\033[0;31m╚═════════════════════════════╝╚═════════════════════════════╝")
    print ("\033[0;31m╔═════════════════════════════╗╔═════════════════════════════╗")
    print ("\033[0;31m║                             ║║                             ║")
    print ("\033[0;31m║    [\033[0;32m3\033[0;31m] \033[0;34mDns                  \033[0;31m║║   [\033[0;32m4\033[0;31m] \033[0;34mAvailableSoOoN..!     \033[0;31m║")
    print ("\033[0;31m║                             ║║                             ║")
    print ("\033[0;31m╚═════════════════════════════╝╚═════════════════════════════╝")
    print ("")
    cho = int ((input ("\033[1;33menter your choose >> ")))
    if cho == 1 :
        os.system ("clear")
        time.sleep(0.500)
        ip ()
    elif cho == 2 :
        os.system("clear")
        time.sleep(0.500)
        portscanner ()
    elif cho == 3 :
        os.system("clear")
        time.sleep(0.500)
        dns ()
    else :
        print ("not found ..! ")
main ()
