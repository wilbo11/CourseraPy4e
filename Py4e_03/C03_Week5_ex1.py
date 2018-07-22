import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
if len(url) < 1:
    address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
count = 0
sm = 0

print('Retrieving', url)
urlh = urllib.request.urlopen(url)
data = urlh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
# print(lst)
# print('Amount of numbers:', len(lst))

for item in lst:
    no = item.find('count').text
    # print('no:', no)
    sm = sm + int(no)
    count = count + 1
print('Count:', count)
print('Sum:', sm)


