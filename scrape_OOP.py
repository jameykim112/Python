# * https://realpython.com/python3-object-oriented-programming/
# WebScraping script created as Object Orientated Programming

from selenium import webdriver
import datetime
import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
now = datetime.datetime.now()
now.strftime("%d-%m-%y")

class scrape:

    # Initializer / Instance attribute
    def __init__(self, url):
        self.url = url

    def scrapeData(self, xcode):
        self.xcode = xcode
        browser = webdriver.Chrome(executable_path="/Users/janetyuen/Documents/Side projects/Web Scraping/chromedriver",options=option)
        browser.get(self.url)
        self.data = browser.find_element_by_xpath(self.xcode)
        return self.data.text
    # Instance method
    #TODO: Append pricing data to existing text file
    def create_df(self, scraped_data, csv_file):
        data_df = pd.DataFrame(scraped_data)

    # Instance method
    #TODO: Append df to existing csv or create new csv
    

DanMurphys = scrape("https://www.danmurphys.com.au/product/DM_38905/hennessy-vs-cognac-700ml")
DanMurphys.extract('//*[@id="main-content"]/div/shop-product-detail/div/section/h1/span[1]')



