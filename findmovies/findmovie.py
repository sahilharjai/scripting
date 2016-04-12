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
		print(item)
		visited[item]="true"
		req=requests.get(item)
		soup=BeautifulSoup(req.text)
		list1=soup.findAll('a')
		print(list1)

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
						
				
											
movies("http://www.imdb.com")
