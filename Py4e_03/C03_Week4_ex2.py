# Following multiple links from a web-page.
# Position is the number of the link it will 'click on',
# Count is how many times it will go through this process.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
pos1 = input('Enter count: ')
pos2 = input('Enter position: ')
print('Retrieving:', url)  # stupid requirement of course assessment :(
big_count = 0
new_url = None
adds = []

while big_count < int(pos1):
    if new_url is None:
        new_url = url
    html = urllib.request.urlopen(new_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = 0
    tags = soup('a')
    for tag in tags:
        line = tag.get('href', None)
        count = count + 1
        if count == int(pos2):
            new_url = line
            break
        else:
            continue
    print('Retrieving:', line)
    big_count = big_count + 1
