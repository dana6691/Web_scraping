<!-- Table of Contents -->
## Table of Contents
* BeautifulSoup
   * Image scraping: scrape famous movie posters of each year from 2015 - 2019
   * Yahoo finance: scrape multiple pages of stock data and save on csv file
   * Naver stock: scrape stock data (1-50)
   * Shopping List(Ebay,Coupang): scrape multiple pages of laptop data with conditions
* Scrapy
   * Basic: functions in Scrapy
* Selenium
   * Basic: click, submit, page go back, go forward, refresh, and login using Selenium
   * Flight_ticket: google flight, set destination and date of departure and returning, grab flights information
   * Google_movie: list of google movie, display only discounted Movie, scroll the page to see all movies
   * Pagination.py: scrap multiple pages of data and save data into xlsx file
* Project
   * Sublink_scraping.py: fetch all href links and save the collected data from sublinks into xlsx file  
   * Paginated_scraping.py: scraping multiple pages data using while loop
   * Google_image.py: using google_image_download library
   * Newsheadline_Weather: bring up-to-date news headlines and weather information
   * RealEstate: location, size,and price of the houses in Minneapolis
   * Search List: find a list of trending search words in naver.com

<!-- Web scraping vs Web crawling -->
## Web scraping vs Web crawling
 Web scraping  | Web crawling 
 :---:  | :---:
 Extracting data from any source | Extracting data from websites<br>in an automated manner. 
 Any scale  | Large scale  |
 Directly fetches the specific data and store it| Collecting as much information as possible 
Apift SDK, Scrapy, BeautifulSoup|


<!-- WEb SCRAPING STEP -->
## Web Scraping Procedure
1. **Request** the data through HTTP server, when we are requesting HTTP METHOD should be selected
   1. GET: everyone can see, using url
      * GET is after '?', all the parameters are seperated with '&'
      * ex) https://www.coupand.com/np/search?minPrice=1000&maxPrice=1000000&page=1
   1. POST: conceived under the body
1. **Parsing HTML**
1. **Download Data**
The final part is where you download and save the data in a CSV, JSON or in a database so that it can be retrieved and used manually or employed in any other program.

```python
# requests for fetching html of website
import requests

# Make the GET request to a url
r = requests.get('http://www.cleveland.com/metro/index.ssf/2017/12/case_western_reserve_university_president_barbara_snyders_base_salary_and_bonus_pay_tops_among_private_colleges_in_ohio.html')

# Make the GET request to a url
r =  urllib.request.urlopen('http://localhost:8082/v3/nodes', data=query)

# Extract the content
c = r.content
from bs4 import BeautifulSoup
# Create a soup object
soup = BeautifulSoup(c)
```

<!-- LIBRARY -->
## Python Libraries Used
* requests: retrieving content from a webpage(Get requests)
* BeautifulSoup
* Scrapy
* Selenium
* google_images_download
* re: regular expression operations





