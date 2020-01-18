from scrapy import Selector
#extract(): extract all lists
#extract_first(): first element of the list

ps = sel.xpath('//p')
second_p = ps[1]
second_p.extract()
#%%
#Example of extract()
rom scrapy import Selector
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