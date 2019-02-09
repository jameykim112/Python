# Import required packages
from selenium import webdriver #Initialise web browser
import datetime #Print current date
import pandas as pd

# Create an Incognito instance of Chrome
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

# Find the ChromeDriver and get website
#TODO: Make URL an input to make solution more flexible
browser = webdriver.Chrome(executable_path="/Users/janetyuen/Documents/Side projects/Web Scraping/chromedriver",options=option)
browser.get("https://www.danmurphys.com.au/product/DM_38905/hennessy-vs-cognac-700ml")

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
data = prices_df[-1][0]+'   '+prices_df[-1][1]

# Import results to existing text file
outputFile = open("/Users/janetyuen/Documents/Side projects/Web Scraping/webscraping_results.txt","a")
outputFile.write(data)
outputFile.write("\n")
outputFile.close()

# Close ChromeDriver
browser.quit()

# Crontab setup to run code at 10:05pm daily
print("Complete")
