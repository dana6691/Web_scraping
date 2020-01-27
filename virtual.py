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
# %%
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
name=a.find('div', attrs={'class':'_3wU53n'})
price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
products.append(name.text)
prices.append(price.text)
ratings.append(rating.text)
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
with urlopen('https://www.amazon.com/s?k=shrimp&ref=nb_sb_noss_2') as response:
    soup = BeautifulSoup(response, 'html.parser') #change html source into python object using html parser
    for anchor in soup.select('span.a-offscreen'):
        print(anchor.get_text())

# %%
