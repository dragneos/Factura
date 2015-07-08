#-*- encoding: utf -*-
import urllib.request
import re
urls =["http://www.animeid.tv/"]
regex = '<title>(.+?)</title>'
regex2 = '<figure>(.+?)</figure>'
regex3 = '<header>(.+?)</header>'

pattern = re.compile(regex2)
pattern2 = re.compile(regex3)

htmlfile = urllib.request.urlopen(urls[0])
htmltext = htmlfile.read()
htmltext = str(htmltext)

figure = re.findall(pattern,htmltext)
header = re.findall(pattern2,htmltext)

print (htmltext)
print("")
print (figure)
print(len(figure))
print (header)
print(len(header))


l = [0,1,2,3,4,5,6,7,8,9]
for x in l:
    print(figure[x])
    print(header[x])
