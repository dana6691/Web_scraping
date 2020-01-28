#%%
###Beautifulsoup
## Save data in text file
from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://www.naver.com')
soup = BeautifulSoup(response,'html.parser')
i=1
f= open('this.txt','w',encoding="utf-8")
for anchor in soup.select('span'):
    data = str(i) + anchor.get_text() + "\n"
    i = i+1 
    f.write(data)
f.close()
#%%
## Image download 
## To save it: right click on downlods folder > Reveals in Explorer
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"shrimp, crab", "limit":20, "print_urls":True, "format":"png"}
paths = response.download(arguments) #passing arguments to the function
print(paths)
# %%
from scrapy import Selector
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com","https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass

# %%
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
#%%
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;uniq")
# %%
