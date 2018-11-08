import os
import json
import requests
from parse import parse
import warnings
warnings.filterwarnings("ignore")

if (os.path.isfile("API_KEY.dat") == False):
	print("\033[91m[+] Run setup.py\033[91m")
else:
	try:
		file = open("API_KEY.dat", "r")
		apikey = file.read()
		file.close()
	except Exception as e:
		print("\033[91m[+] \033[92mError reading API_KEY.dat")
def get_message():
	r = requests.post("https://www.hackthebox.eu/api/shouts/get/initial/html/100?api_token="+apikey)
	js = json.loads(str(r.content, 'utf-8'))
	html = js['html']
	global lastmsg
	lastmsg = html[99]
	for x in html:
		if 'https://www.hackthebox.eu/storage/avatars/' in x:
			parse(x)

quite = True
def get_last_message(quite):
	try:
		while True:
			r = requests.post("https://www.hackthebox.eu/api/shouts/get/initial/html/1?api_token="+apikey)
			js = json.loads(str(r.content, 'utf-8'))
			html = js['html'][0]
			if quite == True:
				if 'https://www.hackthebox.eu/storage/avatars/' in html:
					if html != lastmsg:
						parse(html)
						global lastmsg
						lastmsg = html
			else:
				if html != lastmsg:
					parse(html)
					global lastmsg
					lastmsg = html
	except:
		print("")
