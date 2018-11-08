#!/usr/bin/python
from os import system, getcwd
from getpass import getpass
import platform
import requests
import json

#Original author: r4j1337

try:
	from bs4 import BeautifulSoup
except:
	system("pip install bs4")
	from bs4 import BeautifulSoup

HACKTHEBOX_LOGIN_URL = "https://www.hackthebox.eu/login"


session = requests.Session()
response = session.get(HACKTHEBOX_LOGIN_URL)
cookie = session.cookies.get_dict()
html = BeautifulSoup(response.content, 'lxml')
token = html.body.find('input', attrs={'type':'hidden'})['value']

## USER DATA
email = input("Email: ")
password = getpass("password: ")
##

session2 = requests.Session()
data = {"_token":token,"email":email,"password":password,"remember":"on"}

response2 = session2.post(HACKTHEBOX_LOGIN_URL, data, cookies=cookie)
cookie2 = session2.cookies.get_dict()

if "hackthebox.eu/home" not in str(response2.content, 'utf-8'):
	exit("[+] Enter a valid email and password!")

file = open("cookies.dat","w")
file.write(json.dumps(cookie2))
file.close()
file = open("cookies.dat","r")
cont = file.read()
f = json.loads(cont)
r = requests.get("https://hackthebox.eu/home/hof", cookies=f)
content = str(r.content, 'utf-8')
num = content.find("api_token=")
api_key = content[num+10:num+70]
api_key_file = open("API_KEY.dat", "w")
api_key_file.write(api_key)
api_key_file.close()

print ("\033[96m[+] \033[92mDownloading HTB vpn")
vpd = requests.get('https://www.hackthebox.eu/home/htb/access/ovpnfile', cookies=f)
ovpn = open('htb.ovpn', 'w')
ovpn.write(str(vpd.content, 'utf-8'))
ovpn.close()
print ("\033[96m[+] \033[92mDownloaded")

system('python -m pip install netifaces')
system('python -m pip install htmlparser')
system('chmod +x htb.py')
if (platform.system() == "Linux"):
	system("sudo apt -y install openvpn")
elif(platform.system() == "Darwin"):
	system("brew install openvpn")
print("\033[96m[+] \033[92mSetup Successful")
print("\033[96m[+] \033[92mType htb on your terminal")
