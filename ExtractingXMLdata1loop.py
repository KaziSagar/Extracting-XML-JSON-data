import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
if len(url) < 1:
    print('Invalid input')
    quit()

data = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
sum = 0
for i in lst:
    sum = sum + int(i.find('count').text)
print('Sum =',sum)
