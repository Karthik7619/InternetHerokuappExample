import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the URL
url = "https://the-internet.herokuapp.com/disappearing_elements"
driver.get(url)

menu_item = ['Home','About','Contact Us','Portfolio','Gallery']

for menu in menu_item:
    try:
        element = driver.find_element(By.LINK_TEXT,menu)
        element_text=element.text
        if element_text == menu:
            print(f"{menu} is present")
    except NoSuchElementException:
        print(f"{menu} is not present")

driver.quit()