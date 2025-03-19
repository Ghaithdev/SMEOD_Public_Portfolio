import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    url = address
    url_handle = urllib.request.urlopen(url, context=ctx)

    data = url_handle.read()
    print('Retrieved', len(data), 'characters')
    info = json.loads(data)
    print('User count:', len(info))
    run_total=0
    for item in info['comments']:
        run_total+=int(item['count'])
    print(run_total)
    finish=input("Done? (Y/N)\n>").capitalize()
    if finish == "Y":
        break
print("thank you")