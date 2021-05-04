import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.chrome.options import Options    
from selenium.webdriver.common.by import By       
import xlsxwriter

element_list = []
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'C:\Users\daheekim\Downloads\chromedriver_win32\chromedriver.exe',options=options)
#driver.get('https://www.dnb.com/business-directory/company-information.crop-production.us.html?page=1')
driver.get('https://www.dnb.com/business-directory/company-information.cattle-ranching.us.montana.html?page=1')
 
while True:
    driver.implicitly_wait(10)
    name = driver.find_elements_by_xpath('//*[@id="companyResults"]/div/div[1]')
    address = driver.find_elements_by_xpath('//*[@id="companyResults"]/div/div[2]')
    revenue = driver.find_elements_by_xpath('//*[@id="companyResults"]/div/div[3]')
    for i in range(len(name)):
        #if "South Dakota" in address[i].text or "Montana" in address[i].text:
        element_list.append([name[i].text, address[i].text, revenue[i].text])
    print(i)
    with xlsxwriter.Workbook('result.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        for row_num, data in enumerate(element_list):
            worksheet.write_row(row_num, 0, data)     
    try:
        driver.find_element_by_partial_link_text('Next').click()
    except:
        break
 
driver.quit()
