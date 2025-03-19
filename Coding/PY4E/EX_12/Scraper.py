from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
Σ=0
n=0
tags = soup('span')
for tag in tags:
    n+=1
    Σ+=int(tag.contents[0])
print(f"There are {n} results with a sum total of {Σ} for a mean of {Σ/n}")
