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

# Find elements based on xpath, what is xpath?
prices = browser.find_elements_by_xpath('//*[@id="main-content"]/div/shop-product-detail/div/section/div[2]/div/div/div[2]/shop-add-to-cart/div/div[1]/div/div/p[1]/span')
i = 0
for i in range(len(prices)):
    print(prices[i].text)

prices[0].text
