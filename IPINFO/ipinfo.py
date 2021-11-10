import requests
import bs4
import argparse

parser = argparse.ArgumentParser(description='Get IP')
parser.add_argument('-ip','--ipaddress',type=str)
args = parser.parse_args()


WHOIS_URL = 'https://whois.com'

def findIPInfo(ip):
	COMPLETE_URL = WHOIS_URL + "/whois/{}".format(ip)
	response = requests.get(COMPLETE_URL) 
	soup = bs4.BeautifulSoup(response.text,'html.parser')
	html_element = soup.find('pre')

	if html_element:
		print(html_element.text)
	else:
		print(None)

def makeRequest(url):
	with requests.get(url) as wurl:
		if wurl.status_code == 200:
			print(wurl)
			findIPInfo(args.ipaddress)
		else:
			print("Can't connect to {}".format(url))

makeRequest(WHOIS_URL)
