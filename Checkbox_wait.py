from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open a website
driver.get("https://the-internet.herokuapp.com/checkboxes")

# Define the wait with ignored exceptions
wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])

# try:
    # Wait for the element to be present in the DOM and visible
element = wait.until(EC.element_to_be_clickable((By.XPATH,"//input[3]")))
    # Perform action with the element
element.click()
print("Element clicked successfully!")
# except Exception as e:
# print("An error occurred: ", e)
# finally:
    # Close the browser
driver.quit()
