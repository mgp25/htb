#!/usr/bin/python
from os import geteuid, system
from getpass import getpass
#made by r4j1337
if geteuid() != 0:
    exit("You need to have root privileges to run this script.")

print "[+] Made By r4j1337"
print "[+] twitter: https://twitter.com/r4j1337"
print "[+] htb: https://www.hackthebox.eu/home/users/profile/13243"

a = getpass("Enter Your Hackthebox Api Key > ")
b = raw_input("Enter Your HTB vpn location(if there) > ")
textsearch = "MYAPIKEY"
with open('getchats.py', 'r') as file :
  filedata = file.read()

filedata = filedata.replace(textsearch, a)
with open('getchats.py', 'w') as file:
  file.write(filedata)
if b != "":
	textsearch = "MYVPNFILE"
	with open('htb.py', 'r') as file :
  		filedata = file.read()
	filedata = filedata.replace(textsearch, b)
	with open('htb.py', 'w') as file:
  		file.write(filedata)
system("pip install bs4")
system('chmod +x htb.py')
system("apt -y install openvpn")
system('ln -s `pwd`/htb.py /usr/bin/htb')
print "[+] Setup Successful"
print "[+] Type htb on your terminal"
