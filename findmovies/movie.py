import requests
import os
from bs4 import BeautifulSoup
from queue import *
from urllib.parse import urljoin
visited={}
queue=[]
def movies(url):
	queue.append(url)
	while(len(queue)!=0):
		item=queue.pop(0)
		if item in visited:
			continue
		visited[item]=True
		link=requests.get(item)
		soup=BeautifulSoup(link.text)
		list1=soup.findAll('a')
		for i in list1:
			if i==None:
				continue	
			href=i.get('href')
			if href==None:
				continue
			if href.split("//")[0]!="htpps:" or href.split("//")[0]!="http:":
				href="http://www.imdb.com"+href
			for e in href:
				ij=request.

		v=soup.find_all("div",{"class":"rec_item"})
		print(v)
		for m in v:
			if(m.a!=None):
				if(item.a['href']!=None):
					queue.append(m.a['href'])
		rating=soup.find("span",{"itemprop":"ratingValue"})
		if(rating==None):
			continue
		print(rating)
movies("http://www.imdb.com")
