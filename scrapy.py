######################################################
#extract(): extract all lists
#extract_first(): first element of the list
######################################################
from scrapy import Selector
ps = sel.xpath('//p')
second_p = ps[1]
second_p.extract()
#%%
#Example of extract()
from scrapy import Selector
html = '''
<html>
<body>
<div class="hello datacamp">
<p>Hello World!</p>
</div>
<p>Enjoy DataCamp!</p>
</body>
</html>
'''
sel = Selector( text = html )
sel.css("div > p")
sel.css("div > p").extract()
#%%
##Same 
sel.xpath('/html/body/div[2]') 
#= sel.xpath('/html').xpath('./body/div[2]') 
#= sel.xpath('/html').xpath('./body').xpath('./div[2]')
#%%
sel = Selector( text=html ) #all html
divs = sel.xpath( '//div' ) #all div
divs[2].xpath('./*') # select all the children of the third div element.
#%%
from scrapy import Selector
import requests
# Create the string html containing the HTML source
html = requests.get( url ).content
sel = Selector( text=html )
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )
#%%
##CSS Locator
#XPath: /html/body/div
#CSS locator: html > body > div
''' 1)'/' replaced with '>"
    2)'//' replaced with blank space
    3)'[N]' replaced by :nth-of-type(N)
        #//div/p[2]
        #div > p:nth-of-type(2)
    4)Find class, use .
        #p.class-1
    5)Find by id, use #
        #div#uid
    6)element/@attr_name by element::attr(attr_name)
        xpath = '//div[@id="uid"]/a/@href'
        css_locator = 'div#uid > a::attr(href)'
    7)wildcard: '*.class-1', '*#uid' ,'#uid >*'
    8)/text(), //text():even future generation into ::text or space ::text 
'''
css_locator ='div#uid > p.class1' #Select paragraph elements within class class1
css_locator = '.class1' #all elements whose class attribute belongs to class1
xpath ='//*[@class="class1"]' #Only 'class1'
xpath ='//*[contains(@class, "class1")]' #Any class contains 'class1'

xpath = '/html/body/span[1]//a'
css_locator = 'html > body > span:nth-of-type(1) a'
xpath = '//div[@id="uid"]/span//h4'
css_locator = 'div#uid > span h4'
xpath ='//div[@id="uid"]/a/@href'
css_locator ='div#uid > a::attr(href)'
#%%
##selecting all href
from scrapy import Selector
sel = Selector( text=html )
course_as = sel.css( 'div.course-block > a' )
# css
hrefs_from_css = course_as.css( '::attr(href)' )
# xpath
hrefs_from_xpath = course_as.xpath( './@href' )
#%%
##example of text
xpath = '//p[@id="p3"]/text()'
css_locator = 'p#p3::text'
print_results( xpath, css_locator )

xpath = '//p[@id="p3"]//text()'
css_locator = 'p#p3 ::text'
print_results( xpath, css_locator )
#%%
##Use Response for xpath
this_url = response.url
# Get the title of the website loaded in response
this_title = response.xpath( '/html/head/title/text()' ).extract_first()
print_url_title( this_url, this_title )

##Use Response for css
css_locator = 'a.course-block__link'
response_as = response.css( css_locator )
sel_as = sel.css( css_locator )
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
  print( "Element %d from response: %s" % (i+1, response_as[i]) )
  print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
  print( "" )
  
##Extract first
divs = response.css('div.course-block')
first_div = divs[0]# Take the first div element
h4_text = first_div.css('h4::text').extract_first()
print( "The text from the h4 element is:", h4_text )

## Create a SelectorList of the course titles
crs_title_els = response.css( 'h4::text' ) 
crs_titles = crs_title_els.extract()# Extract the course titles
for el in crs_titles:
  print( ">>", el )# Print out the course titles 

## Calculate the number of children of the mystery element
how_many_kids = len( mystery.xpath( './*' ) )
print( "The number of elements you selected was:", how_many_kids )

#%%
######################################################
##Inheriting Spider
######################################################
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
######################################################
##Hurl the URLs
######################################################
import scrapy
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
inspect_class( YourSpider )# Inspect Your Class


import scrapy
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    self.print_msg( "Hello World!" )
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
inspect_class( YourSpider )# Inspect Your Class

#%%
import scrapy
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = "https://www.datacamp.com", callback = self.parse )
  # parse method
  def parse( self, response ):
    pass
inspect_class( YourSpider )# Inspect Your Class
#%%

import scrapy
class DCspider( scrapy.Spider ):
  name = 'dcspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  # parse method
  def parse( self, response ):
    # Create an extracted list of course author names
    author_names=response.css('p.course-block__author-name::text').extract()
    return author_names
inspect_spider( DCspider )# Inspect the spider
#%%
import scrapy
class DCdescr( scrapy.Spider ):
  name = 'dcdescr'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request( url = url_short, callback = self.parse )
  
  # First parse method
  def parse( self, response ):
    links = response.css( 'div.course-block > a::attr(href)' ).extract()
    # Follow each of the extracted links
    for link in links:
      yield response.follow( url = link, callback = self.parse_descr )
      
  # Second parsing method
  def parse_descr( self, response ):
    # Extract course description
    course_descr = response.css( 'p.course__description::text' ).extract_first()
    # For now, just yield the course description
    yield course_descr
inspect_spider( DCdescr )# Inspect the spider
#%%
##Capstone
import scrapy
from scrapy.crawler import CrawlerProcess
# Create the Spider class
class DC_Chapter_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    crs_title_ext = crs_title.extract_first().strip()
    ch_titles = response.css('h4.chapter__title::text')
    ch_titles_ext = [t.strip() for t in ch_titles.extract()]
    dc_dict[ crs_title_ext ] = ch_titles_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()

previewCourses(dc_dict)# Print a preview of courses
#%%

# %%
##DataCamp Description
# Import scrapy
import scrapy

# Import the CrawlerProcess: for running the spider
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class DC_Description_Spider(scrapy.Spider):
  name = "dc_chapter_spider"
  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url = url_short,
                         callback = self.parse_front)
  # First parsing method
  def parse_front(self, response):
    course_blocks = response.css('div.course-block')
    course_links = course_blocks.xpath('./a/@href')
    links_to_follow = course_links.extract()
    for url in links_to_follow:
      yield response.follow(url = url,
                            callback = self.parse_pages)
  # Second parsing method
  def parse_pages(self, response):
    # Create a SelectorList of the course titles text
    crs_title = response.xpath('//h1[contains(@class,"title")]/text()')
    # Extract the text and strip it clean
    crs_title_ext = crs_title.extract_first().strip()
    # Create a SelectorList of course descriptions text
    crs_descr = response.css( 'p.course__description::text' )
    # Extract the text and strip it clean
    crs_descr_ext = crs_descr.extract_first().strip()
    # Fill in the dictionary
    dc_dict[crs_title_ext] = crs_descr_ext

# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(DC_Description_Spider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)
#%%
# parse method
def parse(self, response):
  # Extracted course titles
  crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
  # Extracted course descriptions
  crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
  # Fill in the dictionary
  for crs_title, crs_descr in zip(crs_titles, crs_descrs):
    dc_dict[crs_title] = crs_descr





import scrapy
from scrapy.crawler import CrawlerProcess
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request(url = url_short, callback=self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
    crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
    for crs_title, crs_descr in zip( crs_titles, crs_descrs ):
      dc_dict[crs_title] = crs_descr
    
# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses
previewCourses(dc_dict)