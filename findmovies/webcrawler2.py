import requests
k=requests.get("http://www.imdb.com/chart/top?ref_=ft_250")
from bs4 import BeautifulSoup
j=k.text
soup=BeautifulSoup(j)
tag2=soup.tbody
l=[]
m=[]
k=0;
i=1
while(1):
	if(i>500):
		break
	t={}
	t=tag2.contents[i].contents[3].a.text
	k=tag2.contents[i].contents[5].strong.text
	l.append(t)
	m.append(k)
	i=i+2
print(l)
print(m)
import csv

csvfile = open('webcrawler2.csv', 'w',newline='')
csvwriter = csv.writer(csvfile)
for item in range(len(l)):
	u='name'+'='+l[item]+' '+'rating'+'='+m[item]
	csvwriter.writerow(u)
csvfile.close()