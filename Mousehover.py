import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(5)

account=driver.find_element(By.XPATH,"//a[@id='nav-link-accountList']")
yourorders=driver.find_element(By.XPATH,"//span[normalize-space()='Your Orders']")
language = driver.find_element(By.XPATH,"//span[@class='icp-nav-link-inner']")

actions= ActionChains(driver)
# actions.move_to_element(account).move_to_element(yourorders).perform()

actions.move_to_element(language).perform()
tamil = driver.find_element(By.XPATH,"(//span[contains(@dir,'ltr')][contains(text(),'தமிழ்')])[1]")

actions.move_to_element(tamil).click().perform()
time.sleep(5)
