##pip list : check list
## Create virtual environment (on windows): py -m virtualenv folder_env
## pip uninstall virtualenv
## pip install virtualenv
## virtualenv
#from selenium import webdriver
#%%
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.naver.com/') as response:
    soup = BeautifulSoup(response, 'html.parser') #change html source into python object using html parser
    for anchor in soup.find_all('a'):
        print(anchor.get_text())
#%%
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('C:/Users/daheekim/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.naver.com/')
#content = driver.find_element_by_class_name('ah_list')

# click radio button
#python_button = driver.find_elements_by_xpath("//input[@class='ah_roll_area'")[0]
driver.find_element_by_class_name("ah_roll_area").Click();
WebElement expanded = driver.findElement(By.xpath(".//*[@id='ui-accordion-f-accordion-header-2']/span"));
expanded.click();

# %%
#Click and expand the information and extract
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome('C:/Users/daheekim/Downloads/chromedriver_win32/chromedriver.exe')
driver.implicitly_wait(3)
driver.get('https://www.naver.com/')
roll = driver.find_element_by_xpath("//li[@class='ah_item']").click()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
for anchor in soup.findAll('span', class_=['ah_k', 'ah_r']):
    print(anchor.get_text())
# %%
# Naver 페이 들어가기
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())
#%%
#parsing price and price comparison
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver = webdriver.Chrome('C:/Users/daheekim/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("https://www.amazon.com/s?k=shrimp&ref=nb_sb_noss_2")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('span.a-offscreen')
for n in notices:
    print(n.text.strip())

#%%
from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://www.amazon.com/s?k=shrimp&ref=nb_sb_noss_2') as response:
    soup = BeautifulSoup(response, 'html.parser') #change html source into python object using html parser
    for anchor in soup.find_all(['span.a-offscreen','span.a-size-base-plus a-color-base a-text-normal']):
        print(anchor.get_text())
# %%
from bs4 import BeautifulSoup
from urllib.request import urlopen
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
with urlopen('https://www.amazon.com/s?k=shrimp&ref=nb_sb_noss_2') as response:
    soup = BeautifulSoup(response, 'html.parser') #change html source into python object using html parser
    for anchor in soup.find_all('span.a-offscreen'):
        print(anchor.get_text())
# %%       
    for a in soup.findAll('div',attrs={'class':'s-result-list s-search-results sg-row'}):
        #name= a.find('span', attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        #print(name)
        price= a.find('span', attrs={'class':'a-offscreen'})
        print(price)
    #rating=a.find('span', attrs={'aria-label'})
        #products.append(name.text)
        #prices.append(price.text)
    #ratings.append(rating.text)
#print(prices)

# %%
df = pd.DataFrame({'Product Name':products,'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')
print(df)

#%%
import scrapy
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass

inspect_class(YourSpider)# Inspect Your Class

# %%
import requests
from bs4 import BeautifulSoup
import os

driver = webdriver.Chrome('C:/Users/daheekim/Downloads/chromedriver_win32/chromedriver.exe')

req = requests.get('http://clien.net/cs2/bbs/board.php?bo_table=sold')
req.encoding = 'utf-8' # Clien에서 encoding 정보를 보내주지 않아 encoding옵션을 추가해줘야합니다.

html = req.text
soup = BeautifulSoup(html, 'html.parser')
posts = soup.select('td.post_subject')
latest = posts[1].text # 0번은 회원중고장터 규칙입니다.

with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f:
    f.write(latest)