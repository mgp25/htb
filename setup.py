#!/usr/bin/python
from os import geteuid, system
from getpass import getpass
import requests
import json
try:
	from bs4 import BeautifulSoup
except:
	system("pip install bs4")
	from bs4 import BeautifulSoup
#made by r4j1337
if geteuid() != 0:
    exit("You need to have root privileges to run this script.")

print "\033[96m[+] \033[92mMade By r4j1337"
print "\033[96m[+] \033[92mtwitter: https://twitter.com/r4j1337"
print "\033[96m[+] \033[92mhtb: https://www.hackthebox.eu/home/users/profile/13243"
print ""
session = requests.Session()
response = session.get('https://www.hackthebox.eu/login')
cookie = session.cookies.get_dict()
html = BeautifulSoup(response.content, 'lxml')
token = html.body.find('input', attrs={'type':'hidden'})['value']
email = raw_input("Email: ")
password = getpass("password: ")
session2 = requests.Session()
response2 = session2.post('https://www.hackthebox.eu/login', data={"_token":token, "email":email, "password":password, "remember":"on"}, cookies=cookie)
cookie2 = session2.cookies.get_dict()
if 'hackthebox.eu/home' not in response2.content:
	exit("[+] Enter a valid email and password!")
file = open("cookies.txt","w") 
file.write(json.dumps(cookie2))
file.close() 
file = open("cookies.txt","r")
cont = file.read()
f = json.loads(cont)
r = requests.get("https://hackthebox.eu/home/hof", cookies=f)
content = r.content
num = content.find("api_token=")
api_key = content[num+10:num+70]
print "\033[96m[+] \033[92mDownloading HTB vpn"
vpd = requests.get('https://www.hackthebox.eu/home/htb/access/ovpnfile', cookies=f)
ovpn = open('htb.ovpn', 'w')
ovpn.write(vpd.content)
ovpn.close()
print "\033[96m[+] \033[92mDownloaded"
textsearch = "MYAPIKEY"
with open('getchats.py', 'r') as file :
  filedata = file.read()

filedata = filedata.replace(textsearch, api_key)
with open('getchats.py', 'w') as file:
  file.write(filedata)
system('pip install netifaces')
system('chmod +x htb.py')
system("apt -y install openvpn")
system('ln -s `pwd`/htb.py /usr/bin/htb')
print "\033[96m[+] \033[92mSetup Successful"
print "\033[96m[+] \033[92mType htb on your terminal"
