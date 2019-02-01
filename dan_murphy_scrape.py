# Import required packages
from selenium import webdriver #Initialise web browser
from selenium.webdriver.common.by import By #Search for things
from selenium.webdriver.support.ui import WebDriverWait #Wait for page to load
from selenium.webdriver.support import expected_conditions as EC #What to look for on page
from selenium.common.exceptions import TimeoutException #Handling timeout situations

# Create an Incognito instance of Chrome
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

# Find the ChromeDriver and get website
browser = webdriver.Chrome(executable_path="/Users/janetyuen/Documents/2. Side projects/Web Scraping/chromedriver",chrome_options=option)
browser.get("https://www.danmurphys.com.au/product/DM_38905/hennessy-vs-cognac-700ml")
# Note: Include a pause/wait to ensure entire page has loaded before scraping


# Find price, brand, container using xPath
#TODO: Can you include multiple find_elements_by_xpath in one line rather than repeating?
prices = browser.find_elements_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/div[1]/aside/shop-add-to-cart/div/div[1]/div/div/p[1]/span')
product_brand = browser.find_elements_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/h1/span[1]')
product_name = browser.find_elements_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/h1/span[2]')

#TODO: Format results to be included in Excel Workbook
prices[0].text
product_brand[0].text
product_name[0].text

print("Hello World")
