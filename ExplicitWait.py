from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

#Define explicit wait
wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException])

try:
#wait for the element to be clickable
    checkbox = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[3]")))
    checkbox.click()
    print("Checkbox selected")
except Exception as e:
    print("An error occurred:",e)
finally:
    driver.quit()