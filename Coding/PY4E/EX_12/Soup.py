from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('Enter URL:\n>')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


tags = soup('td')
for tag in tags:
    print(tag.get('href', None))
