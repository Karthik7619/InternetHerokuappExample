import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(10)

url = f"https://admin:admin1@the-internet.herokuapp.com/basic_auth"

driver.get(url)
# time.sleep(5)

if "Congratulations" in driver.page_source:

    print("Successful")
else:
    print("Not Successful")

driver.quit()




