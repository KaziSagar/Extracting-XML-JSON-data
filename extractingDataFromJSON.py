#Sample: http://py4e-data.dr-chuck.net/comments_42.json
#Actual: http://py4e-data.dr-chuck.net/comments_649381.json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
data = urllib.request.urlopen(url, context=ctx).read()

info = json.loads(data)

sum = 0
for item in info["comments"]:
	number = int(item["count"])
	sum = sum + number
print('Sum =',sum)
