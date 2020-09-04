#####################################################################
# image scraping
#####################################################################
# movie poster 
# best 2 movies of the year
# year from 2015 to 2019
# save file in jpg
# we cannot save image right away, get into other link to save pic
#####################################################################
import requests
from bs4 import BeautifulSoup
import re
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

for year in range(2015,2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url, headers= headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    images = soup.find_all("img",attrs={"class":"thumb_img"})
    for index, image in enumerate(images):
        image_url = image["src"]
        if index >1:
            break
        if image_url.startswith("//"):
            image_url = "https:"+ image_url  
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open("/Users/daheekim/Desktop/VisualStudio/Web-scraping-crawling-/downloads/movies{}_{}.jpg".format(year,index+1),"wb") as f:
            f.write(image_res.content)