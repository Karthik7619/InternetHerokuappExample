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
driver.get("https://demoqa.com/links")
driver.maximize_window()
# driver.(By.XPATH,"//body/iframe[1]")

wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
# linkedtext = driver.find_element(By.LINK_TEXT,"Moved")

try:
    element = wait.until(
        EC.visibility_of_element_located((By.ID, "google_ads_iframe_/21849154601,22343295815/Ad.Plus-Anchor_0")) and
        EC.element_to_be_clickable((By.LINK_TEXT,"Moved"))
    )
    # Scroll to the element using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.click()
    print("Clicked")

except TimeoutException:
    print("Element is not clickable")

try:
    element1 = wait.until(
            EC.visibility_of_element_located((By.XPATH,"//b[normalize-space()='Moved Permanently']"))
        )
    if element1.text == "Moved Permanently":
        print("Message is visible")
        print(element1.text)
except TimeoutException:
    print("An error occurred")
finally:
    driver.quit()