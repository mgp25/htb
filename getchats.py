import json
import requests
from parse import parse
import warnings
warnings.filterwarnings("ignore")
apikey = "MYAPIKEY"
def get_message():
	r = requests.post("https://www.hackthebox.eu/api/shouts/get/initial/html/100?api_token="+apikey)
	js = json.loads(r.content)
	html = js['html']
	global lastmsg
	lastmsg = html[99]
	for x in html:
		if 'https://www.hackthebox.eu/storage/avatars/' in x:
			parse(x)

def get_last_message():
	while True:
		r = requests.post("https://www.hackthebox.eu/api/shouts/get/initial/html/1?api_token="+apikey)
		js = json.loads(r.content)
		html = js['html'][0]
		if 'https://www.hackthebox.eu/storage/avatars/' in html:
			if html != lastmsg:
				parse(html)
				global lastmsg
				lastmsg = html
