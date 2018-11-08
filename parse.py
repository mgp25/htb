from bs4 import BeautifulSoup
import os
import platform
import HTMLParser
import re
html_parser = HTMLParser.HTMLParser()

def parse(html):
	#print html
	parsed_html = BeautifulSoup(html, "lxml")
	try:
		time = parsed_html.body.find('span', attrs={'class':'text-warning'}).text
		try:
			rank = parsed_html.body.find('span', attrs={'class':''}).text
			rank = "\033[97m"+rank
		except:
			rank = "\033[91m[Admin]"
		name = parsed_html.body.find('a').text
		num = html.find("</span></span>")
		num = num+15
		msg = html[num:]
		msg = html_parser.unescape(msg[:-4])
		print("\033[96m"+time, "\033[92m"+name, rank, ":\033[94m"+msg)
	except:
		time = parsed_html.text[0:14]
		msg = parsed_html.text[15:]

		if ("requested a reset" in msg):
			matchObj = re.match( r'\w+ (\w+) \w+ \w+ reset on (\w+) .* (\d+)', msg, re.M|re.I)
			notify("Reset requested on"+matchObj.group(2), "Type /cancel "+matchObj.group(3)+"to cancel")
		print("\033[93m"+time, "\033[96m"+msg)

def notify(title, text):
	if (platform.system() == "Darwin"):
	    os.system("""
	              osascript -e 'display notification "{}" with title "{}"' 2>/dev/null
	              """.format(text, title))
	elif (platform.system() == "Linux"):
		os.system("""notify-send '{}' '{}'""".format(text, title))
