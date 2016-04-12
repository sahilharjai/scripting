import os
import sys
import requests
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import cssutils
def css_download(url):
	domain=url.split("//")[-1].split(".")[1]
	req=requests.get(url)
	soup=BeautifulSoup(req.text)
	css_list=set()
	css_file=soup.findAll('link')
	for link in css_file:
		src=link.get('href')
		if src.split("?")[0].split(".")[-1]=='css':
			css_list.add(src)
	for list1 in css_list:
		try:
			re=requests.get(list1)
		except:
			continue
		soup1=BeautifulSoup(re.text)
		tr=soup1.find_all(string=re.compile("background"))
		print(tr)



		
      



def download(url):
	domain=url.split("//")[-1].split(".")[1]
	os.makedirs(domain)
	req=requests.get(url)
	if req.status_code!=200:
		return
	soup=BeautifulSoup(req.text)
	img_src=set()
	img_list=soup.findAll('img')
	for link in img_list:

		src=link.get('src')
		if not src:
			continue
		if src[:7]=='https://' or src[:6]=='http://':
			img_src.add(src)
		else:
			img_src.add(urljoin(url,src))
	i=0
	for url_path in img_src:
		try:
			re=requests.get(url_path)
		except:
			continue
		i=i+1
		filename=str(i)+"."+url_path.split(".")[-1]
		f=open(domain+'/'+filename,"wb")
		f.write(re.content)
		f.close()
download("http://www.google.co.in")
