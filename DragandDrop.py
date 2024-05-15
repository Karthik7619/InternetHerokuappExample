import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Code to select and unselect checkbox

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Drag and Drop").click()

title = driver.find_element(By.XPATH,"//h3[normalize-space()='Drag and Drop']").text
print("------- "+ title + " ------")
wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.ID,"column-a")))
wait.until(EC.presence_of_element_located((By.ID,"column-b")))

# Drag and Drop
source= driver.find_element(By.ID,"column-a")
target= driver.find_element(By.ID,"column-b")

action = ActionChains(driver)
# 1st method using drag and drop method from action
# action.drag_and_drop(source,target).perform()

# 2nd method using drag and drop method from action
# action.drag_and_drop(source,100,200).perform()


# 3rd method using click and hold
# action.click_and_hold(source).move_to_element(target).release().perform()

# 4th method using click and hold using offset method
action.click_and_hold(source).move_by_offset(100,100).release().perform()

# 5th method using click and hold using offset method
# action.click_and_hold(source).move_to_element_with_offset(target,150,150).release().perform()

time.sleep(3)

# action = ActionChains(driver)
# action.drag_and_drop(target,source)
#
# time.sleep(5)