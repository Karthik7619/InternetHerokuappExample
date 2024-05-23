import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/abtest")
driver.maximize_window()
wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])
expected_result = "A/B Test Variation 12"

try:
    # Wait until the first element is visible
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//h3[normalize-space()='A/B Test Variation 1']"))
    )
    print(element.text)
    # Retrieve the text from the element
    element_text = element.text
    print(element_text)

    # Compare the text with the expected result
    if expected_result in element_text:
        print("Text is present and matches the expected result")
    else:
        print("Text does not match the expected result")

    # Wait until the paragraph element is visible
    element1 = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Also known as split testing. This is a way in whic')]"))
    )

    pattern = "Also known as split testing."
    element1_text = element1.text
    print(f"Paragraph element text: {element1_text}")

    if re.match(pattern,element1_text):
        print("Pattern is matched")
    else:
        print("Pattern is not matched")


except TimeoutException as e:
    print(f"TimeoutException: {str(e)}")
    # Take a screenshot to see the current state of the page
    driver.save_screenshot('timeout_exception_screenshot.png')
    print("Screenshot taken: timeout_exception_screenshot.png")
finally:
    driver.quit()
