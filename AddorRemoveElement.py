import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Code to select and unselect checkbox

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[normalize-space()='Add Element']").click()

wait = WebDriverWait(driver,10)

button = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[normalize-space()='Delete']")))
button.click()

button1 = wait.until(EC.invisibility_of_element_located((By.XPATH,"//button[normalize-space()='Delete']")))

if button1:
    print("Delete button is not visible")
else:
    print("Delete button is visible")

time.sleep(5)
driver.quit()
