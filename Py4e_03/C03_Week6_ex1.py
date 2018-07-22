import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API

url = input('Enter location:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_104229.json'
print('Retrieving', url)
urlh = urllib.request.urlopen(url)
data = urlh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

# print(json.dumps(js, indent=2))

x = 0
count = 0

for item in js['comments']:
    x = x + int(item['count'])
    count = count + 1
print('Count:', count)
print('Sum:', x)
