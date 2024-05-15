import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/context_menu")
driver.maximize_window()
time.sleep(5)
box = driver.find_element(By.ID,"hot-spot")

# Context_Click() = Right click
actions = ActionChains(driver)
actions.move_to_element(box).context_click(box).perform()

time.sleep(2)

alertwindow = driver.switch_to.alert
alertwindow.accept()

time.sleep(3)