import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

import urllib.request



#url = 'http://py4e-data.dr-chuck.net/known_by_Jorja.html'
url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
with urllib.request.urlopen("http://py4e-data.dr-chuck.net/known_by_Fikret.html") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s)

soup = BeautifulSoup(s,"s.parser")
href = soup('a')
#print href

for i in range(count):
    
    link = href[position].get('href', None)
    print (href[position].contents[0])
    soup = BeautifulSoup(html,"html.parser")
    href = soup('a')
    