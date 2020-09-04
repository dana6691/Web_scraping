#################################################################
# Yahoo finance stock information
#################################################################
# Bring 50 active stocks infomation (each page is 25 rows)
# Save a file in csv
#################################################################
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/most-active?count=25&offset="
filename = "stock1-50.csv"
output_rows = []
header = "Symbol	Name	Price (Intraday)	Change	% Change	Volume	Avg Vol (3 month)	Market Cap	PE Ratio (TTM)".split("\t")

for page in range(2):
    res = requests.get(url + str(page*25))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    table = soup.find("table", attrs={"class":"W(100%)"}).find("tbody").find_all("tr")
    for row in table:
        columns = row.find_all("td")
        titles = row.find_all("th")
        title = [title.get_text() for title in titles]
        data = [column.get_text() for column in columns]
        output_rows.append(data)

    with open("/Users/daheekim/Desktop/VisualStudio/Web-scraping-crawling-/BeautifulSoup/" + filename, "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(output_rows)