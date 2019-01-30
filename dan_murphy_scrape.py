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
browser.get("https://www.danmurphys.com.au/search?searchTerm=hennessy")

# Find element based on xpath, what is xpath?
prices = browser.find_elements_by_xpath('//span[@class="value"]')
prices[1].text
