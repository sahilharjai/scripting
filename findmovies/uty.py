import requests
import os
from bs4 import BeautifulSoup
from queue import *
from urllib.parse import urljoin
visited={}
queue =[]

def movies(url):
	visited[url]="true"
	queue.append(url)
	k=1
	y=0
	

	while(len(queue)!=0):
		if y==200:
			break


		item=queue.pop(0)



		visited[item]="true"
		req=requests.get(item)

		soup=BeautifulSoup(req.text)
		list1=soup.findAll('a')
		
		for i in list1:
			link=i.get('href')
			if y==200:
				break
			
			
			if link==None:
				continue
			else:
				if link.split("//")[0]!="htpps:" or link.split("//")[0]!="http:":
					link=urljoin(url,link)
					if link not in visited:
						k=k+1
						queue.append(link)

				re=requests.get(link)
				soup1=BeautifulSoup(re.text)
				mymovies=soup1.findAll('td',class_="titleColumn")
				
				for l in mymovies:
					if y==200:
						break
					if l!=[]:
						lin=l.find('a')
						
						
						
						
movies("http://www.imdb.com")
print(visited)


















for li in mycontent:
					if li!=[]:
						if y==200:
							break
						name=mycontent.find('td',class_="titleColumn").get_text()
						print(name)
						print("@@@@@@@@@")
						rate=mycontent.find('td',class_="ratingColumn").strong.get_text()
						mydict[name]=rate
						y=y+1





















































import requests
import os
from bs4 import BeautifulSoup
from queue import *
from urllib.parse import urljoin
visited={}
queue =[]

def movies(url):
	visited[url]="true"
	queue.append(url)
	y=0
	while(len(queue)!=0):
		if y==200:
			break
		item=queue.pop(0)
		visited[item]="true"
		req=requests.get(item)
		soup=BeautifulSoup(req.text)
		list1=soup.findAll('a')
		for i in list1:
			link=i.get('href')
			if y==200:
				break
			if link==None:
				continue
			else:
				if link.split("//")[0]!="htpps:" or link.split("//")[0]!="http:":
					link=urljoin(url,link)
					if link not in visited:
						queue.append(link)

				re=requests.get(link)
				soup1=BeautifulSoup(re.text)
				mymovies=soup1.findAll("td",{"class":"titleColumn"})
				for w in mymovies:
					df=w.find('a')['href']
					df=url+df
					print(df)
					sd=requests.get(df)
					rating=sd.find("span",{"itemprop":"ratingValue"})
					if rating==None:
						continue
					else:
						print(rating)
						y=y+1
				
											
movies("http://www.imdb.com")

