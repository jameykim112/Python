# Import required packages
from selenium import webdriver #Initialise web browser
import datetime #Print current date
import pandas as pd

#TODO: Refactor code to be OOP
#TODO: Exception handling?
#TODO: Write GitHub User Guide

# Create an Incognito instance of Chrome
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

site_links = ["https://www.danmurphys.com.au/product/DM_38905/hennessy-vs-cognac-700ml", \
              "https://www.danmurphys.com.au/product/DM_49750/maker's-mark-kentucky-straight-bourbon-whisky-700ml", \
              "https://www.danmurphys.com.au/product/DM_904127/grey-goose-vodka-700ml"]
i = 0
for i in range(3):
    # Find the ChromeDriver and get website
    
    browser = webdriver.Chrome(executable_path="/Users/janetyuen/Documents/Side projects/Web Scraping/chromedriver",options=option)
    browser.get(site_links[i])
    #"https://www.danmurphys.com.au/product/DM_38905/hennessy-vs-cognac-700ml"
    # Find price, brand, container using xPath
    #TODO: Can you include multiple find_elements_by_xpath in one line rather than repeating?
    prices = browser.find_element_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/div[1]/aside/shop-add-to-cart/div/div[1]/div/div/p[1]/span')
    product_brand = browser.find_element_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/h1/span[1]')
    product_name = browser.find_element_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/h1/span[2]')

    # Format results to write to text file
    now = datetime.datetime.now()
    now.strftime("%d-%m-%y")

    # Create a Pandas DataFrame 
    prices_df = []
    prices_df.append([now.strftime("%d-%m-%y"),prices.text, product_brand.text, product_name.text])
    data = prices_df[-1][0]+'   '+prices_df[-1][1]+'    '+prices_df[-1][2]+'    '+prices_df[-1][3]

    # Import results to existing text file
    outputFile = open("/Users/janetyuen/Python/WebScraping/webscraping_results.txt","a")
    outputFile.write(data)
    outputFile.write("\n")
    outputFile.close()

    # Close ChromeDriver
    browser.quit()

    # Crontab setup to run code at 10:00am daily
    # When setting up Crontab, absolute paths for Python and Python Script must be used
    # https://crontab.guru/#*_10_*_*_*
    print("Complete")
