import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Code to select and unselect checkbox 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[normalize-space()='Checkboxes']").click()
time.sleep(5)

print(driver.find_element(By.XPATH,"//input[1]").is_displayed())
print(driver.find_element(By.XPATH,"//input[1]").is_enabled())

# Checkbox1
checkbox1 = driver.find_element(By.XPATH,"//input[1]").is_selected()
if not checkbox1:
    print("Checkbox not selected")
    driver.find_element(By.XPATH, "//input[1]").click()
else:
    print("Checkbox is selected")
    driver.find_element(By.XPATH, "//input[1]").click()

time.sleep(5)

# Checkbox2
driver.find_element(By.XPATH,"//input[2]").is_displayed()
driver.find_element(By.XPATH,"//input[2]").is_enabled()
checkbox2 = driver.find_element(By.XPATH,"//input[2]").is_selected()
if checkbox2:
    print("Checkbox is selected")
    driver.find_element(By.XPATH, "//input[2]").click()
else:
    print("Checkbox is not selected")

time.sleep(5)
