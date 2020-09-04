#############################################
# naver.finance
# 1) page 1-3
# 2) extract all data
# 3) save data on csv file
#############################################
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?&page="

filename = "/Users/daheekim/Desktop/VisualStudio/Web-scraping-crawling-/downloads/naverstock.csv"
csvfile  = open(filename, "w", encoding="utf-8-sig",newline='') #change encoding for korean
writer = csv.writer(csvfile)
header = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(header)

for i in range(1,3):
    res = requests.get(url + str(i))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) <=1:
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)