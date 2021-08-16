from selenium import webdriver
from time import sleep
import pandas as pd
browser = webdriver.Chrome(executable_path=r'Project\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def rentalcar(start_date,start_time, end_date,end_time):
    link = "https://www.kayak.com/cars/ORD-a12514/"+ start_date + "-" + start_time + "h/" + end_date + "-" + end_time + "h?sort=rank_a"
    browser.get(link)

    # 'Show more results' Button
    browser.find_element_by_class_name('ULvh-button').click()

    # Order by Cheapest 
    browser.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/button[2]").click()

    # Car Name
    car_name = browser.find_elements_by_xpath("//div[@class='MseY-title js-title']")
    car_namelist = [name.text for name in car_name]
    sleep(4)

    # Car agency, size, prices
    car_sizelist = list()
    car_agencylist = list()
    car_pricelist = list()
    all_spans = browser.find_elements_by_xpath("//div[@class='jo6g']")
    for span in all_spans:
        size = span.find_element_by_class_name("MseY-subTitle").text
        price = span.find_element_by_class_name("EuxN-Current").text
        try:
            agency = span.find_element_by_class_name("mR2O-agencyLogo").get_attribute('alt')
            agency1 = agency.split(": ")[1]
        except Exception as e:
            agency1 = "Surprice Agency"
        car_sizelist.append(size)
        car_agencylist.append(agency1)
        car_pricelist.append(price)

    rentalcar_df = pd.DataFrame({
                                'car':car_namelist,
                                'size':car_sizelist,
                                'agency':car_agencylist,
                                'price':car_pricelist})
    print(rentalcar_df)
    rentalcar_df.to_csv('downloads/rentalcar.csv')

rentalcar(2021_08_21, 10, 2021_08_24, 18)