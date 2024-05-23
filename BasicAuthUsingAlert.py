import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = f"https://admin:admin@the-internet.herokuapp.com/digest_auth"

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL with embedded credentials
# Navigate to the URL
driver.get(url)
time.sleep(5)
# Verify authentication by checking the page content
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "p"))
    )
    if "Congratulations" in success_message.text:
        print("Successfully authenticated!")
    else:
        print("Failed to authenticate.")
finally:
    # Close the browser
    driver.quit()
